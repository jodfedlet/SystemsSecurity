
def vigenereCypher(msg, key, alfabeto, opcao):
	key_len, key_aux, msg_aux = len(key), [ord(i) for i in key], [ord(i) for i in msg]
	msg_len, alf_len = len(msg_aux), len(alfabeto)

	res = ''
	for i in range(msg_len):
		value = 0
		if(opcao == 1):
			value = (msg_aux[i] + key_aux[i%key_len]) % alf_len
		# if(opcao == 2):
		# 	value = (msg_aux[i] - key_aux[i%key_len]) % alf_len
		res += chr(value + ord(alfabeto[0])) 
	return res	

def findKey(msg, key):	
	key_len = len(key)
	new_key = []
	for i in range(len(msg)):
		new_key.append(key[i%key_len])
	return new_key

import string as stg
key = 'LIMAO'
msg = 'ATACARBASESUL' 
alf = list(stg.ascii_lowercase)

KEY = ''.join(findKey(msg, key))

print('A chave: ',KEY)

cifra_de_vigenere = vigenereCypher(msg, KEY, alf,1)
print('A cifragem de Vigenere: ',cifra_de_vigenere)

# decifra_de_vigenere = vigenereCypher(cifra_de_vigenere, KEY, alf,2)
# print('A decifragem de Vigenere: ',decifra_de_vigenere)


