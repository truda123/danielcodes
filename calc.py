import os
import time
import math
#Version 4.0
welcome = """
   _       _                               _     ___      _            _       _                     _  _    ___  
  /_\   __| |_   ____ _ _ __   ___ ___  __| |   / __\__ _| | ___ _   _| | __ _| |_ ___  _ __  __   _| || |  / _ \ 
 //_\\ / _` \ \ / / _` | '_ \ / __/ _ \/ _` |  / /  / _` | |/ __| | | | |/ _` | __/ _ \| '__| \ \ / / || |_| | | |
/  _  \ (_| |\ V / (_| | | | | (_|  __/ (_| | / /__| (_| | | (__| |_| | | (_| | || (_) | |     \ V /|__   _| |_| |
\_/ \_/\__,_| \_/ \__,_|_| |_|\___\___|\__,_| \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|      \_/    |_|(_)___/ 
                                                                                                                  
 __    __     _                                                                                                   
/ / /\ \ \___| | ___ ___  _ __ ___   ___                                                                          
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \                                                                         
 \  /\  /  __/ | (_| (_) | | | | | |  __/                                                                         
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|                                                                         
                                                        
"""
print(welcome)
time.sleep(1.5)
ans = "Your answer is"
def add(num):
   #addition
    sum = 0
    for n in num:
        sum = sum + n

    print(ans,sum)

    time.sleep(1.5)#Pauses so the user can read
    os.system('cls')#Clears the screen
def subtract(num):
    diff = 0
    for n in num:
        diff = diff - n

    print(ans,diff)

    time.sleep(1.5)#Pauses so the user can read
    os.system('cls')#Clears the screen
while 1==1:#while loop(1 always equals to 1)
   print("-------------------------------------------------------------------")
   print("Options:")
   print("Enter '+' to add two numbers")
   print("Enter '-' to subtract two numbers")
   print("Enter 'x' to multiply two numbers")
   print("Enter '/' to divide two numbers")
   print("Enter '//' to floor divide to numbers")
   print("Enter '%' to use the modulus operation")
   print("Enter '^' to use the exponent operation")
   print("Enter 'sqrt' to use the square root operation")
   print("Enter 'fact' to use the factorial operation")
   print("Enter 'abs' to find absolute value")
   print("Enter 'sine' to find the sine of x")
   print("Enter 'cos' to find the cosine of x")
   print("Enter 'tan' to find the tangent of x")
   print("Enter 'exit' to end the program")
   print("-------------------------------------------------------------------")
   user_input = input("Enter your choice: ")

   if user_input == "exit":
      break
   elif user_input == "+":
   #addition
     values = input("Input some comma seprated numbers : ")
     nums = values.split(",")
     nums = (map(int, nums)) 
     add(nums)
   elif user_input == "-":
   #subtraction
    values = input("Input some comma seprated numbers : ")
    nums = values.split(",")
    nums = (map(int, nums)) 
    subtract(nums)
   elif user_input == "x":
   #multiplication
    os.system('cls')#clears the screen
    x = float(input("Enter a number: "))#prompt 
    y = float(input("Enter another number: "))#prompt 
    print ((x)*(y))#prints answer
    time.sleep(1.5)#pause so the user can read
    os.system('cls')#clears the screen
   elif user_input == "/":
   #division
    os.system('cls')#clears the screen 
    x = float(input("Enter a number: "))#prompt
    y = float(input("Enter another number: "))#prompt
    print ((x)/(y))#prints answer
    time.sleep(1.5)#pauses so the user can read
    os.system('cls')
   elif user_input == "//":
   #floor division
    os.system('cls')#it works the same way just with different operators
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print ((x)//(y))
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "%":
   #modulus
    os.system('cls')#it works the same way just with different operators
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print ((x)%(y))
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "^":
   #exponent
    os.system('cls')#it works the same way just with different operators
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    print (math.pow(x,y))
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "sqrt":
   #square root
    os.system('cls')#clears the screen
    x = float(input("Enter a number: "))#prompt
    print(math.sqrt(x))#prints answer
    time.sleep(1.5)#pauses so the user can read
    os.system('cls')#clears the screen
   elif user_input == "fact":
   #factorial
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    print(math.factorial(x))
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "abs":
   #Absolute value
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    print(abs(x))
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "sine":
   #Sine
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    print(math.sin(x))
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "cos":
   #Sine
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    print(math.cos(x))
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "tan":
   #tangent
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    print(math.tan(x))
    time.sleep(1.5)
    os.system('cls')
   else:
   #exception
      print("Invalid input")
      time.sleep(1.5)
      os.system('cls')


