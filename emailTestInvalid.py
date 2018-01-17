from sweeper import sweep
import filecmp

#Test for some basic email examples
sweep("emails2.txt")

if(filecmp.cmp("badEntries.txt", "E2bad.txt")):
	print("PASS")
else:
	print("FAIL")

