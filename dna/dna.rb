require_relative '../lib/rosalind.rb'
include Rosalind

input = read_file(ARGV[0])

output = NUCLEOTIDES.map {|n|
  input.count(n)
}.join(' ')

write_file(output)
