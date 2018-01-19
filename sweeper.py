
def sweep(inputFileName):
	f = open(inputFileName, "r")
	outFile = open("badEntries.txt", "w")
	charCount = 1	
	invalidEntry = False
	letter = False
	at = False # tracks if
	period = False
	dash = False
	lastCharAt = False
	lastCharPeriod = False
	entry = ""
	currentChar = "Unset"
	writtenTo = False
	
	while(True):
		currentChar = f.read(1)
		if(currentChar == ""): #Reached end of file
			break
		cVal = ord(currentChar)

		if(currentChar == ','): #Marks the end of the current entry
			if(lastCharPeriod == True or lastCharAt == True or (at == False and dash == False) or (period == False and dash == False)):
				invalidEntry = True
			elif((dash == True and charCount != 13) or charCount < 6):
				invalidEntry = True
			if(invalidEntry == True):
				if(writtenTo == True):
					outFile.write(", ")
				outFile.write(entry)
				writtenTo = True
			entry = "" #Setting up for next entry
			charCount = 1
			invalidEntry = False
			letter = False
			at = False
			period = False
			dash = False
			continue #Begins a new entry
		elif(invalidEntry == True):
			True #Do nothing, just cotinue the loop
		elif(currentChar == '@'):
			if(letter == False or at == True or period == True or dash == True):
				invalidEntry = True
			at = True
		elif(currentChar == ' ' or currentChar == '\n'):
			continue
		elif(currentChar == '-'):
			if(letter == True or at == True or period == True or (charCount != 4 and charCount != 8)):
				invalidEntry = True
			dash = True
		elif(currentChar == '.'):
			if(dash == True or period == True or at == False):
				invalidEntry = True
			period = True			
		elif((cVal >= ord('A') and cVal <= ord('Z')) or (cVal >= ord('a') and cVal <= ord('z'))):
			if(dash == True):
				invalidEntry = False
			letter = True
		elif(cVal >= ord('0') and cVal <= ord('9')):
			if(dash == True and letter == True): #Not necessary, but extra precaution
				invalidEntry = True

		entry += currentChar #Adding currentChar to the current entry
		charCount += 1
	if(entry != "" and invalidEntry == True): #Writing last invalid entry
		if(writtenTo == True):
			outFile.write(", ")
		outFile.write(entry)

	f.close()	
	#outFile.write("\n")
	outFile.close()
	return

sweep("phoneNumbersInvalid.txt")
