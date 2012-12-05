require_relative '../lib/rosalind.rb'
include Rosalind

dnas = parse_fasta_file ARGV[0]

max = { id: '', gc: 0.0 }

dnas.each_pair do |id, dna|
  gc = gc_count(dna) 
  max.merge!(id: id, gc: gc) if gc > max[:gc]
end

output = max[:id] + "\n" + ("%.6f" % max[:gc]) + '%'
puts output
write_file output
