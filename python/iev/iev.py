import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import expected_dom_offspring

values = util.read_file(str(sys.argv[1])).split(' ')
couple_dict = dict(zip(['DD', 'DH', 'DR', 'HH', 'HR', 'RR'], map(int, values)))

output = "%.1f" % expected_dom_offspring(couple_dict)

util.write_file(output)

