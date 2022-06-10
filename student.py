class Student:
    def __init__(self,first_name,last_name,age,country):
           self.first_name=first_name
           self.last_name=last_name
           self.age=age
           self.country=country

    def greet(self):
               return f"Hello {self.first_name} {self.last_name} this is your fullnames"
    def initials(self):
               return f"Hello {self.first_name[0]} {self.last_name[0]} this is your initials"
    def yob(self):
        year=2022-self.age
        return f"Hello you were born in {year}"

                 
        