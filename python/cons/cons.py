import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import profile_matrix, consensus_string, NUCLEOTIDES

dnas = util.read_file(str(sys.argv[1])).splitlines()

p_mat = profile_matrix(dnas)
con_str = consensus_string(p_mat)

output = con_str + '\n'
for n in NUCLEOTIDES:
	output += n + ': ' + ' '.join(map(str, p_mat[n])) + '\n'

util.write_file(output)

