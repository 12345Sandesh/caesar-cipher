#main function
choice = input(str('Encryption(E) or Decryption(D) : '))
if choice == 'E':
	def caesar(text, shift, encrypt = 'True'):
		if not isinstance(shift, int) or isinstance(shift, bool):
			return 'Shift should be integer.'

		if shift < 1 or shift > 25:
			return 'Shift should be between the number 1 and 25'

		if not encrypt:
			return "Please provide encrypted message to decrypt."

		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		shifted_alphabet = alphabet[shift:] + alphabet[:shift]
		translation_table = str.maketrans(alphabet, shifted_alphabet)
		return text.translate(translation_table)

	def encrypt(text, shift):
		return caesar(text, shift)

	text = a = input(str('Enter the message to encrypt.'))
	shift = b = int(input('Enter the shift to be made:'))

	encrypted_text = caesar(a,b)
	print(f'Your encrypted text : {encrypted_text}')	
else:
	def caesar(text, shift, decrypt = 'True'):
		if not isinstance(shift, int) or isinstance(shift, bool):
			return 'Shift should be integer.'

		if shift < 1 or shift > 25:
			return 'Shift should be between the number 1 and 25'

		if not decrypt:
			return "Please provide encrypted message to decrypt."

		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		shifted_alphabet = alphabet[shift:] + alphabet[:shift]
		translation_table = str.maketrans(shifted_alphabet, alphabet)
		return text.translate(translation_table)

	def decrypt(text, shift):
		return caesar(text, shift)

	text = a = input(str('Enter the message to decrypt.'))
	shift = b = int(input('Enter the shift to be made:'))

	decrypted_text = caesar(a,b)
	print(f'Your decrypted_text: {decrypted_text}')
