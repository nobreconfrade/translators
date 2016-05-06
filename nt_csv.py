""" 
PRAISE THE SUN 

Author: William Pereira

An RDF NT -> CSV translator, hope it works.

Version 1.00

-Saving 'line' in 'newline' on CSV format; CHECKED
-Save 'newline' on the 'csv_data.csv' file; CHECKED

"""
nt_file = input ("Write the file name to be translated (without .nt):")
nt_file += ".nt"
with open(nt_file,'r', buffering = 4096) as f1:
	# print ("File has been successfully loaded.")
	with open("csv_data.csv",'w') as f2:
		# print ("Translated file has been successfully loaded.")
		for line in f1: 
			# print (line)
			newline = ""
			space_count = 0
			# test_line = "abcd   efgh"
			for enum_letter,letter in enumerate(line):
				# print (letter)	
				# print (enum_letter,' ',letter)
				if(letter == '<'):
					newline += letter.replace('<','"')
				elif(letter == '>'):
					newline += letter.replace('>','"')
				elif(letter == ' ' and space_count<2):
					newline += letter.replace(' ',',')
					space_count += 1
				
				elif(letter == '.' and line[enum_letter-1] == ' '):
					break
				else:
					newline += letter
			# print (newline)
			newline += '\n'
			f2.write(newline)
		print ("Data successfully translated.")