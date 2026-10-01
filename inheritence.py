""""
In Python Inheritance is a object Oriented Programming Feature that allows one class to acquire the properties and methods of another class
Types of Inheritance In Python
1. Single
    Parent → Child
2. Multilevel
    Grandparent → Parent → Child
3. Multiple
    Parent1 + Parent2 → Child
4. Hierarchical Inheritance
     Parent
    /     \
 Child1 Child2
 5. Hybrid
    Combination of two or more inheritance types
"""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
    def work(self):
        print("Employee is Working")
class Developer(Employee):
    def work(self):#method Overriding
        print("Developer is writing code")
class SeniorDeveloper(Developer):
    def work(self):
        print("Senior Developer is designing and reviewing code")
class Manager(Employee):
    def work(self):
        print("Manager is managing the team")
class Intern(Employee):
    def work(self):
        print("Intern is learning and assisting the team")
class Trainer:
    def train(self):
        print("Trainer is conducting technical training")
class TechLead(Employee,Trainer):
    def work(self):
        print("Tech Lead is developing and leading the team")

