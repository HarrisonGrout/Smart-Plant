from OmegaExpansion import relayExp

RELAYADDR = 7
RELAYCHANNEL = 0

class Pump(object):
	def __init__(this, port=0):
		print("Pump loaded")
		this.port = port

		this.initialized = relayExp.checkInit(RELAYADDR)

		if not initialized:
			if relayExp.driverInit(RELAYADDR) != 0:
				print("ERROR: Could not initialize Relay Expansion!")

	def setState(this, state):
		if initialized:
			if state == "idle":
				relayExp.setChannel(RELAY_EXP_ADDR, RELAY_EXP_CHANNEL, 0)
			elif state == "pump":
				relayExp.setChannel(RELAY_EXP_ADDR, RELAY_EXP_CHANNEL, 1)
			else:
				print("INVALID PUMP STATE! Not pumping")
		else:
			print("Relay expansion not initialised!")