import re
import sys

filepath=str(sys.argv[1])
with open(filepath, 'r') as ifile:
	s=ifile.read()
sentences = re.split(r'((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s)', s)
for line in sentences:
	if re.match(r'^\s*$',line):	##To skip blank lines from op.
		continue		
	print line
