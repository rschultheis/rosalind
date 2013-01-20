import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import gc_content

dna_db = util.read_fasta_file(str(sys.argv[1]))

max_gc = {'id': 'xxx', 'content': -1.0}

for dna_id, dna in dna_db.items():
	gc = gc_content(dna)
	if gc > max_gc['content']:
		max_gc = {'id': dna_id, 'content': gc}

output = max_gc['id'] + "\n" + "%2.6f" % max_gc['content'] + '%'

util.write_file(output)

