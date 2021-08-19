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
				relayExp.setChannel(RELAYADDR, RELAYCHANNEL, 0)
			elif state == "pumping":
				print("set channel pumping")
				relayExp.setChannel(RELAYADDR, RELAYCHANNEL, 1)
			else:
				print("INVALID PUMP STATE! Not pumping")
		else:
			print("Relay expansion not initialised!")