class Person():
    def __init__(self, name, age, unik, date, started):
        self.name = name
        self.age = age
        self.university = unik
        self.gradDate = date
        self.edStarted = started
    
    def checkPerson(self):
        print(self.age, self.name, self.university)

    def checkInSchoolYears(self):
        ans = self.gradDate - self.edStarted
        gradAge = self.age + ans
        print("He should graduate in " + str(ans) + " years")
        print("So he will be " + str(gradAge))