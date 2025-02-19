user_str = input("Enter the input file (dont forget .txt):")

file_input = open(user_str, 'r')

input_string = file_input.read()
new_string = input_string[0].upper()

for ch in input_string[1:]:
  if ch.isupper():
    new_string += f' {ch.lower()}'
  else:
    new_string += ch 


out_str = input("Enter the output file (dont forget .txt):")

file_output = open(out_str, 'w')
file_output.write(new_string)