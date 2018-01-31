
class Item:
    def __init__(self, line):
        self.__name = None
        self.__address = None
        self.__permission = None
        self.__comments = ''
        self.__len = 1
        self.__data_type = 'uint32_t'
        self.id = None
        self.__parse_line(line)
        pass

    @property
    def name(self):
        return self.__name
        pass

    @property
    def address(self):
        return self.__address
        pass

    @property
    def permission(self):
        return self.__permission
        pass

    @property
    def comments(self):
        return self.__comments
        pass

    @property
    def len(self):
        return self.__len
        pass

    @property
    def data_type(self):
        return self.__data_type
        pass

    def __parse_line(self, line):
        if isinstance(line, str):
            _tmp_txt = ''
            _step = 0
            for _ch in line:
                if (_ch == ' ') and (_step < 3):
                    if _tmp_txt != '':
                        if _step == 0:
                            self.__name = str(_tmp_txt)
                            _tmp_txt = ''
                            _step += 1
                            pass
                        elif _step == 1:
                            _tmp_txt = _tmp_txt.replace('_', '')
                            _tmp_txt = _tmp_txt.split('~')
                            _start = int(_tmp_txt[0], base=16)
                            try:
                                _end = int(_tmp_txt[1], base=16)
                                if _start > _end:
                                    _tmp = _end
                                    _end = _start
                                    _start = _tmp
                                self.__len = ((_end - _start) >> 2) + 1
                                self.__address = (_start, _end)
                            except IndexError:
                                self.__address = (_start, None)
                            _tmp_txt = ''
                            _step += 1
                            pass
                        elif _step == 2:
                            if (_tmp_txt == 'R') or (_tmp_txt == '-'):
                                self.__permission = '__O'
                            elif _tmp_txt == 'W':
                                self.__permission = '__I'
                            elif _tmp_txt == 'R/W':
                                self.__permission = '__IO'
                            else:
                                raise SystemError('{} can\'t be parsed as permission')
                            _tmp_txt = ''
                            _step += 1
                            pass
                    pass
                else:
                    _tmp_txt += _ch
                    pass
            if _step == 3:
                self.__comments = _tmp_txt
            else:
                raise SystemError('line data({}) is invalid'.format(line))
            pass
        else:
            raise SystemError('line data type must be string')
        pass

    def __str__(self):
        _name = self.__name
        if isinstance(self.id, int):
            _name += '_{}'.format(self.id)
        if self.len > 1:
            _name += '[{}]'.format(self.len)
        _add = '0x{:0>8X}'.format(self.address[0])
        if isinstance(self.address[1], int):
            _add += ' ~ 0x{:0>8X}'.format(self.address[1])
            pass
        return '{} {} {}; /* {}: {} */'.format(self.permission, self.data_type, _name, _add, self.comments)
        pass
    pass


########################################################################################################################
script_version = "0.0.1"
########################################################################################################################


def main():
    import argparse
    import os as _os
    from jinja2 import Environment, FileSystemLoader
    _parser = argparse.ArgumentParser(description="REG map File Generation Tool v{}".format(script_version),
                                      formatter_class=argparse.RawTextHelpFormatter)

    _parser.add_argument('-O', '--output',
                         default='regmap.h',
                         type=str,
                         help="The reg map file path that will be outputted (default is regmap.h)")

    _parser.add_argument('-I', '--input',
                         type=str,
                         help="The reg map source file that needs to be imported")
    _args = _parser.parse_args()

    if (_args.output is None) or (_args.input is None):
        _parser.print_help()
        pass
    else:
        _items = []
        with open(_args.input, 'r') as rf:
            for _line in rf:
                _line = _line.strip()
                if _line != '':
                    _item = Item(_line)
                    _items.append(_item)
                    pass
                pass
            pass
        _items = sorted(_items, key=lambda _item: _item.address[0])
        _here = _os.path.abspath(_os.path.dirname(__file__))
        _env = Environment(loader=FileSystemLoader(_here),
                           trim_blocks=True,
                           lstrip_blocks=True)
        _reg_map_file = 'regmap.template'
        _reg_map_template = _env.get_template(_reg_map_file)
        _reg_map_result = _reg_map_template.render(filename=_args.output,
                                                   items=_items,
                                                   len=len(_items),
                                                   script_version=script_version)
        with open(_args.output, 'w') as f:
            f.write(_reg_map_result)
        pass
    pass


if __name__ == '__main__':
    main()
    pass
