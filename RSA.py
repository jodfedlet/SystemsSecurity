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
            
p = int(input('Enter a number: '))
q = int(input('Enter a secund number: '))
n = p * q
fiN = (p - 1) * (q - 1)

print('N: ',n)
print('Fi de n: ',fiN)
e = calcularE(fiN, 2)
print('e: ',e)




