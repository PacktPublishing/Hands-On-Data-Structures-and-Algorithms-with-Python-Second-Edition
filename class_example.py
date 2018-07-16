class Employee(object):
  numEmployee = 0
  def __init__(self, name, rate):
    self.owed = 0
    self.name = name
    self.rate=rate
    Employee.numEmployee += 1
  def __del__(self):
    Employee.numEmployee -= 1
  def hours(self, numHours):
    self.owed += numHours * self.rate
    return("%.2f hours worked" % numHours)
  def pay(self):
    self.owed = 0
    return("payed %s " % self.name)


emp1= Employee("Jill", 18.50)

emp2=Employee("jack", 15.50)

Employee.numEmployee

emp1.hours(20)

emp1.owed

emp1.pay()
