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
	oledExp.write('Moisture: ')

	oledExp.setCursor(1,0)
	oledExp.write("___________________________________________________________")