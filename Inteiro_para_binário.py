n = 14 #1110
numero="" #0111

while n>=1:
    res = n%2
    numero+=str(res)
    b=n/2
    n=int(b)

s=len(numero)

while s!=0:
    print(numero[s-1], end="")
    s+=-1

#-------------------------------------------------Binário para Inteiro-----------------------------------------------

print()

n = 1110 #14
count=0
res=0
for i in str(n): #Tamanho de n
    count+=1

for x in str(n): #Conversão para inteiro
    count-=1
    res += (int(x)*(2**(count)))
print(res)  



