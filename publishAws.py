#publish Meters aws
# importing libraries
import paho.mqtt.client as paho
import os
import socket
import ssl
import random
import string
import json
from time import sleep

from GetTempAndHumidity import createData_func as createData
from GetTempAndHumidity import getTemp_func as getTemp
from GetTempAndHumidity import getHumidity_func as getHumidity
 
connflag = False
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#AWS Parameters to connect to DynamoDB
awshost = "a1mpej6j9a40jf-ats.iot.eu-west-2.amazonaws.com"      # Endpoint
awsport = 8883                                             
clientId = "MeterProject_Client"                                   
thingName = "MeterProject_Client"                                   
caPath = "/home/pi/Documents/AWS/AmazonRootCA1.pem"                                      # Root_CA_Certificate_Name
certPath = "/home/pi/Documents/AWS/ccacb7f17c-certificate.pem.crt"                            # <Thing_Name>.cert.pem
keyPath = "/home/pi/Documents/AWS/ccacb7f17c-private.pem.key"                          # <Thing_Name>.private.key
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_start()                                          # Start the loop
 
while 1==1:
    sleep(60)
    if connflag == True:
        setTemp = getTemp()
        setHumidity = getHumidity()
        paylodmsg0="{"
        paylodmsg1 = "\"assetId\": \""
        paylodmsg2 = "\", \"temperature\":"
        paylodmsg3 = ", \"humidity\": \""
        paylodmsg4="\"}"
        paylodmsg = "{} {} {} {} {} {} {} {}".format(paylodmsg0, paylodmsg1, "RP001", paylodmsg2, setTemp , paylodmsg3, setHumidity, paylodmsg4)
        paylodmsg = json.dumps(paylodmsg) 
        paylodmsg_json = json.loads(paylodmsg)       
        mqttc.publish("MeterReadings", paylodmsg_json , qos=1)        # topic: temperature # Publishing Temperature values
        print("msg sent: MeterReadings" ) # Print sent temperature msg on console
        print(paylodmsg_json)

    else:
        print("waiting for connection...")
        