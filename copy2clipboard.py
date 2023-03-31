import sys
import pyperclip

def convertPath(path):
	new = path.replace("\\", "//")
	return new

try:
	droppedFile = sys.argv[1]

	with open(convertPath(droppedFile), 'r') as file:
		text = file.readline()
			
	pyperclip.copy(text)
	
except IndexError:
	print("No file dropped")
