import os
from OmegaExpansion import oledExp


class Oled(object):
	def __init__(this):
		oledExp.setVerbosity(-1)
		status  = oledExp.driverInit()
		if status != 0:
			print ('ERROR initializing OLED Expansion')
			
		oledExp.setTextColumns()
		oledExp.setCursor(0,1)
		oledExp.write('Moisture:')

	def updateMoisture(this,moisture):
		oledExp.setTextColumns()
		oledExp.setCursor(0,10)
		oledExp.write("" + str(moisture) + "  ")

	def updateState(this,state):
		oledExp.setTextColumns()
		oledExp.setCursor(0,14)
		if state == "idle":
			state = state + "   "
		oledExp.write(str(state) )
