from sweeper import sweep
import filecmp

#Test for some basic email examples
sweep("emails.txt")

if(filecmp.cmp("badEntries.txt", "Ebad.txt")):
	print("PASS")
else:
	print("FAIL")

