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
    return cifrar 
    
def decifrarMes(e,n,d, mess):
    while True:
        try:
            ddd,dn = input('Digite a chave privada: ').split(' ')        
            dn = int(dn)
            ddd = int(ddd)
            if n != dn or ddd != d:
                print('Chave invalida')
            else:
                decifrar = []
                for num in mess:
                    decryp = num ** d % n
                    decifrar.append(decryp)
                print(55*'-')    
                print('Mensagem Cifrada: ', mess)     
                print('Mensagem Decifrada: ', end="") 
                for cif in decifrar:
                    print('{}'.format(cif), end="")
                print() 
                print(55*'-')
                texto = input('Quer ver o texto da mensagem? (S para aceitar): ')
                if texto == 'S' or texto == 's':
                    print('Mensagem Decifrada em texto: ', end="") 
                    for cif in decifrar:
                        print('{}'.format(chr(cif)), end="")
                    print()
                    exit(1)
                else:
                    exit(1)
        except ValueError:
             print('Voce deve digitar 2 numeros na mesma linha!')
                         
while True:       
    try:
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
            maxNUm = max+1
            e = calcularE(fiN, maxNUm)
            print(55*'*')
            print('Chave publica: ({} , {})'.format(e,n))
            print(55*'*')
            print()
            message = input('Enter a message: ')
            messLower = message.lower()
            
            mess =  cifrarMes(n,e,messLower)  
            d = calcularD(e,fiN, maxNUm)
            print()
            print(55*'*')
            print('Chave privada: ({} , {})'.format(d,n))
            print(55*'*')
            print()
            decifrarMes(e,n,d, mess)
            
    except ValueError:
        print('Voce deve digitar 2 numeros na mesma linha!')
    




