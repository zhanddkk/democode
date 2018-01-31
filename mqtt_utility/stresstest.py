from paho.mqtt.client import Client as _Client
import base64
import hashlib
import time


class TestClient:

    def __init__(self):
        self.__test_topic = 'AllowedRequest/Device/NMC1/Identity/Setting/ModelNumber{}'.format('{}'.format(time.time()).replace('.', '_'))
        # self.__test_topic = 'Device/SLC/Identity/General/Heartbeat'
        # self.__tuner_instance = _Client("TestClientTuner")
        self.__tuner_instance = _Client()
        self.__tuner_instance.on_message = self.__on_message
        # instance.on_message = _on_message
        # self.__tuner_instance.tls_set(ca_certs='ca-ubuntu.crt')
        sn = 'SN12345678000000'
        base64_code = base64.b64encode(self.__calculate_sn_base64(sn))
        password = (sn + bytes.decode(base64_code, 'utf-8'))
        user = 'Tuner'
        print(password)

        # user = 'SLC'
        # password = '8aef'
        self.__tuner_instance.username_pw_set(username=user, password=password)
        self.__tuner_instance.connect('192.168.1.101', 1883, 60)
        # self.__tuner_instance.subscribe(self.__test_topic, 0)
        self.__tuner_instance.loop_start()

        # self.__hmi_instance = _Client("TestClientHmi")
        self.__hmi_instance = _Client()
        self.__hmi_instance.on_message = self.__on_message
        # user = 'HMI'
        # password = '3c9d'
        user = 'UC'
        password = 'bd15'
        self.__hmi_instance.username_pw_set(username=user, password=password)
        # instance.connect('192.168.23.3', 1883, 60)
        self.__hmi_instance.connect('192.168.1.101', 1883, 60)
        self.__hmi_instance.subscribe(self.__test_topic, 0)
        self.__hmi_instance.loop_start()

        self.__send_count = 0
        self.__received_count = 0
        pass

    @staticmethod
    def __calculate_sn_base64(sn):
        data = sn.encode('utf-8')
        for i in range(5):
            hash_instance = hashlib.sha256()
            hash_instance.update(data)
            data = hash_instance.digest()
        return data
        pass

    def __on_message(self, mqttc, obj, msg):
        # print('''Client: received
        # |->timestamp    = {timestamp}
        # |->qos          = {qos}
        # |->retain       = {retain}
        # |->topic        = {topic}
        # |->payload      = {payload}'''.format(timestamp=msg.timestamp,
        #                                       qos=msg.qos,
        #                                       retain=msg.retain,
        #                                       topic=msg.topic,
        #                                       payload=msg.payload))
        _time = time.time()
        self.__received_count += 1
        _last_count = int(msg.payload.decode())
        if _last_count % 1000 == 0:
            print('{} = {} [{}]'.format(_last_count, self.__received_count, _time))
        # print('{}, {}, {}'.format(_last_time, _time, _time - _last_time))
        pass

    def __on_publish(self, mqttc, obj, mid):
        pass

    def start(self):
        while True:
            self.__send_count += 1
            _info = self.__tuner_instance.publish(topic=self.__test_topic, payload='{}'.format(self.__send_count), retain=1, qos=1)
            _info.wait_for_publish()

            if self.__send_count >= 500000:
                print('Stopped')
                while self.__send_count != 0:
                    time.sleep(1)
                break
            pass
        pass
    pass


if __name__ == '__main__':
    tc = TestClient()
    tc.start()
    pass
