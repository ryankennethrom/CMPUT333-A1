def filter_13_letter_words(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for word in infile:
            word = word.strip()
            if len(word) == 13:
                outfile.write(word + '\n')

# Specify input and output files
input_file = 'words.txt'
output_file = 'words13.txt'

# Run the function
filter_13_letter_words(input_file, output_file)

print(f'Filtered words saved to {output_file}')
