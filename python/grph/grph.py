import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import is_adjacent

dna_db = util.read_fasta_file(str(sys.argv[1]))

output =''
for id1 in dna_db.keys():
	for id2 in dna_db.keys():
		if id1==id2: continue
		if is_adjacent(dna_db[id1], dna_db[id2]):
			output += ' '.join([id1, id2]) + '\n'


util.write_file(output)

