from upsethernetprotocol import UpsEthernetProtocol, UpsEthernetProtocolFrame, MessageIdFrameFilter
from queue import Empty, Queue
import threading
from struct import Struct
from sysinfoeid import *


class SimDataPackage:
    DATA_INVALID = 0x00
    DATA_BOOL = 0x01
    DATA_INT8 = 0x02
    DATA_INT16 = 0x03
    DATA_INT32 = 0x04
    DATA_F32 = 0x05

    OPT_SET = 0x0
    OPT_GET = 0x1
    OPT_CMD = 0x2

    RESPONSE_SUCCEED = 0x0
    RESPONSE_FAILED = 0x1

    def __init__(self):
        self.__eid = 0
        self.__type = self.DATA_INVALID
        self.__operation = self.OPT_SET
        self.__response = self.RESPONSE_FAILED
        self.__index = 0
        self.__value = None

        self.__value_format_dic = {
            self.DATA_BOOL: '?',
            self.DATA_INT8: 'B',
            self.DATA_INT16: 'h',
            self.DATA_INT32: 'l',
            self.DATA_F32: 'f',
        }
        pass

    @property
    def eid(self):
        return self.__index
        pass

    @eid.setter
    def eid(self, val: int):
        self.__eid = val
        pass

    @property
    def type(self):
        return self.__type
        pass

    @type.setter
    def type(self, val: int):
        self.__type = val & 0b1111
        pass

    @property
    def operation(self):
        return self.__operation
        pass

    @operation.setter
    def operation(self, val: int):
        self.__operation = val & 0b11
        pass

    @property
    def response(self):
        return self.__response
        pass

    @response.setter
    def response(self, val: int):
        self.__response = val & 0b11
        pass

    @property
    def index(self):
        return self.__index
        pass

    @index.setter
    def index(self, val: int):
        self.__index = val
        pass

    @property
    def value(self):
        return self.__value
        pass

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def data(self):
        _info = (self.__type << 4) | (self.__operation << 2) | self.__response
        if (self.__operation == self.OPT_SET) or (self.__operation == self.OPT_CMD):
            if self.__type == self.DATA_INVALID:
                _pkg_structure = Struct('<HBB')
                _data = _pkg_structure.pack(self.__eid, _info, self.__index)
                pass
            else:
                try:
                    _format = '<HBB{}'.format(self.__value_format_dic[self.__type])
                    pass
                except KeyError:
                    raise ValueError('invalid package with invalid type {}'.format(self.__type))
                    pass
                _pkg_structure = Struct(_format)
                _data = _pkg_structure.pack(self.__eid, _info, self.__index, self.__value)
                pass
            pass
        elif self.__operation == self.OPT_GET:
            _info &= 0b00001100
            _pkg_structure = Struct('<HBB')
            _data = _pkg_structure.pack(self.__eid, _info, self.__index)
            pass
        else:
            _data = bytearray()
            pass
        return _data

    @data.setter
    def data(self, val: bytearray):
        _head_format = Struct('<HBB')
        self.__eid, _info, self.__index = _head_format.unpack(val[:4])
        self.__type = (_info >> 4) & 0b1111
        self.__operation = (_info & 0b1100) >> 2
        self.__response = _info & 0b11
        if self.__type == self.DATA_INVALID:
            pass
        else:
            try:
                _format = '<{}'.format(self.__value_format_dic[self.__type])
                _value_format = Struct(_format)
                self.__value = _value_format.unpack(val[4:8])[0]
                pass
            except KeyError:
                _code = ', '.join('{:0>2X}'.format(_v) for _v in val)
                raise ValueError('invalid package data({})'.format(_code))
            pass
        pass

    def __str__(self):
        return 'id:{:0>4X}, type:{}, operation:{}, response:{}, index:{}, value:{}'.format(
            self.__eid,
            self.__type,
            self.__operation,
            self.__response,
            self.__index,
            self.__value
        )
        pass
    pass


def __process_cmd_line(cmd: str):
    _t_args = cmd.split(' ')
    _args = []
    for _v in _t_args:
        _tv = _v.strip()
        if _tv:
            _args.append(_tv)

    if _args[0] == 'STOP':
        pass
    pass

