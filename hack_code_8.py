import sys
n = int(input().strip())
d={}
for i in range(n):
    line=input().split(' ')
    d[line[0]]=line[1]

while(True):
    try:
        q=input()
        if q in d:
        	print (q+"="+d[q])
        else:
        	print ("Not found")
    except:
        break


#n = int(input())
#name_numbers = [input().split() for _ in range(n)]
#phone_book = {k: v for k,v in name_numbers}
#while True:
#    try:
#        name = input()
#        if name in phone_book:
#            print('%s=%s' % (name, phone_book[name]))
#        else:
#            print('Not found')
#    except:
#        break