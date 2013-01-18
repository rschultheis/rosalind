require_relative '../lib/rosalind.rb'
include Rosalind

dnas = parse_fasta_file ARGV[0]
ids = dnas.keys

adjacents = []

ids.each_index do |i|
  ids.each_index do |j|
    next if i==j
    if is_adjacent?(dnas[ids[i]], dnas[ids[j]], 3)
      adjacents << ids[i] + ' ' + ids[j]
    end
  end
end

output = adjacents.join("\n")
puts output
write_file output
