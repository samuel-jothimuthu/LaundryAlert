#!/usr/bin/python
from AWSIoTPythonSDK.MQTTLib import AWSIotMQTTClient
from datetime import date, datetime
import RPi.GPIO as GPIO
import time
MD = "Movement Detected!"

#AWS stuff
myMQTTClient = AWSIotMQTTClient("new_Client")
myMQTTClient.configureEndpoint("a1hgclva7dx6v0-ats.iot.us-west-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/Desktop/AmazonRootCA1.pem",
                                  "/home/pi/Desktop/f6db1ce402-private.pem.key",
                                  "/home/pi/Desktop/f6db1ce402-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1) #Infinte offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) #Draining: 2Hz
myMQTTClient.configureConnectDisconnectTimeout(10) #10 sec
myMQTTClient.configureMQTTOperationTimeout(5) #5 sec

#Connecting
connecting_time = time.time() + 10
if time.time() < connecting_time: #10 second connect to AWS
        myMQTTClient.connect()
        myMQTTClient.publish("Vibe/info","connected",0)
        print("MQTT Client connection success!")
else:
        print("Error: Failed to connect")

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print(MD)
                myMQTTClient.publish("Vibe/data",MD,0)
        else:
                print(MD)
                myMQTTClient.publish("Vibe/data", MD, 0)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)