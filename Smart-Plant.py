#import serial, sys, os, getopt, time, signal, json

import os

dirName = os.path.dirname(os.path.abspath(__file__))


def init():
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

		# elif opt in ("-l", "--losant"):
		# 	import losantHelper
		# 	LOSANT_CLOUD = True
		# 	filepath = '/'.join([dirName, arg])
		# 	if os.path.abspath(arg):
		# 		filepath = arg
		# 	with open( filepath ) as f:
		# 		try:
		# 			losantConfig = json.load(f)
		# 		except:
		# 			print("ERROR: expecting JSON file")
		# 			sys.exit()
		# 		if not losantHelper.isConfigValid(losantConfig):
		# 			sys.exit()



	elif (ans == "N") | (ans == "n"):
		print("\tLosant not in use")
		losantflag = False
	else:
		print("\t!!!Invalid input, ignoring Losant!!!")
		losantflag = False	













def main():
	init()



if __name__ == "__main__":
	main()