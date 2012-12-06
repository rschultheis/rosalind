require_relative '../lib/rosalind.rb'
include Rosalind

input = read_file ARGV[0]
value_array = input.split(' ').map {|n| n.to_i }

population = Hash[[:D, :H, :R].zip(value_array)]


population_size = population.values.inject(:+).to_f


outcome_probabilities = {
  :DD => ( (population[:D] / population_size) * ((population[:D] - 1) / (population_size - 1)) ),
  :DH => ( (population[:D] / population_size) * (population[:H] / (population_size -1)) ) * 2,
  :DR => ( (population[:D] / population_size) * (population[:R] / (population_size -1)) ) * 2,

  :HH => ( (population[:H] / population_size) * ((population[:H] - 1) / (population_size - 1)) ),
  :HR => ( (population[:H] / population_size) * (population[:R] / (population_size -1)) ) * 2,
  
  :RR => ( (population[:R] / population_size) * ((population[:R] - 1) / (population_size - 1)) ),
}

puts outcome_probabilities.inspect

dominate_allele_probabilities = {
  :DD => outcome_probabilities[:DD],
  :DH => outcome_probabilities[:DH],
  :DR => outcome_probabilities[:DR],

  :HH => outcome_probabilities[:HH] * 0.75,
  :HR => outcome_probabilities[:HR] * 0.5,

  :RR => 0.0,
}

puts dominate_allele_probabilities.inspect

has_dominate_allele_probability = dominate_allele_probabilities.values.inject(:+)

puts has_dominate_allele_probability

output = has_dominate_allele_probability.to_s
write_file output
