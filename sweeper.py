
def sweep(inputFileName):
	file = open(inputFileName, r)
	outFile = open(badEntries, w)
	charCount = 1	
	invalidEntry = False

	while(True):
		currentChar = read(1)
		if(currentChar == " " or currentChar == "\n"):
			continue
		elif(currentChar == 4 or currentChar == 8
		charCount += 1
	file.close()	
	outFile.close()
	return


