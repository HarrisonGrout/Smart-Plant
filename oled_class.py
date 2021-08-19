import os
from OmegaExpansion import oledExp

def init():
	oledExp.setVerbosity(-1)
	status  = oledExp.driverInit()
	if status != 0:
		print ('ERROR initializing OLED Expansion')

	## write the default text
	# write the first word on the second line and the right side of the screen
	oledExp.setTextColumns()
	oledExp.setCursor(0,1)
	oledExp.write('Moisture:')

def updateMoisture(moisture):
	oledExp.setTextColumns()
	oledExp.setCursor(0,11)
	oledExp.write("" + str(moisture) + "  ")

def updateState(state):
	oledExp.setTextColumns()
	oledExp.setCursor(0,15)
	oledExp.write(str(state))