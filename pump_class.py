from OmegaExpansion import relayExp

RELAYADDR = 7
RELAYCHANNEL = 0

class Pump(object):
	def __init__(this, port=0):
		print("Pump loaded")
		this.port = port

		this.initialized = relayExp.checkInit(RELAYADDR)

		if not this.initialized:
			if relayExp.driverInit(RELAYADDR) != 0:
				print("ERROR: Could not initialize Relay Expansion!")

	def setState(this, state):
		if this.initialized:
			if state == "idle":
				print("set channel idle")
				relayExp.setChannel(RELAY_EXP_ADDR, RELAY_EXP_CHANNEL, 0)
			elif state == "pump":
				print("set channel pump")
				relayExp.setChannel(RELAY_EXP_ADDR, RELAY_EXP_CHANNEL, 1)
			else:
				print("INVALID PUMP STATE! Not pumping")
		else:
			print("Relay expansion not initialised!")