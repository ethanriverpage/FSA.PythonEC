# Sample Python programs

> This was done as part of an assessment for Fullstack Academy, used to test knowledge of writing Python, managing libraries, among others.

#### 1. Sys library usage test (`systest()`)
Demonstrates the usage of the 'sys' library in python to read user input.
#### 2. Fibonacci test (`fibonacci()`)
Imports a library for the fibonacci sequence and allows user specified power to calculate of the Fibonacci sequence.
#### 3. Foobar test (`foobar()`)
Used to demonstrate accessing, writing, and manipulating files in Python
#### 4. Pythagorean theorum calculator (`pythagorea()`)
Demonstrates using floats and mathematics within Python
#### 5. While loop test (`whiletest()`)
Demonstrates loops within programming and how to utilize them

### Python mitigation explanation

Python mitigation is the idea of avoiding security vulnerabilities within Python and using Python itself to avoid those vulnerabilities.

For example, a Python function like `eval()` is dangerous, and unless handled very precisely, could be used for evil through unsanitized user inputs. Sanitizing user inputs is crucial to preventing RCEs and other exploits like [SQL injection!](https://en.wikipedia.org/wiki/SQL_injection) Bad news for someone running a website, for example. Python also has tools written for it like [Bandit](https://bandit.readthedocs.io/en/latest/), that are designed to look at static code and search for security vulnerabilities. 
