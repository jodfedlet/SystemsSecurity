def prim(j):
    t = 1
    while t == 1:
        n = j+1
        k = 2
        prime = 0
        while k <= n:
            if n % k == 0:
                prime+=1
            k+=1    
        if prime == 1:
            return n
        else:
            j+=1

p = int(input('Enter a number: '))
q = int(input('Enter a secund number: '))
n = p * q
e = (p - 1) * (q - 1)
a = e
i = 2
list = []
while(a >= i):
    if a % i == 0:
        res = a // i
        list.append(i)
        a = res 
    else:
        i+=1  

last = list[-1]
j = last + 1
e = prim(j)
print(e)
print(n)

