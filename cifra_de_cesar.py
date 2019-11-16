def cifrar(msg, cv):
	cesar = lambda char, cv, alf=26: chr((ord(char) - ord('a') + cv)%alf + ord('a'))
	return ''.join([cesar(char, cv) for char in msg.lower()])

mensagem = input('Digite a mensagem: ')
chave 	 = int(input('Digite a chave da codificacao: '))
print(cifrar(mensagem, chave))