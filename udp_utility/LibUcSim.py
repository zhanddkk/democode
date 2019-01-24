from upsethernetprotocol import UpsEthernetProtocol, UpsEthernetProtocolFrame, UepMessageReader, MessageIdFrameFilter
from struct import Struct
import SysInfoDataMap
from robot.libraries.BuiltIn import BuiltIn
from typing import Union


class SimDataPackage:
    # 4 bit
    DATA_INVALID = SysInfoDataMap.SYS_INFO_DATA_INVALID
    DATA_BOOL = SysInfoDataMap.SYS_INFO_DATA_BOOL
    DATA_INT8 = SysInfoDataMap.SYS_INFO_DATA_INT8
    DATA_INT16 = SysInfoDataMap.SYS_INFO_DATA_INT16
    DATA_INT32 = SysInfoDataMap.SYS_INFO_DATA_INT32
    DATA_F32 = SysInfoDataMap.SYS_INFO_DATA_F32
    DATA_BYTE_BUF = 0x6
    DATA_SIZE = 0x7

    # 4 bit
    OPT_SET = 0x0
    OPT_GET = 0x1
    OPT_CMD = 0x2

    # 8 bit
    RESPONSE_SUCCEED = 0x00
    RESPONSE_FAILED = 0x01
    RESPONSE_DATA_BACK = 0x02
    RESPONSE_NO_USE = 0xff

    HEAD_SIZE = 12
    MAX_DATA_SIZE = UpsEthernetProtocolFrame.MAX_DATA_SIZE - HEAD_SIZE

    __name_type = {
        DATA_INVALID: 'invalid',
        DATA_BOOL: 'bool',
        DATA_INT8: 'int8',
        DATA_INT16: 'int16',
        DATA_INT32: 'int32',
        DATA_F32: 'float',
        DATA_BYTE_BUF: 'byte buffer',
        DATA_SIZE: 'size'
    }

    __name_operation = {
        OPT_SET: 'SET',
        OPT_GET: 'GET',
        OPT_CMD: 'CMD'
    }

    __name_response = {
        RESPONSE_SUCCEED: 'SUCCEED',
        RESPONSE_FAILED: 'FAILED',
        RESPONSE_DATA_BACK: 'DATA BACK',
        RESPONSE_NO_USE: 'NO USE'
    }

    def __init__(self):
        self.__eid = 0
        self.__type = self.DATA_INVALID
        self.__operation = self.OPT_SET
        self.__response = self.RESPONSE_NO_USE
        self.__index = 0
        self.__value = None

        self.__value_format_dic = {
            self.DATA_BOOL: ('?', 1),
            self.DATA_INT8: ('B', 1),
            self.DATA_INT16: ('h', 2),
            self.DATA_INT32: ('l', 4),
            self.DATA_F32: ('f', 4),
            self.DATA_SIZE: ('L', 4)
        }
        self.__head_format = Struct('<HBBL')
        pass

    @staticmethod
    def __name_width(names: dict):
        _width = 0
        for _name in names.values():
            _tmp = len(_name)
            if _width < _tmp:
                _width = _tmp
                pass
            pass
        return _width
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
        self.__operation = val & 0b1111
        pass

    @property
    def response(self):
        return self.__response
        pass

    @response.setter
    def response(self, val: int):
        self.__response = val & 0xff
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
        _val_structure = None
        try:
            _val_structure = Struct('<{}'.format(self.__value_format_dic[self.__type][0]))
            pass
        except KeyError:
            pass
        if (self.__operation == self.OPT_SET) or (self.__operation == self.OPT_CMD):
            _info = (self.__type << 4) | self.__operation
            pass
        elif self.__operation == self.OPT_GET:
            _info = (self.DATA_INVALID << 4) | self.__operation
            pass
        else:
            raise ValueError('Invalid operation {}'.format(self.__operation))
        _data = self.__head_format.pack(self.__eid, _info, self.__response, self.__index)
        if self.__operation == self.OPT_SET:
            if isinstance(_val_structure, Struct):
                _data = _data + _val_structure.pack(self.__value)
                pass
            pass
        elif self.__operation == self.OPT_CMD:
            if isinstance(_val_structure, Struct):
                _data = _data + _val_structure.pack(self.__value)
                pass
            else:
                if self.__type == self.DATA_BYTE_BUF:
                    if isinstance(self.__value, bytes):
                        _data = _data + self.__value
                        pass
                    elif isinstance(self.__value, bytearray):
                        _data = _data + bytes(self.__value)
                        pass
                    else:
                        pass
                    pass
                pass
            pass
        else:
            pass
        return _data

    @data.setter
    def data(self, val: bytearray):
        self.__eid, _info, self.__response, self.__index = self.__head_format.unpack(val[:8])
        self.__operation = _info & 0xf
        self.__type = (_info >> 4) & 0xf
        _val_structure = None
        _dln = None
        try:
            _tmp = self.__value_format_dic[self.__type]
            _val_structure = Struct('<{}'.format(_tmp[0]))
            _dln = _tmp[1]
            pass
        except KeyError:
            pass
        if isinstance(_val_structure, Struct):
            self.__value = _val_structure.unpack(val[8: 8 + _dln])[0]
            pass
        else:
            if self.__operation == self.OPT_CMD:
                if self.__type == self.DATA_BYTE_BUF:
                    self.__value = bytes(val[8:])
                    pass
                pass
            pass
        pass

    def __str__(self):
        try:
            _type = '{:0>1X}({})'.format(self.__type, self.__name_type[self.__type])
            pass
        except KeyError:
            _type = '{:0>1X}'.format(self.__type)
            pass
        try:
            _opt = '{:0>1X}({})'.format(self.__operation, self.__name_operation[self.__operation])
            pass
        except KeyError:
            _opt = '{:0>1X}'.format(self.__operation)
            pass
        try:
            _rsp = '{:0>2X}({})'.format(self.__response, self.__name_response[self.__response])
            pass
        except KeyError:
            _rsp = '{:0>2X}'.format(self.__response)
            pass
        return 'id:{:0>4X}, type:{}, operation:{}, response:{}, index:{}, value:{}'.format(
            self.__eid,
            _type,
            _opt,
            _rsp,
            self.__index,
            self.__value
        )
        pass
    pass


