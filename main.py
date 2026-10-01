from inheritence import (
Employee,
Developer,
SeniorDeveloper,
Manager,
Intern,
Trainer,
TechLead
)

print("===== EMPLOYEE =====")
employee = Employee("Ravi", 30000)
employee.display()
employee.work()

print("\n**** DEVELOPER ****")
developer = Developer("Suresh", 50000)
developer.display()
developer.work()

print("\n===== SENIOR DEVELOPER =====")
senior = SeniorDeveloper("Rahul", 80000)
senior.display()
senior.work()

print("\n**** MANAGER *****")
manager = Manager("Anil", 90000)
manager.display()
manager.work()

print("\n===== INTERN =====")
intern = Intern("Kiran", 15000)
intern.display()
intern.work()

print("\n***** TECH LEAD ****")
tech_lead = TechLead("Arjun", 100000)
tech_lead.display()
tech_lead.work()
tech_lead.train()