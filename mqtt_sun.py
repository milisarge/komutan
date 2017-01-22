#!/usr/bin/env python


import sys
import paho.mqtt.client as mqtt



def on_connect(mosq, obj, rc):
	print("rc: "+str(rc))

def on_message(mosq, obj, msg):
	print(msg.topic+" "+str(msg.payload))

def on_publish(mosq, obj, mid):
	print("mid: "+str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
	print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mosq, obj, level, string):
	print(string)


def main():
   
	mqttc = mqtt.Client()
	mqttc.on_message = on_message
	mqttc.on_connect = on_connect
	mqttc.on_publish = on_publish
	mqttc.on_subscribe = on_subscribe
	mqttc.connect("test.mosquitto.org", 1883, 60)
	mqttc.subscribe("milislinux/komutan", 0)
	mqttc.subscribe("milislinux/komutan/rehber", 0)

	rc = 0
	while rc == 0:
		rc = mqttc.loop()

	return 0

if __name__ == "__main__":
	sys.exit(main())
