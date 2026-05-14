#Inheritance is a fundamental concept in (OOP) that allows a class 
# to inherit attributes and methods from another class


class Scanner:
    def scan(self):
        print("Scanning the target")


class Webscanner(Scanner):
    def test_vuln(self):
        print("testing web vulnerbalities")


s = Webscanner
s.scan()
s.test_vuln()

# this means child class can reuse parent methods and can make their own
# methods too

# super() keyword ka use child class ke ander parent class ke method ya constructor ko call krne ke liye hota hai


class Father:
    def hello(self):
        print("hello from father")

class Son(Father):
    def hello(self):
        super().hello()
        print("hello from son")


s = Son()
s.hello()


# method overiding in inheritance
# Child class parent ke method ko same naam se dobara define karti hai.

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()

