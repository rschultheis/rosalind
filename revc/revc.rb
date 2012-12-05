require_relative '../lib/rosalind.rb'
include Rosalind

input = read_file ARGV[0]
puts input

output = reverse_complement(input)

puts output
write_file output
