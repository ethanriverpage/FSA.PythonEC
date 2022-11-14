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

foobar()
pythagorea()