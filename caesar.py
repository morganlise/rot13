
def rotate_character(char, rot):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	if char.isalpha() == False:
		return char
	else:
		adjusted_index = (alphabet_position(char) + rot) % 26
		finalChar = ""
		if char.isupper() == True:
			finalChar = alphabet[adjusted_index].upper()
		else:
			finalChar = alphabet[adjusted_index]
		return finalChar

def alphabet_position(letter):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	letter = letter.lower()
	indexL = alphabet.index(letter)
	return indexL

def encrypt(text, rot):
	new_message = ''
	for char in text:
		new_char = rotate_character(char, rot)
		new_message = new_message + new_char
	return new_message