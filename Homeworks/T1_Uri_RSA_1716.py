def isPrime(n):
    prim = 0
    for i in range(2,n+1):
        if n % i == 0:
            prim+=1
    if prim == 1:
        return True
    else:
        return False

def factoriser(n):
  i = 2
  lista = []
  while n > i:
    a = i
    if n % a == 0:
      res = n // a
      if isPrime(res) and a * res == n:
        lista.append(res)
        lista.append(a)
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

def decifrarMes(n,d, mess):
  return pow(mess, d, n) 

n,e,c = [ int(x) for x in input().split(" ")] 
if n > 14 and n < pow(10,9) and e > 0 and c > 0 and c < n:
  pq = factoriser(n)
  fiN = (pq[0] - 1) * (pq[1] - 1)
  d = calcularD(e,fiN, 2)
  print(decifrarMes(n,d, c))
