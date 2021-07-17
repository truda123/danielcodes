import os
import time
import math
import playsound
import speech_recognition as sr
from gtts import gTTS

filenum = 0#Creates a file name
def getFilename():#Define function
    global filename, filenum #makes variables global
    filenum = 1#sets filenum to 1
    file = f"voice{filenum}.mp3"#creates filename
    return file#returns file

def speak(text):#Define function
    global filenum, filename
    tts = gTTS(text=text, lang="en")#'speaks' the text
    filename = getFilename()#get file name
    tts.save(filename)#saves mp3
    playsound.playsound(filename)#Plays the sound

ans = "Your answer is"#text
#Version 3.0
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
    os.system('cls')#Clears the screen 
    y = float(input("Enter a number: "))#Prompt 
    x = float(input("Enter another number: "))#Prompt
    z = str(x + y)#converts int to str
    speak(ans + z)#speaks answer
    time.sleep(1.5)#Pauses so the user can read
    os.system('cls')#Clears the screen
   elif user_input == "-":
   #subtraction
    os.system('cls')#clears the screen
    x = float(input("Enter a number: "))#prompt 
    y = float(input("Enter another number: "))#prompt 
    z = str(x - y)#converts int to str
    speak(ans + z)#speaks answer
    time.sleep(1.5)#pause so the user can read
    os.system('cls')#clears the screen
   elif user_input == "x":
   #multiplication
    os.system('cls')#clears the screen
    x = float(input("Enter a number: "))#prompt 
    y = float(input("Enter another number: "))#prompt 
    z = str(x * y)#converts int to str
    speak(ans + z)#speaks answer
    time.sleep(1.5)#pause so the user can read
    os.system('cls')#clears the screen
   elif user_input == "/":
   #division
    os.system('cls')#clears the screen 
    x = float(input("Enter a number: "))#prompt
    y = float(input("Enter another number: "))#prompt
    z = str(x / y)#converts int to str
    speak(ans + z)#speaks answer
    time.sleep(1.5)#pauses so the user can read
    os.system('cls')#clears the scrren
   elif user_input == "//":
   #floor division
    os.system('cls')#it works the same way just with different operators
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    z = str(x // y)#converts int to str
    speak(ans + z)#speaks answer
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "%":
   #modulus
    os.system('cls')#it works the same way just with different operators
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    z = str(x % y)#converts int to str
    speak(ans + z)#speaks answer
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "^":
   #exponent
    os.system('cls')#it works the same way just with different operators
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    z = str(x ** y)#converts int to str
    speak(ans + z)#speaks answer
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "sqrt":
   #square root
    os.system('cls')#clears the screen
    x = float(input("Enter a number: "))#prompt
    z = str(math.sqrt(x))#converts int to str
    speak(ans + z)
    time.sleep(1.5)#pauses so the user can read
    os.system('cls')#clears the screen
   elif user_input == "fact":
   #factorial
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    z = str(math.factorial(x))#converts int to str
    speak(ans + z)
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "abs":
   #Absolute value
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    z = str(abs(x))#converts int to str
    speak(ans + z)
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "sine":
   #Sine
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    z = str(math.sin(x))#converts int to str
    speak(ans + z)
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "cos":
   #Sine
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    z = str(math.cos(x))#converts int to str
    speak(ans + z)
    time.sleep(1.5)
    os.system('cls')
   elif user_input == "tan":
   #tangent
    os.system('cls')#the same as above
    x = float(input("Enter a number: "))
    z = str(math.tan(x))#converts int to str
    speak(ans + z)
    time.sleep(1.5)
    os.system('cls')
   else:
   #exception
      print("Invalid input")
      time.sleep(1.5)
      os.system('cls')



