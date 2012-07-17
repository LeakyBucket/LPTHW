import re
import inspect
import os
import sys
from sets import Set
files = ["ex1/ex1.py", "ex10/ex10.py", "ex11/ex11.3.py", "ex11/ex11.py", "ex12/ex12.py", "ex13/ex13.1.py", "ex13/ex13.2.py", "ex13/ex13.3.py", "ex13/ex13.py", "ex14/ex14.py", "ex15/ex15.py", "ex16/ex16.1.py", "ex16/ex16.py", "ex17/ex17.py", "ex18/ex18.py", "ex19/ex19.py", "ex2/ex2.py", "ex20/ex20.py", "ex21/ex21.py", "ex22/test.py", "ex24/ex24.py", "ex3/ex3.py", "ex4/ex4.py", "ex5/ex5.py", "ex6/ex6.py", "ex7/ex7.py", "ex8/ex8.py", "ex9/ex9.py", "test.py"]
method = Set([])
variable = Set([])
key_word = Set([])
method_match = re.compile('\s*(\w*?)\(|\.(\w*?)\(')
variable_match = re.compile('\s*(\w*?)\s?=|[(|\s](\w*?)[,|)]')
key_word_match = re.compile('(?<!")\s*(\w*?)\s(?!=)|(?!=")')
for file in files:
  target = open(file)
  for line in target.readlines():
    if (line[0] != '#'):
      if (method_match.search(line) is not None):
        method.add(method_match.search(line).group().strip())
      if (variable_match.search(line) is not None):
        variable.add(variable_match.search(line).group().strip())
      if (key_word_match.search(line) is not None):
        key_word.add(key_word_match.search(line).group().strip())
print "Here are the Methods: %r" % (method)
print "\n"
print "Here are the Variables: %r" % (variable)
print "\n"
print "Here are the Key Words: %r" % (key_word)
