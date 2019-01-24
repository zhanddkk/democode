import os as _os
import subprocess

_here = _os.path.abspath(_os.path.dirname(__file__))
_os.chdir(_here)
_build_output = '{}/output'.format(_here)


def install_folder(src, des_root):
    for root, dirs, files in _os.walk(src):
        _des_path = '{}/{}'.format(des_root, root)
        subprocess.call(['install', '-d', _des_path])
        for name in files:
            subprocess.call(
                ['install',
                 '{root}/{name}'.format(root=root, name=name),
                 '{des_path}/{name}'.format(root=root, name=name, des_path=_des_path)])
            pass
    pass


def check_dep_packages(packages):
    _is_all_package_prepared = True
    _output_log = ''
    if isinstance(packages, (list, tuple)):
        for pkg in packages:
            if subprocess.call(['dpkg', '-s', pkg]) != 0:
                _is_all_package_prepared = False
                _output_log += 'ERROR: {} is not found\n'.format(pkg)
        if _is_all_package_prepared is False:
            print(_output_log)
    return _is_all_package_prepared
    pass


def build_lib_mosquitto():
    _dep_packages = (
        # 'libc-ares2-dev',
        'uuid-dev',
        'libssl-dev',
        'docbook-xsl',
        'xsltproc'
    )

    _project_dir = 'secure_power_agilis_lib_mosquitto'
    if check_dep_packages(_dep_packages):
        subprocess.call(
            ['git', 'clone', 'ssh://teamforge.schneider-electric.com:29418/{}'.format(_project_dir)])
        _os.chdir('secure_power_agilis_lib_mosquitto')
        subprocess.call(['git', 'checkout', 'Dev'])
        subprocess.call(['make', 'install', 'DESTDIR={}'.format(_build_output)])
        _os.chdir(_here)
        subprocess.call(['rm', '-rf', _project_dir])
    pass


def build_lib_modbus():
    _dep_packages = (
        'autoconf',
        'automake',
        'libtool'
    )
    _project_dir = 'secure_power_agilis_lib_modbus'

    if check_dep_packages(_dep_packages):
        subprocess.call(
            ['git', 'clone', 'ssh://teamforge.schneider-electric.com:29418/{}'.format(_project_dir)])
        _os.chdir(_project_dir)
        subprocess.call(['git', 'checkout', 'Dev'])
        subprocess.call(['./configure', '--prefix={}/usr/local'.format(_build_output)])
        subprocess.call(['make', 'install'])
        _os.chdir(_here)
        subprocess.call(['rm', '-rf', _project_dir])
    pass


def build_cn_cbor():
    _dep_packages = (
        'cmake',
        'doxygen'
    )
    _project_dir = 'secure_power_agilis_modules_cn_cbor'

    if check_dep_packages(_dep_packages):
        subprocess.call(
            ['git', 'clone', 'ssh://teamforge.schneider-electric.com:29418/{}'.format(_project_dir)])

        _os.chdir(_project_dir)
        subprocess.call(['git', 'checkout', 'Dev'])
        # subprocess.call(['git', 'checkout', '-B', 'build', '588fb41c1b0e6dc7cb27b74a0e29cf5bbcf2c994'])
        if _os.path.exists('build'):
            pass
        else:
            subprocess.call(['mkdir', 'build'])
        _os.chdir('build')
        subprocess.call(['cmake',
                         '-DCMAKE_BUILD_TYPE=Release',
                         '-Dcoveralls=OFF',
                         '-DCMAKE_INSTALL_PREFIX={}/usr/local'.format(_build_output), '..'])
        subprocess.call(['make', 'doc', 'install'])
        _os.chdir(_here)
        subprocess.call(['rm', '-rf', _project_dir])
    pass


def build_google_gmock():
    _project_dir = 'googletest'
    subprocess.call(
        ['git', 'clone', 'https://github.com/google/{}.git/'.format(_project_dir)])
    _os.chdir(_project_dir)
    subprocess.call(['git', 'checkout', 'release-1.8.0', '-b', 'Dev'])
    _os.chdir('googlemock/make')
    subprocess.call(['make', 'all'])
    subprocess.call(['install', '-d', '{}/usr/local/lib'.format(_build_output)])
    subprocess.call(['install', '-d', '{}/usr/local/include/'.format(_build_output)])
    subprocess.call(['install',
                     'gmock_main.a',
                     '{}/usr/local/lib/libgmock_main.a'.format(_build_output)])
    _os.chdir('../')
    install_folder('include', '{}/usr/local'.format(_build_output))
    _os.chdir('../googletest/')
    install_folder('include', '{}/usr/local'.format(_build_output))
    _os.chdir(_here)
    subprocess.call(['rm', '-rf', _project_dir])
    pass


def build_berkeley_db():
    _project_dir = 'secure_power_agilis_lib_berkeley_db'
    subprocess.call(
        ['git', 'clone', 'ssh://teamforge.schneider-electric.com:29418/{}'.format(_project_dir)])
    _os.chdir(_project_dir)
    subprocess.call(['git', 'checkout', 'Dev'])
    _os.chdir('build_unix')
    subprocess.call(['../dist/configure', '--prefix={}/usr/local'.format(_build_output)])
    subprocess.call(['make', 'install'])
    _os.chdir(_here)
    subprocess.call(['rm', '-rf', _project_dir])
    pass


def build_libusb():
    _dep_packages = (
        'autoconf',
        # 'automake',
        'libtool'
    )
    _project_dir = 'libusb'

    if check_dep_packages(_dep_packages):
        subprocess.call(
            ['git', 'clone', 'https://github.com/libusb/{}.git'.format(_project_dir)])
        _os.chdir(_project_dir)
        subprocess.call(['git', 'checkout', 'v1.0.21'])
        subprocess.call(['./autogen.sh', '--disable-udev', '--prefix={}/usr/local'.format(_build_output)])
        subprocess.call(['make', 'install'])
        _os.chdir(_here)
        subprocess.call(['rm', '-rf', _project_dir])
    pass


def build_tinycbor():
    _project_dir = 'secure_power_agilis_modules_tiny_cbor'
    subprocess.call(
        ['git', 'clone', 'ssh://teamforge.schneider-electric.com:29418/{}'.format(_project_dir)])
    _os.chdir(_project_dir)
    subprocess.call(['git', 'checkout', 'Dev'])
    # _os.chdir('build_unix')
    subprocess.call(['make', 'all', 'funopen-pass=1'])
    subprocess.call(['make', 'install', 'prefix={}/usr/local'.format(_build_output)])
    _os.chdir(_here)
    subprocess.call(['rm', '-rf', _project_dir])
    pass


def main():
    # build_lib_mosquitto()
    build_lib_modbus()
    # build_cn_cbor()
    # build_google_gmock()
    # build_berkeley_db()
    # build_libusb()
    # build_tinycbor()
    pass


if __name__ == '__main__':
    main()
    # import datetime
    # print(datetime.datetime.now())
    # with open('text.txt', '+a') as _f:
    #     _f.write(('[{}]===\r\n'.format(datetime.datetime.now())))
    #     pass
    pass
