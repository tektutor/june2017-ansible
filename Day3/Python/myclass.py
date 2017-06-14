#!/usr/bin/python

class Calculator:
   
   #This is class member
   count = 0

   def __init__(self):
       print("constructor ...")
      
       Calculator.someFunc(self)
     
       Calculator.count = Calculator.count + 1

       self.x = 0
       self.y = 0
  
       print( "Number of object is ", Calculator.count )

   def getInputs(self):
       self.x = input("Enter your first number : ")
       self.y = input("Enter your second number : ")

   def add(self):
       self.getInputs()
       return self.x + self.y

def main():
    calculator1 = Calculator()
    calculator2 = Calculator()
    calculator3 = Calculator()
    print("The result is ", calculator1.add() )

if __name__ == "__main__":
   main()

