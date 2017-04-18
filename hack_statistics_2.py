# https://www.hackerrank.com/challenges/s10-weighted-mean

n = int(input())
x = input()
xx = x.split(' ')
x = [int(i) for i in xx]
w = input()
ww = w.split(' ')
w = [int(i) for i in ww]

idx=0
sum=0
while idx < n:
    sum += x[idx]*w[idx]
    idx += 1
    
idx=0
sum2=0
while idx < n:
    sum2 += w[idx]
    idx += 1
    
print (round(sum/sum2, 1))

# еще вариант

input()
X = map(float,raw_input().split())
W = map(float,raw_input().split())
print round(sum([i[0]*i[1] for i in zip(X,W)])/sum(W),1)

# еще вариант

n = int(raw_input())
nums = [int(x) for x in raw_input().split()]
weight = [int(x) for x in raw_input().split()]
print round(1.0*sum([nums[i]*weight[i] for i in range(n)])/sum(weight), 1)