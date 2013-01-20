import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import nucleotide_counts

dna = util.read_file(str(sys.argv[1]))
counts = nucleotide_counts(dna)
output = ' '.join(map(str, [counts['A'], counts['C'], counts['G'], counts['T']]))

util.write_file(output)

