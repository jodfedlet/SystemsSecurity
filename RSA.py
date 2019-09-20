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

# def inversoDoE(e, fiN):
#     fin = fiN
#     fi = []
#     if e % fiN == 1:
#         fi.append(fiN)
#         return fi
#     else:
#         fiN +=1
#         return inversoDoE(e, fiN)

def cifrarMes(n, e, messLower):
    cifrar = []
    for let in messLower:
        asc = ord(let)
        cryp = asc**e % n
        cifrar.append(cryp)
    print('Mensagem Normal: ', messLower.capitalize())     
    print('Mensagem Cifrada: ', end="") 
    for cif in cifrar:
        print('{}'.format(cif), end="")   
    print()  
    

# def decifrarMes(n,e):
#     dn,de = input('Digite a chave de 2 numeros: ').split(' ')        
#     dn = int(dn)
#     de = int(de)
#     if n != dn or e != de:
#         print('Chave invalida')
#     else:
#         print('Teste')


import string as str  
p,q = input('Digite os 2 numeros primos: ').split(' ')        
p = int(p)
q = int(q)
n = p * q
fiN = (p - 1) * (q - 1)
e = calcularE(fiN, 2)
print('Chave publica: ({} , {})'.format(n,e))
message = input('Enter a message: ')
messLower = message.lower()
cifrarMes(n,e,messLower)

    




