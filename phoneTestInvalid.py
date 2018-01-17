from sweeper import sweep
import filecmp

#Tests sweeper.py using a file with some bad phone
#numbers and some good phone numbers
sweep("phoneNumbersInvalid.txt")
if(filecmp.cmp("badEntries.txt", "PN2bad.txt")):
	print("PASS")
else:
	print("FAIL")

