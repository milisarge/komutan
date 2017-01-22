#!/usr/bin/env python


import sys
import paho.mqtt.client as mqtt
import datetime
import os


def on_connect(mosq, obj, rc):
	print("bag-s: "+str(rc))

def on_message(mosq, obj, msg):
	print(msg.topic+" "+str(msg.payload))
	zmn=str(datetime.datetime.now())
	open("log/mqtt.log","a").write(zmn+"@"+msg.topic+"@"+str(msg.payload)+"<p>")

def on_publish(mosq, obj, mid):
	print("mid: "+str(mid))
	
def on_subscribe(mosq, obj, mid, granted_qos):
	print("abonelik-s: "+str(mid)+" "+str(granted_qos))

def on_log(mosq, obj, level, string):
	print(string)


def main():
	if os.path.isfile("uuid"): 
		kimlik=open("uuid","r").read()
	else:
		kimlik= uuid.uuid4()
		kimlik=str(kimlik)
		open("uuid","w").write(kimlik)
	mqttc = mqtt.Client()
	mqttc.on_message = on_message
	mqttc.on_connect = on_connect
	mqttc.on_publish = on_publish
	mqttc.on_subscribe = on_subscribe
	mqttc.connect("test.mosquitto.org", 1883, 60)
	mqttc.subscribe("milislinux/komutan", 0)
	mqttc.subscribe("milislinux/komutan/rehber", 0)
	open("log/mqtt.log","a").write("")
	mqttc.publish('milislinux/komutan', kimlik+' komutan sunucu aktif.')
	rc = 0
	while rc == 0:
		rc = mqttc.loop()

	return 0

if __name__ == "__main__":
	sys.exit(main())
