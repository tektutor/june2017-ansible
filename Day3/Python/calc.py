#!/usr/bin/python

def addNumbers(firstInput, secondInput):
    return firstInput + secondInput

def main():
   a = input("Enter any number: ")
   b = input("Enter any number: ")
  
   print("Type of a is ", type(a) )
   print("Type of b is ", type(b) )
   print( "The sum of ", a, " and ", b, " is ", addNumbers( a, b ) )
  
   a = "hello"
   print("Type of a is ", type(a) )
   b = 1.000034343;
   print("Type of b is ", type(b) )

if __name__ == "__main__":
   main()
