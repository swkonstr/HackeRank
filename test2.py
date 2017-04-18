def addTwoDigits(n):
    n=str(n)
    a=int(n[0])
    b=int(n[1])

    sum=a+b
    print(a,b,sum)
    return sum

n=34
print(addTwoDigits(n))