import sys

print("=== DEMO PYTHON 3.12.15 ===")
print("Python version:", sys.version)

# 1. Print function
print("1. Print is a function: print(...)")

# 2. Integer division
print("2. 5 / 2 =", 5 / 2, "(Type:", type(5 / 2), ")")

# 3. Strings and Unicode
s = "Привіт"
print("3. Default string type:", type(s), "| Bytes type:", type(b"Hello"))

# 4. Input function
print("4. Function for string input is input()")

# 5. Range output
r = range(3)
print("5. range(3) returns range object:", type(r), "->", r)

# 6. Exception handling syntax
try:
    1 / 0
except ZeroDivisionError as e:
    print("6. Exception syntax 'except Exception as e':", e)

# 7. Dictionary keys
d = {"a": 1, "b": 2}
print("7. dict.keys() returns view object:", type(d.keys()), "->", d.keys())

# 8. Extended Unpacking
a, *b = [1, 2, 3, 4]
print("8. Extended Unpacking supported: a =", a, ", b =", b)

# 9. Incompatible comparison
try:
    1 < "2"
except TypeError as e:
    print("9. Comparison 1 < '2' raises TypeError in Py3:", e)

# 10. Standard library module name
import urllib.request
print("10. Module urllib.request imported successfully")