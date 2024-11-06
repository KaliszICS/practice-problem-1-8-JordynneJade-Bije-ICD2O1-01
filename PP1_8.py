def q1():
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  integer = input("Enter an integer: ")
  integer = int(integer)
  bool1 = integer != 0
  print(bool1)

def q3():
  number = input("Enter a number: ")
  number = float(number)
  number = number >= 0 and number <= 10
  print(number)

def q4():
  food = input("Input food: ")
  drink = input("Input drink: ")
  bool1 = food != "pizza" or drink != "pop"
  print(bool1)

def q5():
  integer = input("Enter an integer: ")
  integer = int(integer)
  num = integer % 2
  bool1 = num == 0
  print(f"The integer {integer} is {bool1}.")

#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()