# Test steps:
# Device/UC/Status/CommunicationStatus -> 2 | Authenticated
# Device/UC/Status/SystemConfigured -> 0 | StateOK
# Set the input voltage -> 120.0
# UPSSystem/InputSystem/Status/Mains1PhaseVoltageStatus -> 2 | StateLow
# Set the input voltage -> 325.0
# UPSSystem/InputSystem/Status/Mains1PhaseVoltageStatus -> 0 | StateInBand


def __demo_task(host, port, cmd_line_queue, cmd_line_processed):
    _ups_ethernet_protocol = UpsEthernetProtocol(remote=host, remote_port=port, local='0.0.0.0', local_port=port)
    _ups_ethernet_protocol.set_frame_filter(MessageIdFrameFilter(message_id=0x0000000D))
    _ups_ethernet_protocol.start_server()

    _demo_packages = (
        (eSysId_ParUpsDevMgrOpMode, SimDataPackage.DATA_INT32, 1, 65538),
        (eSysId_OutPhPhVolSetting, SimDataPackage.DATA_INT16, 0, 258),
        (eSysId_OutFreqSetting, SimDataPackage.DATA_INT8, 0, 56),
        (eSysId_ChgRegVolRef, SimDataPackage.DATA_F32, 0, 78.9),
        (eSysId_SlcChgEn, SimDataPackage.DATA_BOOL, 0, False),
        (0x0001, SimDataPackage.DATA_INVALID, 0, None),
        (0x0002, SimDataPackage.DATA_INVALID, 0, None),
        (0x0003, SimDataPackage.DATA_F32, 0, 100.0),
    )

    while True:
        _frame = _ups_ethernet_protocol.read_frame(1)
        if _frame:
            print('UEP frame: {}'.format(_frame))
            _data = _frame.data[:_frame.data_length_count]
            print('received: ', ', '.join('{:0>2X}'.format(_v) for _v in _data))
            _pkg = SimDataPackage()
            _pkg.data = _data
            print('Sim Data:', _pkg)
            pass
        else:
            pass

        try:
            _cmd = cmd_line_queue.get(timeout=0.1)
            _t_args = _cmd.split(' ')
            _args = []
            for _v in _t_args:
                _tv = _v.strip()
                if _tv:
                    _args.append(_tv)
                    pass
                pass
            if len(_args) > 0:
                _opt = _args[0].upper()
                if _opt == 'STOP':
                    _ups_ethernet_protocol.stop_server()
                    cmd_line_processed.set()
                    return
                elif (_opt == 'SET') or (_opt == 'GET') or (_opt == 'CMD'):
                    if len(_args) > 1:

                        _index = int(_args[1])
                        _pkg = SimDataPackage()
                        _pkg.eid, _pkg.type, _pkg.index, _pkg.value = _demo_packages[_index]
                        if _opt == 'SET':
                            _pkg.operation = SimDataPackage.OPT_SET
                            pass
                        elif _opt == 'GET':
                            _pkg.operation = SimDataPackage.OPT_GET
                            pass
                        elif _opt == 'CMD':
                            _pkg.operation = SimDataPackage.OPT_CMD
                            pass
                        else:
                            pass

                        _frame = UpsEthernetProtocolFrame()
                        _frame.protocol_id = 0x0f
                        _frame.source = 0x21
                        _frame.priority = 0b0
                        _frame.message_type = 0b111
                        _frame.message_id = 0x0000000D
                        _data = _pkg.data
                        _frame.set_data(_data, 8)

                        print('send: ', ', '.join('{:0>2X}'.format(_v) for _v in _frame.data))

                        _ups_ethernet_protocol.send_frame(_frame)
                        pass
                    pass
                elif _opt == 'FID':
                    if len(_args) > 1:
                        _id = int(_args[1].strip())
                        _ups_ethernet_protocol.set_frame_filter(MessageIdFrameFilter(_id))
                    pass
            cmd_line_processed.set()
        except Empty:
            pass
    pass


def demo(host, port):
    import sys
    _cmd_line_queue = Queue()
    _cmd_line_processed = threading.Event()
    _demo_sub_thread = threading.Thread(target=__demo_task,
                                        args=(host, port, _cmd_line_queue, _cmd_line_processed))
    _demo_sub_thread.start()
    while True:
        line = sys.stdin.readline()
        _cmd_line_processed.clear()
        _cmd_line_queue.put(line)
        while not _cmd_line_processed.isSet():
            pass
        if not _demo_sub_thread.isAlive():
            break
    pass


if __name__ == '__main__':
    demo('192.168.10.129', 8081)
    pass
