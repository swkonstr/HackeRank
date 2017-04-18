# https://www.hackerrank.com/challenges/30-sorting  flag2!=True

n=3
a=[4,2,3,6,5,1]



NumOfSwaps=0
flag=True

while True:
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            NumOfSwaps+=1
            flag=False

    if flag==True:
    	break
    else:
    	flag=True

print("Array is sorted in",NumOfSwaps,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])