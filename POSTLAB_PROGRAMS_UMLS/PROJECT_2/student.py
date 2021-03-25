import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
    
    def __eq__(self, other):
        """Returns if equal or not"""
        if (self.name == other.name):
            return "Equal"
        else:
            return "Not Equal"

    def __lt__(self, other):
        """Returns if less than or not"""
        if (self.name < other.name):
            return "Less Than"
        else:
            return "Not less than"

    def __gt__(self, other):
        if self.name > other.name:
            return "Greater than"
        elif self.name == other.name:
            return "Both are equal"
        else:
            return "Not greater or equal"

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    studentsList = []

    student = Student("Justine", 5)
    for i in range(1, 6):
        student.setScore(i, 100)
    studentsList.append(student)

    student1 = Student("Mon", 8)    
    for i in range(1, 9):
        student1.setScore(i, 100)
    studentsList.append(student1)

    student2 = Student("Darren", 5)
    for i in range(1, 6):
        student2.setScore(i, 100)
    studentsList.append(student2)

    random.shuffle(studentsList)

    print("Shuffled list of Students: ")

    for i in studentsList:
        print(i.__str__())

    print("\nSorted list of Students: ")

    studentsList.sort(key = lambda x:x.name)

    for i in studentsList:
        print(i.__str__())

if __name__ == "__main__":
    main()