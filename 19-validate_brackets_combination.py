# -*- coding: utf-8 -*-
"""validate-brackets-combination

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18DlfCU1Rz10x9BpJXzMD-H4-3X1G5EsD
"""

def isValid(s):
  bracket_map = {"(": ")", "[": "]",  "{": "}"}
  open_par = set(["(", "[", "{"])
  stack = []
  for i in s:
    if i in open_par:
        stack.append(i)
    elif stack and i == bracket_map[stack[-1]]:
        stack.pop()
    else:
        return False
  return stack == []

combination = input('Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: ')
print(isValid(combination))