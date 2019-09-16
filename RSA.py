'''
def prim(j):
    k = 2
    prime = 0
    e = 0
    while j < j + 15 :
        if j % k != 0:
            e = j
            return e
        else:
            j+=1'''

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

'''prime = prim(j)
print(prime)'''
print(n)

