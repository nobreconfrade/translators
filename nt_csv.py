""" 
PRAISE THE SUN 

Author: William Pereira

An RDF NT -> CSV translator, hope it works.

Version 0.01

-Saving 'line' in 'newline' on CSV format;

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
			for enum_letter,letter in enumerate(line):
				# print (letter)	
				if(letter == '<'):
					newline += letter.replace('<','"')
				elif(letter == '>'):
					newline += letter.replace('>','"')
				elif(letter == ' ' and space_count<2):
					newline += letter.replace(' ',';')
					space_count += 1
				elif(letter == ' ' and letter[enum_letter + 1] == '.'):
					newline += letter.replace(' ','')
					newline += letter.replace('.','')
				else:
					newline += letter
			print (newline)