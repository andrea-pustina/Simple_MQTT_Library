import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ssl


class Mqtt:
    def __init__(self, host, port, clientId):
        self.client = mqtt.Client(clientId, clean_session=True, protocol=mqtt.MQTTv311, transport="tcp")
        self.host = host
        self.port = port
        self.client_id = clientId

    def setSsl(self):
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE
        self.client.tls_set_context(ssl_ctx)
        self.client.tls_insecure_set(True)  # This is probably redundant with ssl_ctx.check_hostname = False

    def setAuthentication(self, user, psw):
        self.auth = {
            'username': user,
            'password': psw
        }
        self.client.username_pw_set(user, psw)

    def setOnConnectCallback(self, onConnectCb):
        self.client.on_connect = onConnectCb

    def setOnDisconnectCallback(self, onDisconnectCb):
        self.client.on_disconnect = onDisconnectCb

    def setOnMessageCallback(self, onMessageCb):
        self.client.on_message = onMessageCb

    def connect(self):
        self.client.connect(self.host, self.port, keepalive=60)

    def disconnect(self):
        self.client.disconnect()

    def loopStart(self):                 #not blocking, creates a new tread so has to be called once, auto reconnect
        self.client.loop_start()

    def loopForever(self):               #blocking, auto reconnect
        self.client.loop_forever()

    def publish(self, topic, msg, retain=False, qos=0):
        self.client.publish(topic, payload=msg, qos=qos, retain=retain)

    def single_publish(self, topic, msg, retain=False, qos=0):
        self.connect()
        self.client.publish(topic, payload=msg, qos=qos, retain=retain)
        self.disconnect()

    def subscribe(self, topic, qos=0):
        self.client.subscribe(topic, qos)