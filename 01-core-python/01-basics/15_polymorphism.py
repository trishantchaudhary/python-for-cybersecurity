# oops is way of programming which matchs real world things
# like till now we have done procedural programming line by line
# but with oops we can reduce redundancy adn improve reuseablity of code
# can make much more clean code ok 



# 1. polymorphism : polymorphishm means same method name but different
# behaviour for differnt objects


class Nmap:
    def scan(self):
        print("scannning the network")


class Burpsuite:
    def scan(self):
        print("scanning web applications")


tool1 = Nmap()
tool2 = Burpsuite()

tool1.scan() # ------- scannning the network
tool2.scan() # -------- scanning web applications


# types 
# compile-time polymorphism ---- method overloading
# runtime polymorphism ----- method overriding


#1 compile time or method overloading

# when methods have same name but they work with differnet arguement called overloading
# but python doesnt support tradiotnal overloading directly like c++/java
# we achieve this via default arguements or *args 

class Calculator:
    def add(self, *numbers):
        return sum(numbers)

c = Calculator()

print(c.add(10,20))
print(c.add(10,20,30))
print(c.add(10,20,40,50))


# 2. runtime or overiding method

# when child class  defines parent class methods in their own way with same name
# called method overiding


class Scanner:
    def scan(self):
        print("basic security scan")

class Webscanner(Scanner):
    def scan(self):
        print("redifing it in my own way")


class Scancom(Scanner):
    def scan(self):
        print("scan about to complete")


s1 = Scanner()
s2 = Webscanner()
s3 = Scancom()

s1.scan()
s2.scan()
s3.scan()

    