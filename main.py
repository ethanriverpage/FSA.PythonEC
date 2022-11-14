import math
from fibo import fib
import sys

def foobar():
    file_path = './foobar.txt'
    with open(file_path,"r") as file:
        input = file.read()
        print(input)
        #input = input.replace(',','\n')
        #print(input)
        file.close()

def pythagorea():
    a = float(input("Input side A: "))
    b = float(input("Input side B: "))
    
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"The length of the hypotenuse c is {c}")

def fibonacci():
    power = int(input("Fibonacci to what power?"))
    print(fib(power))

def systest():
    print("What is your name?")
    name = sys.stdin.readline()
    print("What is your age?")
    age = sys.stdin.readline()
    print("...")
    print("...")
    print("Name: " + name + "Age: " + age)

def whiletest():
    while True:
        whiletest_input = int(input("Pick a number. "))
        if whiletest_input >= -1:
            whiletest_input = whiletest_input - 5
            print(whiletest_input)
        elif whiletest_input < -1:
            print(str(whiletest_input) + " is the final number. Goodbye.")
            break
        else:
            return 1

print("sys input test")
systest()
print("Fibonacci test")
fibonacci()
print("Foobar test")
foobar()
print("Pythagorean theorum test")
pythagorea()
print("while test")
whiletest()

print("This is the end.")