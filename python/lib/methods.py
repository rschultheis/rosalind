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



def substring_positions(dna, sub):
	from re import finditer
	expr = '(?=' + sub + ')' #this expr uses lookahead to account for overlappying
	l = [m.start() + 1 for m in finditer(expr, dna)]
	return l

def test_substring_positions():
	dna = "AATTCACCTGCTCCCTGCTCCCTGCTCCCTCCTGCTCGCCTGCTCCCTGCTCCCTGCTCCCCTGCTCGGCCTGCTCAAACTCCTGCTCCCTGCTCCCTGCTCTGTACCGACCCTGCTCAATTTAGCCTGCTCGCCTGCTCATAAATACTCCCTGCTCGAATACCTGCTCTGCCTGCTCACGCCTGCTCAACCTGCTCCCCCCTGCTCATCTCGGTCCCTGCTCACCTGCTCCCTGCTCCCTGCTCGCCTGCTCCGCTCCTGCTCCTCCTGCTCTTTGATCCTGCTCCCCTGCTCACCCTGCTCGCGCCTGCTCCCTGCTCTCACCCCCTGCTCTCCTGCTCCCCTGCTCCGACCTGCTCCCTGCTCAACCTGCTCCCTGCTCCCTGCTCGCCTGCTCGAACATCCTGCTCCCTGCTCCCGGCCTGCTCTCCTGCTCTACGCCTGCTCCCTGCTCAAGACCTGCTCCCTGCTCGCCCCGGCCCTGCTCCCTGCTCGCCCTGCTCCGCCTGCTCCCTGCTCCGCCTGCTCACCTGCTCGCCTGCTCCCTGCTCGGTCTTCCTGCTCCCCTGCTCATTCGCCTGCTCAACCGTGTCTAAAGACTCCCTGCTCGACCCTGCTCCGTCCTGCTCTGTCTCCCTGCTCACCTGCTCTGCCTGCTCCATCGGTAACCTGCTCATTGCCTGCTCCGGGTTAACCTGCTCGTCCACCTGCTCCCTGCTCGTTCTCCATCCTGCTCTTTTCCTGCTCCCTGCTCCCTGCTCATCCTGCTCTCCCTGCTCCGGAGACTATGCCTGCTCCCGACCTGCTCTAATCCTGCTCCCCCCTGCTCTCCTGCTCCCTGCTCCCCTGCTCCCTGCTCCACCTGCTC"
	sub = "CCTGCTCCC"
	expected = [7, 14, 21, 39, 46, 53, 82, 89, 191, 225, 232, 280, 307, 335, 353, 369, 376, 404, 411, 441, 459, 481, 506, 538, 558, 707, 741, 748, 791, 813, 831, 838, 846]
	assert substring_positions(dna, sub) == expected



def hamming_distance(dna1, dna2):
	count = 0
	for i in range(min(len(dna1), len(dna2))):
		if dna1[i] != dna2[i]: count += 1
	return count

def test_hamming_distance():
	dna1 = "GAGCCTACTAACGGGAT"
	dna2 = "CATCGTAATGACGGCCT"
	assert hamming_distance(dna1, dna2) == 7



def is_adjacent(dna1, dna2, distance=3):
	if dna1[-distance:] == dna2[:distance]: return True
	return False

def test_is_adjacent():
	a = 'AAATAAA'
	b = 'AAATTTT'
	c = 'TTTTCCC'
	d = 'AAATCCC'
	e = 'GGGTGGG'

	assert is_adjacent(a,b) == True
	assert is_adjacent(a,d) == True
	assert is_adjacent(b,c) == True
	assert is_adjacent(a,c) == False
	assert is_adjacent(a,e) == False
	assert is_adjacent(b,a) == False


def dom_prob(pop_dict):
	#probabilities depend on population size, so figure that out
	pop_size = float(sum(pop_dict.values()))
	
	#determine_probabilities of all alleles
	outcome_probs = {
		'DD': ((pop_dict['D'] / pop_size) * ((pop_dict['D'] - 1) / (pop_size - 1))),
		'DH': ((pop_dict['D'] / pop_size) * ((pop_dict['H']) / (pop_size - 1))),
		'HD': ((pop_dict['H'] / pop_size) * ((pop_dict['D']) / (pop_size - 1))),
		'DR': ((pop_dict['D'] / pop_size) * ((pop_dict['R']) / (pop_size - 1))),
		'RD': ((pop_dict['R'] / pop_size) * ((pop_dict['D']) / (pop_size - 1))),

		'HH': ((pop_dict['H'] / pop_size) * ((pop_dict['H'] - 1) / (pop_size - 1))),
		'HR': ((pop_dict['H'] / pop_size) * ((pop_dict['R']) / (pop_size - 1))),
		'RH': ((pop_dict['R'] / pop_size) * ((pop_dict['H']) / (pop_size - 1))),

		'RR': ((pop_dict['R'] / pop_size) * ((pop_dict['R'] - 1) / (pop_size - 1))),
	}
	#print str(outcome_probs)

	dom_allele_probs = {
		'DD': 1.0  * outcome_probs['DD'],
		'DH': 1.0  * outcome_probs['DH'],
		'HD': 1.0  * outcome_probs['HD'],
		'DR': 1.0  * outcome_probs['DR'],
		'RD': 1.0  * outcome_probs['RD'],
		'HH': 0.75 * outcome_probs['HH'],
		'HR': 0.5  * outcome_probs['HR'],
		'RH': 0.5  * outcome_probs['RH'],
		'RR': 0.0  * outcome_probs['RR'],
	}

	return sum(dom_allele_probs.values())

def test_dom_prob():
	pop_dict = {
		'D': 2,
		'H': 2,
		'R': 2 }
	
	assert abs(dom_prob(pop_dict) - 0.7833) < 0.0001 


def rna_to_mrna(rna):
	from rna_codon_table import RNA_CODON_TABLE
	codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
	full_mrna = [RNA_CODON_TABLE[codon] for codon in codons]
	#find the first 'Stop'
	stop = full_mrna.index('Stop')
	mrna = ''.join(full_mrna[0:stop])
	return mrna

def test_rna_to_mrna():
	rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
	expected_mrna = 'MAMAPRTEINSTRING'
	assert rna_to_mrna(rna) == expected_mrna

