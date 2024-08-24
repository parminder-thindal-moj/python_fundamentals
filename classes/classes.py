class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary


emp_1 = Employee(name="parminder", age=33, position="data_engineer", salary=1200)
emp_2 = Employee(name="parminder", age=33, position="data_engineer", salary=1200)

print(emp_1.__dict__)
print(emp_2.__class__)

print(emp_1)
print(emp_2)

# some comment here

class Employee:
    pass


e = Employee()

print(e.__dict__)
