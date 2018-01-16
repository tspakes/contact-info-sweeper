from sweeper import sweep
import filecmp

#tests phone numbers that are too long
sweep("phoneNumbersLong.txt")

if(filecmp.cmp("badEntries.txt", "PN3bad.txt")):
	print("PASS")
else:
	print("FAIL")
