#import serial, sys, os, getopt, time, signal, json

#Onion 1737

import os, serial, random, time
import oled_class as oled
import pump_class as pump
from losant_class import Losant

print("\n\n")
print("Welcome to the smart plant system developed by Harrison Grout\n")
print("Please follow the prompts to enable certain settings:")


#Input parsing to determine usage. Could be command line instead.

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
	print("Command received:\n\n" + str(payload) + "\n\n")
	if payload["name"] == "wateringState":
		print("Watering state is now: " + str(payload["payload"]) + "\n")
	else:
		print("Failure")

def display(moisture):
	oled.update(moisture)
def sync(moisture):
	losant_class

def main():
	if oledflag:
		oled.init()
	if pumpflag:
		pump.init()
	if losantflag:
		deviceid = "6115def5ca38d0000666d32b"
		key = "336f5db1-749f-44f9-a052-a9a5308791bf"
		secret = "417176a8313232a7a512da728ef61e1a38a27b8cf1676ee0913a8932f3eac003"
		losant = Losant(deviceid, key, secret, oncommand)


	while(True):
		moisture = measure()
		print("Moisture: " + str(moisture), end='\r')
		display(moisture)
		if losantflag:
			losant.sendSingle(["Moisture", str(moisture)])
		time.sleep(1)



if __name__ == "__main__":
	main()