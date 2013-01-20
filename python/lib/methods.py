NUCLEOTIDES = ['A', 'C', 'G', 'T']


def nucleotide_counts(dna):
	"""count each kind of nucleotide, return the result as a dict """
	counts = {n: 0 for n in NUCLEOTIDES}
	for n in dna:
		counts[n] += 1
	return counts

def test_nucleotide_counts():
	sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
	counts = nucleotide_counts(sample)
	assert counts == dict(zip(NUCLEOTIDES, [20, 12, 17, 21]))



def rna_transcribe(dna):
	"""replace all T with U """
	rna = dna.replace('T', 'U')
	return rna

def test_dna_transcribe():
	sample = "GATGGAACTTGACTACGTAAATT"
	expected = "GAUGGAACUUGACUACGUAAAUU"
	assert rna_transcribe(sample) == expected



def reverse_complement(dna):
	"""returns the reversed complement of a dna string """
	from string import maketrans, translate
	comp = translate(dna, maketrans('CGAT', 'GCTA'))
	return comp[::-1]

def test_reverse_complement():
	sample = "AAAACCCGGT"
	expected = "ACCGGGTTTT"
	assert reverse_complement(sample) == expected


def gc_content(dna):
	count = 0
	for n in dna:
		if (n == 'G' or n == 'C'):
			count += 1
	return (float(count) / len(dna)) * 100

def test_gc_content():
	dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
	assert abs(gc_content(dna) - 60.92) < 0.01

