lst=['1', '2']
choice=(lst,) #tuple init

print(choice)
choice+=(lst,) #tuple add
print(choice)

x,y = choice[1] #tuple unpack

print (x,y)

#Test.objects.all() return all
#Test.objects.filter(id=1) return [1]
#Test.objects.