require_relative '../lib/rosalind.rb'
include Rosalind

lines = file_lines ARGV[0]
dna1 = lines[0]
dna2 = lines[1]

output = hamming_distance(dna1, dna2).to_s

puts output
write_file output
