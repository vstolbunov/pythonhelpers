def FindRE(pat,str):
	'''Simple function which uses the regular expression library
	to check for the existance of a pattern within a string'''

	import re

	match = re.search(pat,str)
	if match:
		return pat
	else:
		return None