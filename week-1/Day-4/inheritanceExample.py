class EMPLOYEE:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def high_sal(self,other_emp):
        if self.salary >= other_emp.salary:
            return self
        else:
            return other_emp
    def disp(self):
        print(self.name , self.salary) # type: ignore


class Manager(EMPLOYEE):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department

        #call the parent class constructor to initialize name and sal

#emp1=EMPLOYEE("Alice",50000)
mgr1=Manager("Bob",85000,"Eng")
#high=emp1.high_sal(mgr1)
#print(f"high sal is {high.salary}, earned by {high.name}")
mgr1.disp()
#print(f"high sal is {mgr1.salary}, earned by {mgr1.name}")
