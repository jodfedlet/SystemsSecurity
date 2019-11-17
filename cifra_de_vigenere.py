
def cifrar(msg, key, alfabeto, opcao):
	key_len, key_aux, msg_aux = len(key), [ord(i) for i in key], [ord(j) for j in msg]
	msg_len, alf_len = len(msg_aux), len(alfabeto)

	res = ''
	for i in range(msg_len):
		value = 0
		if(opcao == 1):
			value = (msg_aux[i] + key_aux[i%key_len]) % alf_len
		if(opcao == 2):
			value = (msg_aux[i] - key_aux[i%key_len]) % alf_len
		res += chr(value + ord(alfabeto[0])) 
	return res			

import string as stg
key = 'LIMAO'
msg = 'ATACARBASESUL' 
alf = list(stg.ascii_lowercase)
cifra_de_vigenere = cifrar(msg, key, alf,1)
print('A cifragem de Vigenere: ',cifra_de_vigenere)
decifra_de_vigenere = cifrar(msg, key, alf,2)
print('A decifragem de Vigenere: ',decifra_de_vigenere)