class LibUcSim(object):

    ROBOT_LIBRARY_VERSION = 1.0
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.__uep_server = None
        self.__uc_sim_reader = UepMessageReader(MessageIdFrameFilter(message_id=0xFFFFFFFE))
        pass

    @property
    def _uep_server(self)->UpsEthernetProtocol:
        if isinstance(self.__uep_server, UpsEthernetProtocol):
            return self.__uep_server
        else:
            raise SystemError('Uc simulator not be initialized')

    def uc_sim_initialize_library(self, uep_server: UpsEthernetProtocol=None):
        if isinstance(uep_server, UpsEthernetProtocol):
            _selected_uep_server = uep_server
            pass
        else:
            _lib_uep = BuiltIn().get_library_instance('TestLibraries.LibUep')
            _selected_uep_server = _lib_uep.uep_server
            if not isinstance(_selected_uep_server, UpsEthernetProtocol):
                raise SystemError('Uep server of LibUep is not started')
            pass

        if isinstance(self.__uep_server, UpsEthernetProtocol):
            if _selected_uep_server == self.__uep_server:
                _next_uep_server = None
                pass
            else:
                self.__uep_server.remove_reader(self.__uc_sim_reader)
                _next_uep_server = _selected_uep_server
                pass
            pass
        else:
            _next_uep_server = _selected_uep_server
            pass
        self.__uc_sim_reader.reset()
        if isinstance(_next_uep_server, UpsEthernetProtocol):
            self.__uep_server = _next_uep_server
            self.__uep_server.append_reader(self.__uc_sim_reader)
            pass
        pass

    def uc_sim_set_the_value_of_sys_info(self, sys_id: int, index: int, val):
        _pkg = SimDataPackage()
        try:
            _pkg.eid = sys_id
            _pkg.type, _len = SysInfoDataMap.sys_info_data_map[sys_id]
            if (index >= _len) or (index < 0):
                raise ValueError('index({}) is out of range'.format(index))
            _pkg.index = index
            _pkg.operation = SimDataPackage.OPT_SET
            _pkg.value = val

            _data = _pkg.data
            _frame = self.__create_uep_frame()
            _frame.data = _data
            print('[>]:', _pkg)
            self._uep_server.send_frame(_frame)

            _frame_r = self._uep_server.read_frame(self.__uc_sim_reader, 15)
            if _frame_r:
                _pkg_r = SimDataPackage()
                _data_r = _frame_r.data[:_frame_r.data_length_count]
                _pkg_r.data = _data_r
                print('[<]:', _pkg_r)
                if _pkg_r.response == _pkg_r.RESPONSE_FAILED:
                    raise IOError('Set sys info({:0>4X} failed)'.format(sys_id))
                pass
            else:
                raise IOError('Sys info({:0>4X}) not response'.format(sys_id))
            pass
        except KeyError:
            raise ValueError('Sys info id({:0>4X}) is not supported'.format(sys_id))
        pass

    def uc_sim_get_the_value_of_sys_info(self, sys_id: int, index: int):
        _pkg = SimDataPackage()
        try:
            _pkg.eid = sys_id
            _pkg.type, _len = SysInfoDataMap.sys_info_data_map[sys_id]
            if (index >= _len) or (index < 0):
                raise ValueError('index({}) is out of range'.format(index))
            _pkg.index = index
            _pkg.operation = SimDataPackage.OPT_GET

            _data = _pkg.data
            _frame = self.__create_uep_frame()
            _frame.data = _data
            print('[>]:', _pkg)
            self._uep_server.send_frame(_frame)

            _frame_r = self._uep_server.read_frame(self.__uc_sim_reader, 15)
            if _frame_r:
                _pkg_r = SimDataPackage()
                _data_r = _frame_r.data[:_frame_r.data_length_count]
                _pkg_r.data = _data_r
                print('[<]:', _pkg_r)
                if _pkg_r.response == _pkg_r.RESPONSE_FAILED:
                    raise IOError('Set sys info({:0>4X}) failed'.format(sys_id))
                return _pkg_r.value
                pass
            else:
                raise IOError('Sys info({:0>4X}) not response'.format(sys_id))
            pass
        except KeyError:
            raise ValueError('Sys info id({:0>4X}) is not supported'.format(sys_id))
        pass

    def uc_sim_command_step_send(self, command_id, index, val_type=SimDataPackage.DATA_INVALID, val=None):
        _pkg = SimDataPackage()
        _pkg.eid = command_id
        _pkg.index = index
        _pkg.operation = SimDataPackage.OPT_CMD
        _pkg.type = val_type
        if _pkg.type != SysInfoDataMap.SYS_INFO_DATA_INVALID:
            _pkg.value = val

        _data = _pkg.data
        _frame = self.__create_uep_frame()
        _frame.data = _data
        print('[>]:', _pkg)
        self._uep_server.send_frame(_frame)
        pass

    def uc_sim_command_step_wait_response(self, command_id, index, timeout: int=5):
        _frame_r = self._uep_server.read_frame(self.__uc_sim_reader, timeout)
        if _frame_r:
            _pkg_r = SimDataPackage()
            _data_r = _frame_r.data[:_frame_r.data_length_count]
            _pkg_r.data = _data_r
            print('[<]:', _pkg_r)
            if _pkg_r.response == _pkg_r.RESPONSE_FAILED:
                raise ValueError('Send command({:0>4X} | {}) failed'.format(command_id, index))
            elif _pkg_r.response == _pkg_r.RESPONSE_DATA_BACK:
                return _pkg_r.value
            else:
                return None
            pass
        else:
            raise SystemError('Command({:0>4X} | {}) not response'.format(command_id, index))
        pass

    def uc_sim_send_command(self, command_id, index, val_type=SimDataPackage.DATA_INVALID, val=None):
        self.uc_sim_command_step_send(command_id, index, val_type, val)
        return self.uc_sim_command_step_wait_response(command_id, index)
        pass

    def uc_sim_send_command_with_multi_data(self, command_id, data: Union[bytearray, bytes]):
        _len = len(data)
        _i = 0
        _index = 0
        self.uc_sim_send_command(command_id, 0, SimDataPackage.DATA_SIZE, _len)
        while True:
            _start = _i
            if _i + SimDataPackage.MAX_DATA_SIZE > _len:
                _i = _len
                pass
            else:
                _i += SimDataPackage.MAX_DATA_SIZE
                pass
            self.uc_sim_send_command(0xfffe, _index, SimDataPackage.DATA_BYTE_BUF, data[_start:_i])
            if _i >= _len:
                break
                pass
            _index += 1
            pass
        pass

    def uc_sim_get_multi_data_of_command(self, command_id):
        self.uc_sim_command_step_send(command_id, 0)
        _ret = bytearray()
        while True:
            _data = self.uc_sim_command_step_wait_response(command_id, 0)
            if _data is None:
                break
                pass
            else:
                _ret = _ret + _data
                pass
            pass
        return bytes(_ret)
        pass

    # TODO: Those functions will be move to other libraries
    def send_cmd_to_enable_uc_simulate(self):
        self.uc_sim_send_command(0x0001, 0)
        pass

    def send_cmd_to_disable_uc_simulate(self):
        self.uc_sim_send_command(0x0002, 0)
        pass

    # Main 1
    def change_the_input_voltage_of_main_1_to(self, voltage: float):
        self.uc_sim_send_command(0x0003, 0, SysInfoDataMap.SYS_INFO_DATA_F32, voltage)
        pass

    def change_3_ph_input_voltage_of_main_1_to(self, voltage1: float, voltage2: float, voltage3: float):
        _format = Struct('<fff')
        _data = _format.pack(voltage1, voltage2, voltage3)
        self.uc_sim_send_command(0x0003, 0, SimDataPackage.DATA_BYTE_BUF, _data)
        pass
    
    def set_the_input_voltage_noise_ampl_of_main_1_to(self, ampl: float):
        self.uc_sim_send_command(0x0006, 0, SysInfoDataMap.SYS_INFO_DATA_F32, ampl)
        pass

    def set_3_ph_input_voltage_noise_ampl_of_main_1_to(self, voltage1: float, voltage2: float, voltage3: float):
        _format = Struct('<fff')
        _data = _format.pack(voltage1, voltage2, voltage3)
        self.uc_sim_send_command(0x0006, 0, SimDataPackage.DATA_BYTE_BUF, _data)
        pass

    # Main 2
    def change_the_input_voltage_of_main_2_to(self, voltage: float):
        self.uc_sim_send_command(0x0004, 0, SysInfoDataMap.SYS_INFO_DATA_F32, voltage)
        pass

    def change_3_ph_input_voltage_of_main_2_to(self, voltage1: float, voltage2: float, voltage3: float):
        _format = Struct('<fff')
        _data = _format.pack(voltage1, voltage2, voltage3)
        self.uc_sim_send_command(0x0004, 0, SimDataPackage.DATA_BYTE_BUF, _data)
        pass

    def set_the_input_voltage_noise_ampl_of_main_2_to(self, ampl: float):
        self.uc_sim_send_command(0x0007, 0, SysInfoDataMap.SYS_INFO_DATA_F32, ampl)
        pass

    def set_3_ph_input_voltage_noise_ampl_of_main_2_to(self, voltage1: float, voltage2: float, voltage3: float):
        _format = Struct('<fff')
        _data = _format.pack(voltage1, voltage2, voltage3)
        self.uc_sim_send_command(0x0007, 0, SimDataPackage.DATA_BYTE_BUF, _data)
        pass

    # Output
    def change_the_output_voltage_to(self, voltage: float):
        self.uc_sim_send_command(0x0005, 0, SysInfoDataMap.SYS_INFO_DATA_F32, voltage)
        pass

    def change_3_ph_output_voltage_to(self, voltage1: float, voltage2: float, voltage3: float):
        _format = Struct('<fff')
        _data = _format.pack(voltage1, voltage2, voltage3)
        self.uc_sim_send_command(0x0005, 0, SimDataPackage.DATA_BYTE_BUF, _data)
        pass

    def set_the_output_voltage_noise_ampl_to(self, ampl: float):
        self.uc_sim_send_command(0x0008, 0, SysInfoDataMap.SYS_INFO_DATA_F32, ampl)
        pass

    def set_3_ph_output_voltage_noise_ampl_to(self, voltage1: float, voltage2: float, voltage3: float):
        _format = Struct('<fff')
        _data = _format.pack(voltage1, voltage2, voltage3)
        self.uc_sim_send_command(0x0008, 0, SimDataPackage.DATA_BYTE_BUF, _data)
        pass

    @staticmethod
    def __create_uep_frame() -> UpsEthernetProtocolFrame:
        _frame = UpsEthernetProtocolFrame()
        _frame.protocol_id = 0x0f
        _frame.source = 0x21
        _frame.priority = 0b0
        _frame.message_type = 0b111
        _frame.message_id = 0xFFFFFFFE
        return _frame
        pass

