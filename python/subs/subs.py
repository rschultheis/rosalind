import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import substring_positions

lines = util.read_file(str(sys.argv[1])).split("\n")
dna = lines[0]
sub = lines[1]

matches = substring_positions(dna, sub)


output = " ".join(map(str, matches))

util.write_file(output)

