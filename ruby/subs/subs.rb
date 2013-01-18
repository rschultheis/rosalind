require_relative '../lib/rosalind.rb'
include Rosalind

lines = file_lines ARGV[0]
dna = lines[0]
sub = lines[1]

output = substring_positions(dna, sub).join(' ')

puts output
write_file output
