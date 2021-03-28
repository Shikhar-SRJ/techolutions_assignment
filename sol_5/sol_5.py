import machine
from mq135 import MQ135
from time import sleep

import ubinascii
from umqtt.simple import MQTTClient

# connecting sensor to analog pin 0
mq135 = MQ135(0)

# configuring mqtt
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
mqtt = MQTTClient(CLIENT_ID, 'broker.mqttdashboard.com')
mqtt.connect()


while True:
    try:
        # reading data from sensor
        co2_ppm = mq135.get_ppm()
        if co2_ppm > 1000:
            mqtt.publish('ppm/co2', str(co2_ppm))
        sleep(2)
    except KeyboardInterrupt:
        break

mqtt.disconnect()
