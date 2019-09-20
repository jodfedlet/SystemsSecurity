def divisor(a):
    i = 2
    liste = []
    while(a >= i):
        if a % i == 0:
            res = a // i
            liste.append(i)
            a = res 
        else:
            i+=1  
    return liste

def mdc(fin, l):
    listFin = divisor(fin)
    listE   = divisor(l)
    a = [ e for e in listE if e in listFin]
    md = 1
    for h in a:
        md *=h 
    return md

def calcularE(fiN,e):
    efin = e
    if mdc(fiN, efin) == 1:
        return efin
    else:
        e += 1
        return calcularE(fiN,e)

def cifrarMes(n, e):
    message = input('Enter a message: ')
    messLower = message.lower()
    cifrar = []
    for let in messLower:
        asc = ord(let)
        cryp = asc**e % n
        cifrar.append(cryp)
    print('Mensagem Cifrada: ', end="") 
    for cif in cifrar:
        print('{} '.format(cif), end="")   
    print()  

import string as str          
p = int(input('Enter a number: '))
q = int(input('Enter a secund number: '))
n = p * q
fiN = (p - 1) * (q - 1)
e = calcularE(fiN, 2)
print('Chave publica: ({} , {})'.format(n,e))

cifrarMes(n,e)

    




