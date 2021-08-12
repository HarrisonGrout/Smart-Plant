import serial, sys, os, getopt, time, signal, json

dirName = os.path.dirname(os.path.abspath(__file__))

print("Welcome to the smart plant system developed by Harrison Grout\n")
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

