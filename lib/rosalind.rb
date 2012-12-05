module Rosalind
  def read_file(input_filename)
    IO.read(input_filename)
  end

  def write_file(output_string, output_filename='output.txt')
    File.open(output_filename, 'w') { |f| f.write(output_string + "\n") }
  end

  NUCLEOTIDES = ['A', 'C', 'G', 'T']
  RNA         = ['A', 'C', 'G', 'U']

  NUCLEOTIDE_TO_RNA = Hash[NUCLEOTIDES.zip(RNA)]

  def count_nucleotides dna_string
    counts = NUCLEOTIDES.map {|n| dna_string.count(n) }
    Hash[NUCLEOTIDES.zip(counts)]
  end

  def transcribe_dna_to_rna dna_string
    NUCLEOTIDE_TO_RNA.each_pair { |n, r| dna_string.gsub!(n,r) }
    dna_string
  end
end

