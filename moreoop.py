class Employee:
    
    def __init__(self,name,role,salary,dob):
        self.name=name
        self.role=role
        self.salary=salary
        self.dob=dob



    def increase_salary(self):
        self.salary +=100



    
    def calculate_age(self):
        dob=int(dob)
        self.age=(2024-dob)


class Manager:

    def __init__(self,name,role,salary,dob,bonus):
        self.name=name
        self.role=role
        self.salary=salary
        self.dob=dob
        self.bonus=bonus


    def incease_salary(self):
        self.salary+=200
        



    def calculate_age(self):
        dob=int(dob)
        self.age=(2024-dob)



    def increase_bonus(self):
        self.bonus+=100
     
        



