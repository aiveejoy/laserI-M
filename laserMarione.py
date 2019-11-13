import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

LedPin = 18    # pin11

# def setup():
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():	
	print '...led on'
	GPIO.output(LedPin, GPIO.HIGH)  # led on

def destroy():
	print '...led off'
	GPIO.output(LedPin, GPIO.LOW)     # led off
	                   # Release resource

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("x")
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

	if(msg.payload=="1"):
 		loop()
		print(msg.topic+" "+str(msg.payload))
	else:
		destroy()
    	print(msg.topic+" "+str(msg.payload))


#def on_message("message", function (topic, payload) {
       # print("recieved:\ntopic: " + topic + "\npayload: " + payload);
 # })

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
