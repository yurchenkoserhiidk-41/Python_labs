# -*- coding: utf-8 -*-
import sys

print "=== DEMO PYTHON 2.7.18 ==="
print "Python version:", sys.version

# 1. Print statement
print "1. Print statement without parentheses works!"

# 2. Integer division
print "2. 5 / 2 =", 5 / 2, "(Type:", type(5 / 2), ")"

# 3. Strings and Unicode
s = "Привіт"
print "3. Default string type:", type(s), "| Unicode type:", type(u"Привіт")

# 4. Input function
print "4. Function for string input is raw_input()"

# 5. Range output
r = range(3)
print "5. range(3) returns list:", type(r), "->", r

# 6. Exception handling syntax
try:
    1 / 0
except ZeroDivisionError, e:
    print "6. Exception syntax 'except Exception, e':", e

# 7. Dictionary keys
d = {"a": 1, "b": 2}
print "7. dict.keys() returns list:", type(d.keys()), "->", d.keys()

# 8. Extended Unpacking
print "8. Extended Unpacking (a, *b = ...) is NOT supported in Python 2"

# 9. Incompatible comparison
print "9. Comparison 1 < '2' works in Py2:", 1 < "2"

# 10. Standard library module name
import urllib2
print "10. Module urllib2 imported successfully"