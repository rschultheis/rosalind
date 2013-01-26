import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import rna_to_mrna

dna = util.read_file(str(sys.argv[1]))
output = rna_to_mrna(dna)

util.write_file(output)

