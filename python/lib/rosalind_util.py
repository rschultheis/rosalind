import sys

def read_file(filename):
	"""read the input file into a string"""
	print "opening input: " + filename
	try:
		fh = open(filename, 'r')
	except IOError as e:
		print ("{}".format(e))
		sys.exit()

	file_contents = fh.read().strip()
	fh.close()
	print "read contents:\n" + file_contents
	return file_contents

def write_file(file_contents, filename='output.txt'):
	"""write the output to a file"""
	try:
		fh = open(filename, 'w')
	except IOError as e:
		print ("{}".format(e))
		sys.exit()
	
	fh.write(file_contents)
	fh.write("\n")
	fh.close()
	print "wrote to: " + filename + "\n" + file_contents



