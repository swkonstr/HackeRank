# https://www.hackerrank.com/challenges/s10-quartiles

n = int(input())
x = input()
xx = x.split(' ')
x = [int(i) for i in xx]


x.sort() # сортировка


test=int(len(x)/2)
if (test & 1) == 1: # чет целого = нечет полусписка

    il1=int(len(x)/4)
    lmed=x[il1]
    ix1=int(len(x)/2)-1
    ix2=int(len(x)/2)
    xmed=(x[ix1]+x[ix2])/2
    iu1=int(len(x)/2)+int(len(x)/4)
    umed=x[iu1]

elif (test & 1) !=1: # нечет целого = чет полусписка

    il1=int(len(x)/4)-1
    il2=int(len(x)/4)
    lmed=(x[il1]+x[il2])/2
    ix1=int(len(x)/2)
    xmed=x[ix1]
    iu1=int(len(x)/2)+int(len(x)/4)-1
    iu2=int(len(x)/2)+int(len(x)/4)
    umed=(x[iu1]+x[iu2])/2

print (int(lmed))
print (int(xmed))
print (int(umed))