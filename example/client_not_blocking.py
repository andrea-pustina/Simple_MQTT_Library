from Mqtt import Mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected")
    #subscribe here to topics

def on_disconnect(client, userdata, flags):
    print("Disconnected, should auto reconnect")

def on_message(client, userdata, paho_msg):
    msg = paho_msg.payload.decode("utf-8")
    print(msg)

mqtt = Mqtt('server_ip', 8885, 'client_Id')
mqtt.setAuthentication('user', 'pass')
mqtt.setSsl()
mqtt.connect()
mqtt.setOnConnectCallback(on_connect)
mqtt.setOnDisconnectCallback(on_disconnect)
mqtt.setOnMessageCallback(on_message)
mqtt.loopStart() #not blocking, client works in another thread (auto reconnect)

print("Here you can do your job")

