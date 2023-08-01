# This script contains very small pieces of code that I wanted to try out. Some of them are extremely trivial, however I let them reside here anyway. 

# Function names are so simple and no information-bearing, because they are irrelevant - functions' sole purpose is to enable me to run only the part of the code I am interested in at any given moment.
  # I used to have separate files for learning, checking how things work etc., but that was too messy, and not really convenient whenever I wanted to recall something
  # Also, the location of 'import' statements is so odd due to the nature of that file

# --------------------------------------------------------------------------------------------------------------------------------
def a():
  msg = "Hello World"
  print(msg)
  print("foo\n\n")

  price = 100
  item = "doll"
  print("Product name is " + item + " and its price is " + str(item)) #concatenating strings(!); this way does NOT insert whitespace; one argument to print()
  # >>> print("This will not work because price is not a string:" + item)
    # TypeError: can only concatenate str (not "int") to str
  print("Product name is",item,"and its price is",price) #printing multiple 'items' - multiple arguments; inserts whitespaces - notice the lack of whitespaces after first part and before last part, in the quotes
  print("Product name is {} and its price is {}".format(item, price))
  print(f"Product name is {item} and its price is  {price}")


  for i in range(10):
    print("no newline,i=",i,">>", end='') #no newline!
  print()
  
  for i in range(10):
    print("no newline and no whitespaces inserted,i=",i,">>", sep='', end='') #no newline and no whitespaces inserted
  print()
  
  for i in range(10):
    print("with newline,i=",i,">>") #with newline!
  print('\n\n')

  print("Well would you look at that syntax:", "-separator-".join(["ab","cd","gg","hy"]))

  list=[]
  for i in range(10):
    list.append(str(i))
  print("list:",list)
  print("Well look at that syntax, again!:", "-separator-".join(list)) # list items must be strings

# ----------------------------------------------------------------
# abandoned
def a2_1():
  def print_my_way(method, object): # so I dont have to type twice name and method call 
      print(object+'.'+method.__name__+'():'+method(object))

  somestring = "Chickens have nice feathers."
  print("somestring:",somestring)

  print_my_way(str.upper, somestring) # somestring.upper()
# ----------------------------------------------------------------
def a2_2():
  somestring = "Chickens have nice feathers."
  print(f"somestring: {somestring} \n----")

  print(
     "somestring.upper():",somestring.upper(),'\n'
     "somestring.lower():",somestring.lower(),'\n'
     "somestring.isupper():",somestring.isupper(),'\n'
     "somestring.upper().isupper():",somestring.upper().isupper(),'\n'     
     "len(somestring):",len(somestring),'\n'
     "somestring[5]:",somestring[5],'\n'
     "somestring[5:7]:",somestring[5:7],'\n'
     "somestring.index(\"h\"):",somestring.index("h"),'\n'
     "somestring.index(\"C\"):",somestring.index("C"),'\n'
     "somestring.index(\"c\"):",somestring.index("c"),'\n'
     "somestring.index(\"ave\"):",somestring.index("ave"),'\n'
     "somestring.index(\"ve ni\"):",somestring.index("ve ni"),'\n'
     "somestring.replace(\"a\",\"E\"):",somestring.replace("a","E"),'\n'
     
     )
  
  # print(somestring.index("blu")) won't work, because there is no such string part
# ----------------------------------------------------------------
def b():
  list = [1,2,3]
  list2 = [4,5,6]

  listoflists = [list, list2]

  print(listoflists)
  print(len(listoflists))
# ----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

def c():
  x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
  plt.plot(x, np.sin(x))       # Plot the sine of each x point
  plt.show()                   # Display the plot
# ----------------------------------------------------------------
def d():
  print(5)
  print(5*3)
  number1 = -4
  print("number1:",number1)
  print(
    "abs(number1):",abs(number1),'\n'
    "pow(number1, 3):",pow(number1, 3),'\n'
    "max(number1, pow(number1,3)):",max(number1, pow(number1,3))
  )
  print(
    "round(3.7):",round(3.7),'\n'
    "round(3.2):",round(3.2)
  )  
  
  from math import floor, ceil, sqrt
  print(
    "floor(3.7):",floor(3.7),'\n'
    "floor(3.2):",floor(3.2),'\n'
    "ceil(3.7):",ceil(3.7),'\n'
    "ceil(3.2):",ceil(3.2),'\n'
    "sqrt(81):",sqrt(81)
  )
  # TO DO difference between math that does not need importing, the one that does need, and the numpy (e.g. np.abs and abs - are there any differences in another methods?)

# ----------------------------------------------------------------
def e():
  number1 = input("Enter number1: ")
  number2 = input("Enter number2: ")

  print("number1 + number2 - string concat!:", number1 + number2)
  #this breaks if floats are used
  try:
    print("int(number1)+int(number2):", int(number1)+int(number2))
    print("int(number1+number2):", int(number1+number2))
  except ValueError:
    print("Cannot cast to int, omitting two print statements")
  
  #this works with floats
  print("float(number1)+float(number2)",float(number1)+float(number2))
  try:
    print("float(number1+number2)",float(number1+number2))
  except ValueError:
    print(f"Cannot sensibly cast that string ({number1+number2}) to float")



# ----------------------------------------------------------------
# ----------------------------------------------------------------
code_fragments = {
    'a': a,
    'a2_1':a2_1,
    'a2_2':a2_2,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
  }
# ----------------------------------------------------------------
# Whenever adding new code above, you probably do not care about code below
import sys
def main():
  is_first_iteration = True
  prev_choice = 'does_not_exist' # magic number - flag
  while True:
    if len(sys.argv) > 1 and is_first_iteration:
      choice = sys.argv[1].strip().lower()
      is_first_iteration = False
    else:
      print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-')
      choice = input("Choose preferred code_fragment ('qwqw' to quit, 'agag' for previous choice): ").strip().lower()
      print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-')


    if choice == 'qwqw':
      break
    if choice == 'agag' and choice != 'does_not_exist': #previos choice does exist
      choice = prev_choice

    prev_choice = choice

    if choice in code_fragments:  
      code_fragments[choice]()
    else:
        print("Invalid choice.")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
if __name__ == "__main__": 
  main()

# if script is run as main program, __name__ is assigned "__main__" (there are two underscores)
# should this script be imported by another script (e.g. "import scripto", when this file is "scripto.py" ), the __name__ in scripto.py will be "scripto"