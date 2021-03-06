#import serial, sys, os, getopt, time, signal, json

#Onion 1737

import os, serial, random, time
from oled_class import Oled
from pump_class import Pump
from losant_class import Losant

print("\n\n")
print("Welcome to the smart plant system developed by Harrison Grout\n")

PUMPTIME = 5
UPDATETIME = 1

#Input parsing to determine usage. Could be command line instead.

MANUALINPUTS = False
if MANUALINPUTS:
	print("Please follow the prompts to enable certain settings:")
	ans = input("\tIs there an OLED attached: (Y/N): ")
	if (ans == "Y") | (ans == "y"):
		print("\tOLED attached")
		oledflag = True
	elif (ans == "N") | (ans == "n"):
		print("\tNo OLED attached")
		oledflag = False
	else:
		print("\t!!!Invalid input, assuming no OLED!!!")
		oledflag = False

	ans = input("\tIs there a pump attached: (Y/N): ")
	if (ans == "Y") | (ans == "y"):
		print("\tPump attached")
		pumpflag = True
	elif (ans == "N") | (ans == "n"):
		print("\tNo pump attached")
		pumpflag = False
	else:
		print("\t!!!Invalid input, assuming no pump!!!")
		pumpflag = False

	ans = input("\tDo you want to connect Losant: (Y/N): ")
	if (ans == "Y") | (ans == "y"):
		print("\tLosant in use")
		losantflag = True
	elif (ans == "N") | (ans == "n"):
		print("\tLosant not in use")
		losantflag = False
	else:
		print("\t!!!Invalid input, ignoring Losant!!!")
		losantflag = False	
else:
	oledflag = True
	pumpflag = True
	losantflag = True

serialPort = serial.Serial('/dev/ttyS1', 9600, timeout=2)
if serialPort.isOpen() == False:
	print("ERROR: Failed to initialize serial port!")
	exit()

def measure():
	serialPort.write(str.encode('r'))
	try:
		moisture = serialPort.readline()

		if moisture == "":
			print("Got blank value!")
			moisture = None
		else:
			moisture = moisture.rstrip() 	#chomp the newline at the end of the response
	except:
		moisture = None

	return moisture

def oncommand(device, payload):
	if payload["name"] == "wateringState":
		print("Watering state is now: " + str(payload["payload"]) + "\n")
		global pumpState
		global pumpflag
		global startTime
		if (payload["payload"] == "start") and (pumpflag):
			startTime = time.time()
			print(startTime)
			pumpState = "pumping"
		elif (payload["payload"] == "stop") and (pumpflag):
			pumpState = "idle"
	else:
		print("Failure")

def display(moisture, pumpState = None):
	oled.updateMoisture(moisture)
	if pumpState:
		oled.updateState(pumpState)
def sync(moisture):
	losant_class

if oledflag:
	oled = Oled()
if pumpflag:
	pump = Pump()
	pumpState = "idle"
	startTime = 0
if losantflag:
	deviceid = "6114ba6dca38d0000666aed7"
	key = "fc736c44-ac77-497b-9bca-7eea26403226"
	secret = "d75e40850d15eba7695af4fcf7ba37983e64bfee2241140fc8450f32bca2a020"
	losant = Losant(deviceid, key, secret, oncommand)


while(True):
	moisture = int(measure())
	print("Moisture: " + str(moisture))
	if pumpflag and oledflag:
		if (pumpState == "pumping") and (int(time.time() - startTime) > PUMPTIME):
			pumpState = "idle"
		pump.setState(pumpState)
		display(moisture, pumpState)
	elif oledflag:
		display(moisture)
	if losantflag:
		losant.sendSingle(["Moisture", moisture])
	time.sleep(UPDATETIME)