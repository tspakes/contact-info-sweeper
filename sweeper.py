def sweep(inputFileName):
	f = open(inputFileName, "r")
	outFile = open("badEntries.txt", "w")
	charCount = 1	
	invalidEntry = False
	phoneEntry = False
	emailEntry = False
	lastCharAt = False
	lastCharPeriod = False
	entry = ""
	currentChar = "-1"
	writtenTo = False
	
	while(True):
		currentChar = f.read(1)
		if(currentChar == ""):
			break
		cVal = ord(currentChar)
		#if(emailEntry == False and (cVal >= ord('a') and cVal <= ord('z')) or (cVal >= ord('A') and cVal <= ord('Z'))):
		#	emailEntry = True

		if(currentChar == '@'):
			emailEntry = True
		if(currentChar == " " or currentChar == "\n"):
			continue

		if(invalidEntry == False and phoneEntry == True and emailEntry == True):
			invalidEntry = True
		elif(invalidEntry == True and currentChar != ','):
			True
			#Do nothing, just continue the loop to print the bad entry
		elif(phoneEntry == False and charCount > 1 and currentChar == '@'):
			entry += currentChar
			charCount += 1
			lastCharAt = True
			emailEntry = True
			continue
		elif(emailEntry == True and lastCharAt == False and currentChar == '.'):
			entry += currentChar
			charCount += 1
			lastCharPeriod = True
			continue
		elif(currentChar == '.' and (emailEntry == False or lastCharAt == True or lastCharPeriod == True)):
			invalidEntry = True
		elif(emailEntry == False and (charCount == 4 or charCount == 8) and currentChar == '-'):
			phoneEntry = True
		elif(currentChar == ','):
			if(lastCharPeriod == True or lastCharAt == True):
				invalidEntry = True
			if(invalidEntry == True):
				if(writtenTo == True):
					outFile.write(", ")
				outFile.write(entry)
				writtenTo = True
			entry = "" #Setting up for next entry
			charCount = 1
			invalidEntry = False
			phoneEntry = False
			emailEntry = False
			lastCharAt = False
			lastCharPeriod = False
			continue #Begins a new entry
		elif((cVal < ord('A') or cVal > ord('Z')) and (cVal < ord('a') or cVal > ord('z')) and (cVal < ord('0') or cVal > ord('9'))):
			invalidEntry = True
		elif(phoneEntry == True and charCount == 13):
			invalidEntry = True #Phone numbers too long
		elif(emailEntry == False and phoneEntry == True and (cVal < ord('0') or cVal > ord('9'))):
			invalidEntry = True #Checking for letters in phone entry
		#else:
		#	print("invalid hereeee")
		#	invalidEntry = True
		entry += currentChar #Adding currentChar to the current entry
		charCount += 1
		if(lastCharAt == True):
			lastCharAt = False
		elif(lastCharPeriod == True):
			lastCharPeriod = False
	if(entry != "" and invalidEntry == True): #Writing last invalid entry
		if(writtenTo == True):
			outFile.write(", ")
		outFile.write(entry)

	f.close()	
	outFile.write("\n")
	outFile.close()
	return

sweep("emails.txt")
