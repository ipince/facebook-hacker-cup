#!/usr/bin/python3

import sys
import math
import operator

from collections import defaultdict
from itertools import combinations

LEFT = 'FX'
RIGHT = 'FO'
MOD = 1_000_000_007

def g(word):
  print(f"processing word of length {len(word)}")
  substrs = [word[x:y] for x, y in combinations(range(len(word) + 1), r = 2)]
  #print(f" substrings are: {substrs}")
  s = 0
  for sub in substrs:
    s = (s + min_switches(sub)) % MOD
  return s

def min_switches(word):

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
  f_word = g(word)

  print('Case #' + str(case+1) + ': ' + str(f_word))
