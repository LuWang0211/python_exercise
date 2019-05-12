class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
	
    def apply_raise(self):
	    self.pay = int(self.pay * self.raise_amount)

    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.num_of_emps)

print(f'Employee.raise_amount_a= {Employee.raise_amount}')
print(f'emp_1.raise_amount = {emp_1.raise_amount}')
print(f'emp_2.raise_amount = {emp_2.raise_amount}')
print(f'Employee.raise_amount_b= {Employee.raise_amount}')