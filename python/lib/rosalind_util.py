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
	#print "read contents:\n" + file_contents
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


def parse_fasta(str):
	str = str.strip()
	db = dict()

	cur_id = None
	for line in str.splitlines():
		line = line.strip()
		if len(line) <= 0:
			next
		if line[0] == '>':
			cur_id = line[1:]
			db[cur_id] = ''
			continue

		db[cur_id] += line

	return db

def test_parse_fasta():
	input_str = """
	>Rosalind_6404
	CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
	TCCCACTAATAATTCTGAGG
	>Rosalind_5959
	CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
	ATATCCATTTGTCAGCAGACACGC
	>Rosalind_0808
	CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
	TGGGAACCTGCGGGCAGTAGGTGGAAT
	"""
	
	expected_db = {
		'Rosalind_6404': 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG',
		'Rosalind_5959': 'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC',
		'Rosalind_0808': 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT',
		}

	assert parse_fasta(input_str) == expected_db

def read_fasta_file(filename):
	return parse_fasta(read_file(filename))

