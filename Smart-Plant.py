#import serial, sys, os, getopt, time, signal, json

import os, serial, random
import oled_class as oled
import pump_class as pump
import losant_class as losant

dirname = os.path.dirname(os.path.abspath(__file__))


def init():
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
	return [oledflag, pumpflag, losantflag]

	serialPort = serial.Serial('/dev/ttyS1', 9600, timeout=2)
	if serialPort.isOpen() == False:
		print("ERROR: Failed to initialize serial port!")
		exit()










def measure():

	return random.randint(1,10)

def display(moisture):
	oled.update(moisture)
def sync(moisture):
	losant_class

def main():
	flags = init()
	
	if flags[0]:
		oled.init()
	if flags[1]:
		pump.init()
	if flags[2]:
		losant.init()



	while(True):
		moisture = measure()
		display(moisture)
		if flags[2]:
			sync(moisture)
		if moisture < -100:
			water()
		time.sleep(1)



if __name__ == "__main__":
	main()