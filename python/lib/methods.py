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

