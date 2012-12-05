require_relative '../lib/rosalind.rb'
include Rosalind

input = read_file ARGV[0]

output = transcribe_dna_to_rna(input)

write_file output
