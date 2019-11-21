def cifrar(msg, cv): #caracters + chave
	cesar = lambda char, cv, alf=26: chr((ord(char) - ord('a') + cv)%alf + ord('a'))
	return ''.join([cesar(char, cv) for char in msg.lower()])

mensagem_original = input('Digite a mensagem: ')
chave 	 = int(input('Digite a chave de codificacao: '))

def decifrar(cifragem_de_cesar, cv): #caracters - chave
	cesar = lambda char, cv, alf=26: chr((ord(char) - ord('a') - cv)%alf + ord('a'))
	return ''.join([cesar(char, cv) for char in cifragem_de_cesar.lower()])

def encontrarChave(cifragem_de_cesar, msg): #primeiroChrCif - primeiroChrOriginal
	return ord(cifragem_de_cesar[0]) - ord(msg[0])

import sys
cifragem_de_cesar = cifrar(mensagem_original, chave)
print('A cifragem de Cesar eh: ',cifragem_de_cesar)

opcao = int(input('Digite 1 para decifrar e 2 para encontrar a chave de codificacao: '))
if opcao == 1:
	cv	 = int(input('Digite a chave de decifragem: '))
	decifragem_de_cesar = decifrar(cifragem_de_cesar, cv)
	if chave == cv:
		print('A decifragem de Cesar eh: ',decifragem_de_cesar)
	else:
		print('Chave invahlida')	
elif opcao == 2:
	key = encontrarChave(cifragem_de_cesar, mensagem_original)
	print('A chave de codificacao eh: ',key)
else:
	sys.exit(1)
