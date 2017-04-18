n = int(input())

e = input()
ee = e.split(' ')
e = [int(i) for i in ee]

f = input()
ff = f.split(' ')
f = [int(i) for i in ff]

idx = 0
x=[]
f.reverse()

for i in e:
    y = 0
    d = f.pop()
    while y < d:
        x.append (i)
        y += 1
        
x.sort()
test=int(len(x)/2)
if (test & 1) == 1: # чет целого = нечет полусписка

    il1=int(len(x)/4)
    lmed=float(x[il1])
    iu1=int(len(x)/2)+int(len(x)/4)+1
    umed=float(x[iu1])

elif (test & 1) !=1: # нечет целого = чет полусписка

    il1=int(len(x)/4)-1
    il2=int(len(x)/4)
    lmed=float((x[il1]+x[il2])/2)
    iu1=int(len(x)/2)+int(len(x)/4)-1
    iu2=int(len(x)/2)+int(len(x)/4)
    umed=float((x[iu1]+x[iu2])/2)
    
print (umed-lmed)