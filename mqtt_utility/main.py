from paho.mqtt.client import Client as _Client
import base64
import hashlib
import time


def _on_message(mqttc, obj, msg):
    print('''Client: received
    |->timestamp    = {timestamp}
    |->qos          = {qos}
    |->retain       = {retain}
    |->topic        = {topic}
    |->payload      = {payload}'''.format(timestamp=msg.timestamp,
                                          qos=msg.qos,
                                          retain=msg.retain,
                                          topic=msg.topic,
                                          payload=msg.payload))
    pass


def _print_hash(data):
    print(', '.join('0x{:>02X}'.format(d) for d in data))
    pass


def _calculate_sn_base64(sn):
    data = sn.encode('utf-8')
    for i in range(5):
        hash_instance = hashlib.sha256()
        hash_instance.update(data)
        data = hash_instance.digest()
    return data
    pass


def _create_tuner_password(sn):
    base64_code = base64.b64encode(_calculate_sn_base64(sn))
    password = (sn + bytes.decode(base64_code, 'utf-8'))
    print('user: Tuner | password: {}'.format(password))
    return password
    pass


def main():
    i = 0
    instance = _Client("TestClient")
    instance.on_message = _on_message
    instance.tls_set(ca_certs='ca-ubuntu.crt')
    sn = 'SN12345678000000'
    base64_code = base64.b64encode(_calculate_sn_base64(sn))
    password = (sn + bytes.decode(base64_code, 'utf-8'))
    user = 'Tuner'
    instance.username_pw_set(username=user, password=password)
    instance.will_set(topic='Device/Tuner/Identity/Status/UnitPresentStatus', payload='123456')
    # instance.connect('169.254.5.1', 8883, 60)
    # instance.connect('10.177.58.98', 8883, 60)
    instance.connect('192.168.1.102', 8883, 10)
    instance.subscribe('Test', 0)
    instance.loop_start()

    while True:
        time.sleep(1)
        instance.publish(topic='Test', payload='I am a message [{}]!'.format(i))
        i += 1
        if i >= 5:
            # instance.socket().close()
            instance.loop_stop()
            instance.disconnect()
            print('======================')
            break
        pass
    while True:
        time.sleep(1)
        print('-----')
    pass


def main_no_cet():
    i = 0
    instance = _Client("TestClient")
    instance.on_message = _on_message
    # user = 'Simulator1'
    # password = '3279'
    user = 'NMC2'
    password = '2779'
    instance.username_pw_set(username=user, password=password)
    # instance.connect('192.168.23.3', 1883, 60)
    instance.connect('192.168.1.102', 1883, 60)
    instance.subscribe('Request/UPSSystem/Setting/MainsConfigurationSetting', 0)
    # instance.subscribe('Test', 0)
    instance.loop_start()

    while True:
        time.sleep(1)
        instance.publish(topic='Test', payload='I am a message [{}]!'.format(i))
        i += 1
    pass
    pass


if __name__ == '__main__':
    main()
    # main_no_cet()
    pass
