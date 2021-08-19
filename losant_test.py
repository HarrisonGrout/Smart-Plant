from losant_class import Losant
import time

laptopid = "6115def5ca38d0000666d32b"
key = "336f5db1-749f-44f9-a052-a9a5308791bf"
secret = "417176a8313232a7a512da728ef61e1a38a27b8cf1676ee0913a8932f3eac003"
#key = "4572b0f0-a1c4-4688-8b19-5e5e36b7bd2e"
#secret = "f2d57cb73a542a1652a9824e9cdec7237a9b0bd4c1b873d1d199a63a64f64ced"
#key = "464a9e74-a38e-47b2-b4cd-96a186e4abaa"
#secret = "36b7d1836d49dd83dad9a2760f5212fb031ba3ed7449d0ac33410b6bbf1ef5c4"

def oncommand(device, payload):
	print("Command received:\n\n" + str(payload) + "\n\n")
	if payload["name"] == "changeFactor":
		print("Change factor to " + str(payload["payload"]) + "\n")
		global factor 
		factor = int(payload["payload"])
	else:
		print("Failure")
	

losant = Losant(laptopid, key, secret, oncommand)

i = 0

while(not losant.device.is_connected()):
	print("Not connected, sleeping")
	time.sleep(1)
	losant.device.loop()

factor = 5

for i in range(100):
	val = i * factor
	losant.sendSingle(["Value", val])
	print("Sent " + str(val) + " current factor is: " + str(factor))
	time.sleep(1)


