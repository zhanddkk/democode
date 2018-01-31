import hashlib
from collections import OrderedDict
from jinja2 import Environment, FileSystemLoader
import ddclient.dgmanager
from ddclient.dgpayload import (E_DATAGRAM_ACTION_PUBLISH,
                                E_DATAGRAM_ACTION_RESPONSE,
                                E_DATAGRAM_ACTION_REQUEST,
                                E_DATAGRAM_ACTION_ALLOW)
import os as _os


class AclItem:
    __user_map = OrderedDict(
        (
            ('UC', 'UC'),
            ('SLC_UPS', 'SLC'),
            ('SLC_NMC', 'NMC'),
            ('HMI', 'HMI'),
            ('Tuner', 'Tuner')
        )
    )
    __permission_map = {
        'producer': {
            'Setting': {
                E_DATAGRAM_ACTION_PUBLISH: 'w',
                E_DATAGRAM_ACTION_RESPONSE: 'w',
                E_DATAGRAM_ACTION_REQUEST: 'r',
                E_DATAGRAM_ACTION_ALLOW: 'w'
            },
            'Command': {
                E_DATAGRAM_ACTION_PUBLISH: 'w',
                E_DATAGRAM_ACTION_RESPONSE: 'r',
                E_DATAGRAM_ACTION_ALLOW: 'r'
            },
            'Status': {
                E_DATAGRAM_ACTION_PUBLISH: 'w',
            },
            'Measure': {
                E_DATAGRAM_ACTION_PUBLISH: 'w',
            },
            'General': {
                E_DATAGRAM_ACTION_PUBLISH: 'w',
            },
        },
        'consumer': {
            'Setting': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
                E_DATAGRAM_ACTION_RESPONSE: 'r',
                E_DATAGRAM_ACTION_REQUEST: 'w',
                E_DATAGRAM_ACTION_ALLOW: 'r'
            },
            'Command': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
                E_DATAGRAM_ACTION_RESPONSE: 'w',
                E_DATAGRAM_ACTION_ALLOW: 'w'
            },
            'Status': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
            },
            'Measure': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
            },
            'General': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
            },
        },
        'ro_consumer': {
            'Setting': {
                E_DATAGRAM_ACTION_PUBLISH: 'r'
            },
            'Command': {
                E_DATAGRAM_ACTION_PUBLISH: 'r'
            },
            'Status': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
            },
            'Measure': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
            },
            'General': {
                E_DATAGRAM_ACTION_PUBLISH: 'r',
            },
        }
    }

    def __init__(self, dg, dev_index, action):
        self.__permission = self.__get_access_permission(dg.attribute, action)
        self.__topic = dg.get_device_data(dev_index).get_topic(action)
        self.__hash = self.__get_hash(self.__topic)
        pass

    @property
    def hash(self):
        return self.__hash

    @property
    def topic(self):
        return self.__topic

    @property
    def permission(self):
        return self.__permission

    @staticmethod
    def __get_hash(topic):
        _sha1_data = hashlib.sha1(topic.encode()).digest()
        _index = len(_sha1_data)
        _hash = None
        if _index > 3:
            _hash = _sha1_data[_index - 4]
            _hash <<= 8
            _hash |= _sha1_data[_index - 3]
            _hash <<= 8
            _hash |= _sha1_data[_index - 2]
            _hash <<= 8
            _hash |= _sha1_data[_index - 1]
        return _hash
        pass

    def __get_access_permission(self, attr, action):
        _permission = ''
        for _key, _value in self.__user_map.items():
            _role = None
            if _key in attr.producer:
                _role = 'producer'
                pass
            elif _key in attr.consumer:
                if _key in attr.no_setting_req_consumer:
                    if action == E_DATAGRAM_ACTION_PUBLISH:
                        _role = 'ro_consumer'
                    pass
                else:
                    _role = 'consumer'
                    pass
                pass
            else:
                pass
            if _role is not None:
                try:
                    _permission += '{}|{},'.format(self.__user_map[_key],
                                                   self.__permission_map[_role][attr.type][action])
                    pass
                except KeyError:
                    print('ERROR: [{},{},{},{}] parse access permission failed for 0x{:0>8X}({})'.format(
                        _key, _role, attr.type, action, attr.hash_id, attr.name))
        pass
        return _permission.rstrip(',')
    pass


########################################################################################################################
script_version = "0.0.2"
########################################################################################################################


def main(acl_file, dd_file):
    _dgm = ddclient.dgmanager.DatagramManager()
    _acl = []
    if _dgm.import_data_dictionary(dd_file):  # 'Full_Interface.CSV'):
        for _hash_id, _dev_index in _dgm.datagram_indexes:
            _dg = _dgm.get_datagram(_hash_id)
            if _dg.attribute.type == 'Setting':
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH))
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_RESPONSE))
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_REQUEST))
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_ALLOW))
                pass
            elif _dg.attribute.type == 'Command':
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH))
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_RESPONSE))
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_ALLOW))
                pass
            else:
                _acl.append(AclItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH))
                pass
            pass
        pass
    _acl = sorted(_acl, key=lambda _item: _item.hash)
    _here = _os.path.abspath(_os.path.dirname(__file__))
    _env = Environment(loader=FileSystemLoader(_here),
                       trim_blocks=True,
                       lstrip_blocks=True)
    _acl_template_file = 'acltemplate.template'
    _acl_file = acl_file
    _acl_template = _env.get_template(_acl_template_file)
    data_dict_c_result = _acl_template.render(filename=_acl_file,
                                              dgm=_dgm,
                                              script_version=script_version,
                                              acl=_acl, len=_acl.__len__())
    with open(_acl_file, 'w') as f:
        f.write(data_dict_c_result)
    pass


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="ACL File Generation Tool v{}".format(script_version),
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-O', '--output',
                        default='simple_acl.cfg',
                        type=str,
                        help="The ACL file path that will be outputted (default is simple_acl.cfg)")

    parser.add_argument('-I', '--input',
                        type=str,
                        help="The data dictionary file that needs to be imported")
    args = parser.parse_args()
    if (args.output is None) or (args.input is None):
        parser.print_help()
        pass
    else:
        main(acl_file=args.output, dd_file=args.input)
        pass
    pass
