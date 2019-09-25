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

def calcularD(e,fiN, d):
    i = 2
    while(d >= i):
        dd = d
        if e * dd % fiN == 1:
            return d
        else:
            d+=1  

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

def isPrime(n):
    prim = 0
    for i in range(2,n+1):
        if n % i == 0:
            prim+=1
    if prim == 1:
        return True
    else:
        return False

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

  
p,q = input('Digite os 2 numeros primos: ').split(' ')  
p = int(p)
q = int(q)

if(isPrime(p) == False or isPrime(q) == False):
    print('Os numeros devem ser primos!')
else:
    n = p * q
    fiN = (p - 1) * (q - 1)
    max = 0
    max = p if p > q else q
    ee = max+1
    e = calcularE(fiN, ee)
    print('Chave publica: ({} , {})'.format(e,n))
    message = input('Enter a message: ')
    messLower = message.lower()
    cifrarMes(n,e,messLower)
    
    d = calcularD(e,fiN, ee)
    
    print('Chave privada: ({} , {})'.format(d,fiN))
    

    




