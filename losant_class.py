import time
from losantmqtt import Device

print("Losant loaded")

class Losant(object):
	def on_command(this, device, command):
	    print("Command received.")
	    print(command["name"])
	    print(command["payload"])

	def __init__(this, name, key, secret, commandSorter=None):
		this.device = Device(name, key, secret)
		this.device.connect(blocking=False)
		if commandSorter:
			print("Adding command with key: " + str(commandSorter))
			this.device.add_event_observer("command", commandSorter)

	def send(this, dataset):
		this.device.loop()
		if this.device.is_connected():
			for data in dataset:
				this.device.send_state({data[0]:data[1]})
		else:
			print("Not connected")

	def sendSingle(this, data):
		this.device.loop()
		if this.device.is_connected():
			this.device.send_state({data[0]:data[1]})
		else:
			print("Not connected")

	def connected(this):
		return this.device.is_connected()
