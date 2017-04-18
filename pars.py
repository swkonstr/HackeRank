# https://docs.python.org/3/tutorial/

try:
    input_file = open('F:/OneDrive/Python/hakerank/test.txt', 'r')
except IOError:
    print('cannot open file')
try:
    output_file = open('F:/OneDrive/Python/hakerank/test2.txt', 'w', encoding='utf-8')
except IOError:
    print('cant save file')

inputLinesNum=0
mailLinesNum=0
words=[]
mail="@"
flag=0
for line in input_file:
    inputLinesNum+=1
    if flag==1:
        print(line, file=output_file)
        flag=0
    if line.find(mail)>0:
        mailLinesNum+=1
        flag=1
        line=line.rstrip('\n')
        line=line.strip(' ')
        words=line.split(' ')
        for word in words:
            if word.find(mail)>0:
                print(word, file=output_file)

print("Обработано: ", inputLinesNum)
print("Обнаружено: ", mailLinesNum)
input_file.close()
output_file.close()

	#for line in input_file:
		#print (line)
		
		#line = line.rstrip('\n')
		#words = line.split(' ')
		
		#for word in words:
			#if word
			#qwe.append(word)
		#print (qwe)

	#for word in words:
	#	word = word.split(',')
	#	print (word)

#try:
	    #    output_file = open('C:/Users/swkon/OneDrive/Python/pars/test2.txt', 'w', encoding='utf-8')
        #except IOError:
        #    print('cannot save file', arg)
        #else:
	    #    output_file.write(qwe)