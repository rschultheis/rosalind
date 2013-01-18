require_relative '../lib/rosalind.rb'
include Rosalind

input = read_file ARGV[0]
puts input

output = transcribe_dna_to_rna(input)

outs output
write_file output
