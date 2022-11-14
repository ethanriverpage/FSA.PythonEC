# FSA.PythonEC

## Python mitigation

Python mitigation is the idea of avoiding security vulnerabilities within Python and using Python itself to avoid those vulnerabilities.

For example, a Python function like `eval()` is dangerous, and unless handled very precisely, could be used for evil through unsanitized user inputs. Sanitizing user inputs is crucial to preventing RCEs and other exploits like [SQL injection!](https://en.wikipedia.org/wiki/SQL_injection). Bad news for someone running a website, for example. Python also has tools written for it like [Bandit](https://bandit.readthedocs.io/en/latest/), that are designed to look at static code and search for security vulnerabilities. 