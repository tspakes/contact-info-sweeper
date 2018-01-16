from sweeper import sweep
import filecmp

# Calls function in sweeper.py with an input file of
# valid phone number entries
sweep("phoneNumbers.txt")
if(filecmp.cmp("badEntries.txt", "PNbad.txt")):
	print("PASS")
else:
	print("FAIL")
