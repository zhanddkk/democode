import threading


class Package:
    def __init__(self, msg_type):
        self.__type = msg_type
        # self.__length = 0
        self.__data = bytearray()
        # self.__check_sum = 0
        # self.__buffer = bytearray()
        pass

    @property
    def data(self):
        _data = bytearray()
        _len = len(self.__data)
        _check_sum = 0
        if self.__type == '1':
            pass

        for _v in self.__data:
            _check_sum += _v
            _check_sum &= 0xffffffff

            pass
        return _data
        pass

    pass


class FirmwareUpdater(threading.Thread):
    def __init__(self, firmware):
        super(FirmwareUpdater, self).__init__()
        self.__fw = firmware
        pass

    def update(self):
        pass

    def run(self):
        pass

    pass


if __name__ == '__main__':
    pass
