from collections import OrderedDict
from jinja2 import Environment, FileSystemLoader
import ddclient.dgmanager
from ddclient.dgpayload import (E_DATAGRAM_ACTION_PUBLISH,
                                E_DATAGRAM_ACTION_RESPONSE,
                                E_DATAGRAM_ACTION_REQUEST,
                                E_DATAGRAM_ACTION_ALLOW)
import os as _os

SIMPLE_ACL_R = 0x00000001
SIMPLE_ACL_W = 0x00000002


class AclTestItem:
    __user_map = OrderedDict(
        (
            ('UC', 'UC'),
            ('SLC', 'SLC_UPS'),
            ('NMC', 'SLC_NMC'),
            ('HMI', 'HMI'),
            ('Tuner', 'Tuner')
        )
    )

    __permission_map = {
        'producer': {
            'Setting': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_W,
                E_DATAGRAM_ACTION_RESPONSE: SIMPLE_ACL_W,
                E_DATAGRAM_ACTION_REQUEST: SIMPLE_ACL_R,
                E_DATAGRAM_ACTION_ALLOW: SIMPLE_ACL_W
            },
            'Command': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_W,
                E_DATAGRAM_ACTION_RESPONSE: SIMPLE_ACL_R,
                E_DATAGRAM_ACTION_ALLOW: SIMPLE_ACL_R
            },
            'Status': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_W
            },
            'Measure': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_W
            },
            'General': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_W
            },
        },
        'consumer': {
            'Setting': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R,
                E_DATAGRAM_ACTION_RESPONSE: SIMPLE_ACL_R,
                E_DATAGRAM_ACTION_REQUEST: SIMPLE_ACL_W,
                E_DATAGRAM_ACTION_ALLOW: SIMPLE_ACL_R
            },
            'Command': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R,
                E_DATAGRAM_ACTION_RESPONSE: SIMPLE_ACL_W,
                E_DATAGRAM_ACTION_ALLOW: SIMPLE_ACL_W
            },
            'Status': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
            'Measure': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
            'General': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
        },
        'ro_consumer': {
            'Setting': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
            'Command': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
            'Status': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
            'Measure': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
            'General': {
                E_DATAGRAM_ACTION_PUBLISH: SIMPLE_ACL_R
            },
        }
    }

    def __init__(self, dg, dev_index, action, user, access):
        self.__topic = dg.get_device_data(dev_index).get_topic(action)
        self.__user = user
        self.__access = access
        self.__result = self.get_permission_result(dg.attribute, action)
        pass

    @property
    def topic(self):
        return self.__topic

    @property
    def user(self):
        return self.__user
        pass

    @property
    def access(self):
        return self.__access
        pass

    @property
    def result(self):
        return self.__result
        pass

    def get_permission_result(self, attr, action):
        _result = False
        _dd_user = self.__user_map[self.__user]
        _role = None
        if _dd_user in attr.producer:
            _role = 'producer'
            pass
        elif _dd_user in attr.consumer:
            if _dd_user in attr.no_setting_req_consumer:
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
                if (self.__permission_map[_role][attr.type][action] & self.__access) != 0:
                    _result = True
                    pass
            except KeyError:
                print('ERROR: [{},{},{},{}] parse access permission failed for 0x{:0>8X}({})'.format(
                    _dd_user, _role, attr.type, action, attr.hash_id, attr.name))
                pass
            pass
        return 'true' if _result is True else 'false'
        pass

    pass


########################################################################################################################
script_version = "0.0.1"
########################################################################################################################


def main(acl_file, dd_file):
    _dgm = ddclient.dgmanager.DatagramManager()
    _acl_test = []
    _users = (
        'UC',
        'SLC',
        'NMC',
        'HMI',
        'Tuner'
    )

    if _dgm.import_data_dictionary(dd_file):  # 'Full_Interface.CSV'):
        for _hash_id, _dev_index in _dgm.datagram_indexes:
            _dg = _dgm.get_datagram(_hash_id)
            for _user in _users:
                if _dg.attribute.type == 'Setting':
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH, _user, SIMPLE_ACL_W))

                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_RESPONSE, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_RESPONSE, _user, SIMPLE_ACL_W))

                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_REQUEST, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_REQUEST, _user, SIMPLE_ACL_W))

                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_ALLOW, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_ALLOW, _user, SIMPLE_ACL_W))
                    pass
                elif _dg.attribute.type == 'Command':
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH, _user, SIMPLE_ACL_W))

                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_RESPONSE, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_RESPONSE, _user, SIMPLE_ACL_W))

                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_ALLOW, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_ALLOW, _user, SIMPLE_ACL_W))
                    pass
                else:
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH, _user, SIMPLE_ACL_R))
                    _acl_test.append(AclTestItem(_dg, _dev_index, E_DATAGRAM_ACTION_PUBLISH, _user, SIMPLE_ACL_W))
                    pass
                pass
            pass
        pass
    _here = _os.path.abspath(_os.path.dirname(__file__))
    _env = Environment(loader=FileSystemLoader(_here),
                       trim_blocks=True,
                       lstrip_blocks=True)
    _acl_test_file_template_file = 'acltestfile.template'
    _acl_file = acl_file
    _acl_test_file_template = _env.get_template(_acl_test_file_template_file)
    data_dict_c_result = _acl_test_file_template.render(filename=_acl_file,
                                                        dgm=_dgm,
                                                        script_version=script_version,
                                                        acl_test=_acl_test, len=_acl_test.__len__())
    with open(_acl_file, 'w') as f:
        f.write(data_dict_c_result)
    pass


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="ACL Test File Generation Tool v{}".format(script_version),
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-O', '--output',
                        default='simple_acl_test.h',
                        type=str,
                        help="The ACL test file path that will be outputted (default is simple_acl_test.h)")

    parser.add_argument('-I', '--input',
                        default='Full_Interface.CSV',
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