# ======================================================================================================================
# Example For Test
# ----------------------------------------------------------------------------------------------------------------------


def test_sys_info(sim: LibUcSim):
    sim.uc_sim_set_the_value_of_sys_info(SysInfoDataMap.eSysId_OutFreqToleranceSetting, 0, 128)
    sim.uc_sim_set_the_value_of_sys_info(SysInfoDataMap.eSysId_OutVolCompSetting, 0, 256)
    sim.uc_sim_set_the_value_of_sys_info(SysInfoDataMap.eSysId_InvSysCtrlTransition, 0, 65536)
    sim.uc_sim_set_the_value_of_sys_info(SysInfoDataMap.eSysId_MinChgVolRef, 0, 220.79)

    print(sim.uc_sim_get_the_value_of_sys_info(SysInfoDataMap.eSysId_OutFreqToleranceSetting, 0))
    print(sim.uc_sim_get_the_value_of_sys_info(SysInfoDataMap.eSysId_OutVolCompSetting, 0))
    print(sim.uc_sim_get_the_value_of_sys_info(SysInfoDataMap.eSysId_InvSysCtrlTransition, 0))
    print(sim.uc_sim_get_the_value_of_sys_info(SysInfoDataMap.eSysId_MinChgVolRef, 0))
    pass


def test_sim_command(sim: LibUcSim):
    import time
    sim.uc_sim_send_command(0x0001, 0)
    time.sleep(0.5)
    sim.uc_sim_send_command(0x0002, 0)
    time.sleep(1)
    sim.uc_sim_send_command(0x0001, 0)
    time.sleep(0.5)
    sim.uc_sim_send_command(0x0002, 0)

    sim.change_the_input_voltage_of_main_1_to(100.0)
    sim.change_3_ph_input_voltage_of_main_1_to(23.5, 37.8, 96.3)
    sim.set_the_input_voltage_noise_ampl_of_main_1_to(128.7)
    sim.set_3_ph_input_voltage_noise_ampl_of_main_1_to(100.0, 234.1, 123.2)

    _data = bytearray(1024)
    for _i in range(len(_data)):
        _data[_i] = _i & 0xff
        pass
    _data[0] = 1
    sim.uc_sim_send_command_with_multi_data(0xfffe, _data)
    _data = sim.uc_sim_get_multi_data_of_command(0xffff)

    _output = ''
    for _i in range(len(_data)):
        _output += '{:0>2X}'.format(_data[_i])
        if _i % 16 == 15:
            print(_output)
            _output = ''
            pass
        else:
            _output += ' '
            pass
    pass


def main():
    _uep = UpsEthernetProtocol(remote='192.168.10.129', remote_port=8081,
                               local='0.0.0.0', local_port=8081)
    _reader = UepMessageReader(MessageIdFrameFilter(message_id=0xFFFFFFFE))
    _uep.append_reader(_reader)
    _uep.start_server()
    _uc_sim = LibUcSim()
    _uc_sim.uc_sim_initialize_library(_uep)
    test_sys_info(_uc_sim)
    test_sim_command(_uc_sim)
    _uep.stop_server()
    print('==== exit ====')
    pass


if __name__ == '__main__':
    main()
    pass
