class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # constructor
    def __init__(self, firstName, lastName, idNum, scores):
        # inheriting the property from base class
        super().__init__(firstName, lastName, idNum)
        self.scores = scores

    def calculate(self):
        self.total = sum(self.scores)
        self.avg = self.total / numScores

        if (self.avg) >= 90:
            return "O"
        elif (self.avg) >= 80:
            return "E"
        elif (self.avg) >= 70:
            return "A"
        elif (self.avg) >= 55:
            return "P"
        elif (self.avg) >= 40:
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())