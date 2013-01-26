import sys
from os import path
#load the libraries
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '../lib')))
import rosalind_util as util

from methods import dom_prob

input_line = util.read_file(str(sys.argv[1]))
values = map(int, input_line.split(' '))
pop_dict = dict(zip(['D', 'H', 'R'], values))

prob = dom_prob(pop_dict)

output = "%0.5f" % prob
util.write_file(output)

