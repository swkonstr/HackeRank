class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        sum = 0
        for i in self.scores:
            sum += i
        b = int(sum/len(self.scores))
        if b >= 40:
            if b >= 55:
                if b >= 70:
                    if b >= 80:
                        if b >= 90:
                            return "O"
                        else:
                            return "E"
                    else:
                        return "A"
                else:
                    return "P"
            else:
                return "D"
        else:
            return "T"
        



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())