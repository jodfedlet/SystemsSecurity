import string
alfabet = list(string.ascii_uppercase)
MAX = 26

def findLetter(letter, option):
	for i in range(0,MAX):
		if option[i] == letter:
			break
	return i		

def cypher(key, message):
	message_len, mes = len(message), []
	for i in range(message_len):
		if message[i] != '':
			cyph = findLetter(message[i], alfabet)
			mes.append(key[cyph])
	return ''.join(mes)	

def uncypher(key, cypher_message):
	message_len, mes = len(cypher_message), []
	for i in range(message_len):
		if cypher_message[i] != '':
			cyph = findLetter(cypher_message[i], key)
			mes.append(key[cyph])
	return ''.join(mes)	

message = input('Write your message: ').upper()
key = input('Enter the key: ')

response = False
for i in range(0, MAX):
	len_key, response = len(key), False
	for j in range(len_key):
		if alfabet[i] == key[j]:response = True
	if not response: key += alfabet[i]		

cypher = cypher(key, message)
print('The cypher text is: ', cypher)

uncypher = uncypher(key, cypher)
print('The uncypher message is: ',message)