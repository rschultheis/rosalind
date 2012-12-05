require_relative '../lib/rosalind.rb'
include Rosalind

input = read_file(ARGV[0])

output = count_nucleotides(input).values.join(' ')

write_file(output)
