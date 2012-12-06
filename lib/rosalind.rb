module Rosalind
  def read_file(input_filename)
    IO.read(input_filename)
  end

  #return an array of lines
  def file_lines(input_filename)
    File.readlines(input_filename).map {|l| l.strip }
  end

  def write_file(output_string, output_filename='output.txt')
    File.open(output_filename, 'w') { |f| f.write(output_string + "\n") }
  end

  #Returns hash: { rosalind_id => dna string }
  def parse_fasta_file filename
    db = {}
    current_id = nil
    file_lines(filename).each do |line|
      if line =~ /^>(.+)$/
        current_id = $1
        db[current_id] = ''
      else
        db[current_id] << line
      end
    end

    db    
  end

  NUCLEOTIDES                 = ['A', 'C', 'G', 'T']
  NUCLEOTIDE_COMPLEMENT       = ['T', 'G', 'C', 'A']
  NUCLEOTIDE_TO_COMPLEMENT    = Hash[NUCLEOTIDES.zip(NUCLEOTIDE_COMPLEMENT)]
  GC                          = ['G', 'C']

  RNA                         = ['A', 'C', 'G', 'U']

  def count_nucleotides dna_string
    counts = NUCLEOTIDES.map {|n| dna_string.count(n) }
    Hash[NUCLEOTIDES.zip(counts)]
  end

  def transcribe_dna_to_rna dna_string
    dna_string.gsub('T', 'U')
  end

  def reverse_complement dna_string
    dna_string.reverse.split('').map {|n| NUCLEOTIDE_TO_COMPLEMENT[n] }.join('')
  end

  def gc_count dna_string
    gc =  0
    dna_string.each_char {|c| gc +=1 if GC.include?(c) }
    (gc.to_f / dna_string.length) * 100.0
  end

  def hamming_distance dna_string_one, dna_string_two
    hamming_distance = 0
    length = [dna_string_one.length, dna_string_two.length].min
    length.times do |n|
      hamming_distance += 1 unless dna_string_one[n] == dna_string_two[n]
    end    
    hamming_distance
  end

  def substring_positions dna_string, substring
    positions = []
    idx = 0
    positions << idx += 1 while (idx = dna_string.index(substring, idx))
    positions
  end
  
  def is_adjacent? dna_1, dna_2, overlap_length
    return false if dna_1 == dna_2
    if dna_2[0, overlap_length] == dna_1[-overlap_length, overlap_length]
      return true
    else
      return false
    end
  end
end

