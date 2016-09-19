import re

text = """Enter the text here. It will be shown as seperate sentences.
"""
sentences = re.split(r'((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s)', text)
for line in sentences:
	print line
