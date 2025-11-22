#!/usr/bin/python3

import sys
import math
import operator

from collections import defaultdict

LEFT = 'FX'
RIGHT = 'FO'

def min_switches(word):
  #print(word)

  switches = 0
  current = None
  for i in word:
    #print(f"current is: {current}")
    if not current:
      if i in LEFT and i not in RIGHT:
        current = 'L'
      elif i in RIGHT and i not in LEFT:
        current = 'R'
      else: # i is in both hands... continue without doing anything
        pass
    else:
      if i in LEFT and i not in RIGHT and current == 'R':
        #print(f"at {i}, switching from {current}")
        current = 'L'
        switches += 1
      elif i in RIGHT and i not in LEFT and current == 'L':
        current = 'R'
        switches += 1

  return switches

# Input
lines = iter(sys.stdin.readlines())
cases = int(next(lines))
for case in range(cases):
  n = int(next(lines).strip())
  word = next(lines).strip()
  f_word = min_switches(word)

  print('Case #' + str(case+1) + ': ' + str(f_word))
