module Rosalind
  def read_file(input_filename)
    IO.read(input_filename)
  end

  def write_file(output_string, output_filename='output.txt')
    File.open(output_filename, 'w') { |f| f.write(output_string + "\n") }
  end

  NUCLEOTIDES = ['A', 'C', 'G', 'T']
end

