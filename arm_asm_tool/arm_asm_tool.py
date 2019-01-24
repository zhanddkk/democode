
class Item:
    def __init__(self, line):
        self.__parse_line(line)
        self.__address = 0
        pass

    def address(self):
        pass

    def operation_code(self):
        pass

    def instruction(self):
        pass

    def contents(self):
        pass

    def comment(self):
        pass

    def __parse_line(self, line):
        _step = 0
        _tmp_txt = ''
        for _ch in line:
            if _step == 0:
                if _ch == '\t':
                    _tmp_txt = '0x' + _tmp_txt.strip().rstrip(':')
                    self.__address = int(_tmp_txt, base=16)
                    _tmp_txt = ''
                    _step += 1
                    pass
                pass
            elif _step == 1:
                if _ch == '\t':
                    _tmp_txt = '0x' + _tmp_txt.strip().rstrip(':')
                    self.operation_code = int(_tmp_txt, base=16)
                    _tmp_txt = ''
                    _step += 1
                    pass
                pass
            elif _step == 2:
                if _ch == '\t':
                    _tmp_txt = _tmp_txt.strip().rstrip(':')
                    self.operation_code = int(_tmp_txt, base=16)
                    _tmp_txt = ''
                    _step += 1
                    pass
                pass
            pass
        pass
    pass


def main():
    with open('irom.dis', 'r') as rf:
        with open('irom.s', 'w') as wf:
            for _line in rf:
                if _line != '':
                    pass
                pass
            pass
        # _line = rf.readline()
        pass
    pass


if __name__ == '__main__':
    pass
