#myclass.py

# gpa.py
# Program to find student with highest GPA

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours
    
    def addGrade(self, gradePoint, credits):
        self.hours += credits
        self.qpoints += gradePoint * credits

def main():
    print("This program calculates a total GPA for a student.")
    s = Student("C", 0, 0)
    while True:
        grade, credits = input("Enter student grades and credits: ").split(',')
        grade = float(grade)
        credits = float(credits)
        if grade < 0:
            break
        #grade = float(grade)
        #credits = float(credits)
        s.addGrade(grade, credits)
        
    print("GPA: ", s.gpa())
if __name__ == '__main__':
    main()
