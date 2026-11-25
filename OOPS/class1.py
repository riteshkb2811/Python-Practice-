from abc import ABC,abstractmethod

# self refers to the current object; a and b must be set before add() is called.
class cmp:
    def add(self):
        print(self.a+self.b)

# Create an instance, call its method, and display its type.
obj=cmp()
obj.add()
print(type(obj))


# Store details separately on each laptop object using self.
class laptop:
    def details(self,brand,ram):
        self.brand=brand
        self.ram=ram
        print(self.brand,self.ram)
obj1=laptop()
obj2=laptop()
obj1.details("HP",8)
obj2.details("DELL",16)
print(id(obj1))
print(id(obj2 ))


# __init__ runs when a car is created and saves data on that instance.
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def details(self):
        print(self.brand,self.model)

ob1=car("BMW","X5")
ob2=car("AUDI","A6")
ob1.details()   
ob2.details()  

# A subclass inherits methods from its parent class.
class abc:
    def ab(self):
        print("ab")
    def cd(self):
        print("Cd")
class de(abc):
     def st(self):
         print("st")
     def rm(self):
         print("rm")

obj1=de()
obj1.ab()
obj1.rm()


# super() calls the parent constructor before the child constructor continues.
class xyz:
    def __init__(self):
        print("Constructor A")
    def abc(self):
        print("Method A")
class pqr(xyz):
    def __init__(self):
        super().__init__()
        print("Constructor B")
    def bcq(self):
        print("Method B")

obj1=pqr()
obj1.abc()


# These objects share a built() method name, though each class has its own behavior.
class laptop:
    def built(self):
        print("laptop Built")
class desktop:
    def built(self):
        print("desktop Built")
class computer:
    def built(self,obj):
        print("Computer Built")
obj1=laptop()
obj2=desktop()
obj3=computer()
obj3.built(obj1)
obj3.built(obj2)
print(obj3.__sizeof__())


# B overrides A's show() method; the object's class determines which one runs.
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
obj6=B()
obj6.show()   


# Payment processes any gateway object that provides a pay() method.
class Razorpay:
    def pay(self):
        print("Razerpay Payment Done")

class Paytm:
    def pay(self):
        print("Paytm Payment Done")

class payment:
    def __init__(self,method):
        self.method=method
    
    def process(self):
        print("Payment Processed") 
        self.method.pay()

gateway1=Razorpay()
gateway2=Paytm()
payment1=payment(gateway1)
payment2=payment(gateway2)
payment1.process()
payment2.process()