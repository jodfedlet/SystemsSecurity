def factoriser(n):
  i = 2
  lista = []
  while True:
    a = i
    if n % a == 0:
      lista.append(a)
      res = n // a
      if res % 2 == 1:
        lista.append(res)
        return lista
      else:
        i+=1  
    else:
      i+=1
    
def calcularD(e,fiN, d):
    i = 2
    while(d >= i):
        dd = d
        if e * dd % fiN == 1:
            return d
        else:
            d+=1  

def decifrarMes(e,n,d, mess):
    decryp = e ** d % n 
    print('Mensagem: ',decryp)
    print() 
 
n,e,c = input('Digite os 3 valores: ').split(' ')  
n = int(n)
e = int(e)
c = int(c)

pq = factoriser(n)

d = calcularD(e,fiN, 2)
decifrarMes(e,n,d, c)