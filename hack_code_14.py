#https://www.hackerrank.com/challenges/30-scope
class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        a=self.__elements
        a.sort()
        maxd = a[len(a)-1]-a[0]
        self.maximumDifference = maxd
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)