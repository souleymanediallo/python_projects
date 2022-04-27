class Employee:
    raise_amont = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "" + last + "@google.com"

    def fulname(self):
        print(f"{self.first} {self.last}")

    def raise_pay(self):
        self.pay *= self.raise_amont 

    @classmethod
    def set_raise_amont(cls, amont):
        cls.raise_amont = amont

    @classmethod
    def formatstring(cls, emptstr):
        first, last, pay = emptstr.split("-")
        return cls(first, last, pay)

    @staticmethod
    def working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime

a = Employee("Diallo", "Souleymane", 60000)
b = Employee("Ba", "Amada", 57000)
c = Employee("Ba", "Mamad", 55000)
my_date = datetime.date(2022, 7, 19)
employee_1 = "Baidy-Diop-60000"
print(Employee.working_day(my_date))




    




    

