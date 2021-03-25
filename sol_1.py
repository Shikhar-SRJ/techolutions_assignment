import time
import paho.mqtt.client as mqtt
from datetime import datetime
import json

host = "broker.mqttdashboard.com"
port = 1883
keepalive = 60
topic = "IoTAssignment_srj"


def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')


def on_message(client, userdata, message):
    print(message.payload.decode("utf-8"))


data = {
    'now': str(datetime.utcnow().strftime("%y:%m:%d, %H:%M:%S")),
    'name': 'Shikhar'
}

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port, keepalive)

client.loop_start()
client.subscribe(topic, qos=0)
client.publish(topic, json.dumps(data))
time.sleep(2)
client.loop_stop()