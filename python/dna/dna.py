import sys

#read the input file
input_filename = str(sys.argv[1])
print "opening input: " + input_filename
input_file = open(input_filename, 'r')
raw_input = input_file.read()
input_file.close()
print "read contents:\n" + raw_input

#process the input

dna = raw_input

counts = dict(A=0, C=0, G=0, T=0)

for n in dna:
	if n in counts:
		counts[n] += 1


#format output
output = ' '.join(map(str, [counts['A'], counts['C'], counts['G'], counts['T']]))


#write the output
output_filename = 'output.txt'
output_file = open(output_filename, 'w')
output_file.write(output)
output_file.write("\n")
output_file.close()
print "wrote to: " + output_filename + "\n" + output

