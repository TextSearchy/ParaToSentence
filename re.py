import re

text = """Enter the text here. It will be shown as seperate sentences.
"""
sentences = re.split(r'((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s)', text)
for line in sentences:
	if re.match(r'^\s*$',line):	##To skip blank lines from op
		continue		
	print line
