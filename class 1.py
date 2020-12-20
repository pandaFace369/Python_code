class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.mail=first+'.'+last+'@company.com'
    def fullname(self):
      return '{} {}'.format(self.first,self.last)


emp_1=Employee('Eliott','Alderson',100000)
print(emp_1.mail)