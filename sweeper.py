def sweep(inputFileName):
	f = open(inputFileName, "r")
	outFile = open("badEntries.txt", "w")
	charCount = 1	
	invalidEntry = False
	entry = ""
	currentChar = "-1"
	writtenTo = False

	while(True):
		currentChar = f.read(1)
		if(currentChar == ""):
			break
		cVal = ord(currentChar)

		if(currentChar == " " or currentChar == "\n"):
			continue
		elif(charCount == 4 or charCount == 8):
			if(currentChar != "-"):
				invalidEntry = True
		#elif(cVal < ord('A') or cVal > ord('Z') and cVal < ord('a') or cVal > ord('z') and cVal < ord('0') or cVal > ord('9')):
		elif(currentChar == ','):
			if(invalidEntry == True):
				if(writtenTo == True):
					outFile.write(", ")
				outFile.write(entry)
				writtenTo = True
			entry = ""
			charCount = 1
			invalidEntry = False
			continue #Begins a new entry
		elif(charCount == 13):
			invalidEntry = True #Phone numbers too long
		elif(cVal < ord('0') or cVal > ord('9')):
			invalidEntry = True
		entry += currentChar #Adding currentChar to the current entry
		charCount += 1
	
	if(entry != "" and invalidEntry == True): #Writing last invalid entry
		if(writtenTo == True):
			outFile.write(", ")
		outFile.write(entry)

	f.close()	
	outFile.close()
	return

sweep("phoneNumbers.txt")
