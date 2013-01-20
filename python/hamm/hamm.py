import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import hamming_distance

lines = util.read_file(str(sys.argv[1])).split("\n")
dna1 = lines[0]
dna2 = lines[1]

dist = hamming_distance(dna1, dna2)

output = str(dist)

util.write_file(output)

