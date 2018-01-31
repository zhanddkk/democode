
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
        return '{} {} {}; /* {}: {} */'.format(self.permission, self.data_type, _name, _add, self.__comments)
        pass
    pass


class StructureData:
    def __init__(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise SystemError('structure name must be string type')
        self.__items = {}
        self.__base_address = None
        pass

    @property
    def name(self):
        return self.__name
        pass

    @property
    def base_address(self):
        if self.__base_address is None:
            self.__base_address = self.members[0].address[0]
        return self.__base_address

    @property
    def members(self):
        _items_list = []
        for _item in self.__items.values():
            if isinstance(_item, list):
                for _sub_item in _item:
                    _items_list.append(_sub_item)
                    pass
                pass
            else:
                _items_list.append(_item)
        _items_list = sorted(_items_list, key=lambda _item: _item.address[0])
        self.__items_check(_items_list)
        return _items_list
        pass

    def add_item(self, item):
        if isinstance(item, Item):
            if item.name in self.__items:
                _item_tmp = self.__items[item.name]
                if isinstance(_item_tmp, list):
                    item.id = len(_item_tmp)
                    _item_tmp.append(item)
                    pass
                elif isinstance(_item_tmp, Item):
                    _item_tmp.id = 0
                    item.id = 1
                    self.__items[item.name] = [_item_tmp, item]
                else:
                    raise SystemError('system error for tool(item:{} is invalid)'.format(self.__items[item.name]))
                pass
            else:
                self.__items[item.name] = item
            self.__base_address = None
        else:
            raise SystemError('system error for tool(item:{} type is invalid)'.format(item))
        pass

    @staticmethod
    def __items_check(items):
        if isinstance(items, list):
            _last_address = None
            for _item in items:
                if _last_address is None:
                    if _item.address[1] is None:
                        _last_address = _item.address[0]
                        pass
                    else:
                        _last_address = _item.address[1]
                        pass
                    pass
                else:
                    _align_size = _item.address[0] - _last_address
                    if _item.address[1] is None:
                        _last_address = _item.address[0]
                        pass
                    else:
                        _last_address = _item.address[1]
                        pass

                    if _align_size != 4:
                        raise SystemError('address error for item: {}'.format(_item))
                    pass
                pass
            pass
        pass

    def __str__(self):
        return '{}: {} members'.format(self.__name, len(self.__items))
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
        _step = 0
        _structures = []
        _structure = None
        with open(_args.input, 'r') as rf:
            for _line in rf:
                _line = _line.strip()
                if _line != '':
                    if _step == 0:
                        if _line.startswith('['):
                            _structure = StructureData(_line[1:])
                            _step = 1
                            pass
                        pass
                    elif _step == 1:
                        if _line.endswith(']'):
                            _structures.append(_structure)
                            _structure = None
                            _step = 0
                            pass
                        else:
                            _item = Item(_line)
                            if isinstance(_structure, StructureData):
                                _structure.add_item(_item)
                            else:
                                raise SystemError('system error for tool(structure data is not init)')
                            pass
                        pass
                    else:
                        raise SystemError('system error for tool(invalid step)')
            pass
        _structures = sorted(_structures, key=lambda _structure: _structure.base_address)
        _here = _os.path.abspath(_os.path.dirname(__file__))
        _env = Environment(loader=FileSystemLoader(_here),
                           trim_blocks=True,
                           lstrip_blocks=True)
        _reg_map_file = 'regmap.template'
        _reg_map_template = _env.get_template(_reg_map_file)
        _reg_map_result = _reg_map_template.render(filename=_args.output,
                                                   structures=_structures,
                                                   isinstance=isinstance,
                                                   list=list,
                                                   len=len(_structures),
                                                   script_version=script_version)
        with open(_args.output, 'w') as f:
            f.write(_reg_map_result)
        pass
    pass


if __name__ == '__main__':
    main()
    pass
