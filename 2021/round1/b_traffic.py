#!/usr/bin/python3

import sys
import math
import operator

from collections import defaultdict
from itertools import combinations

LEFT = 'FX'
RIGHT = 'FO'
MOD = 1_000_000_007

def possible(n, m, a, b):
  return a >= n + m - 1 and b >= n + m - 1

def grid(n, m, a, b):
  rows = []
  for i in range(n):
    if i == n - 1:
      k1 = b - n - m + 2
      k2 = a - n - m + 2
      ones_minus_two = " ".join(["1"] * (m-2)) + " "
      rows.append(" ".join([str(k1)] + (["1"] * (m-2)) + [str(k2)]))
    else:
      rows.append(" ".join(["1"] * m))

  return rows

# Input
lines = iter(sys.stdin.readlines())
cases = int(next(lines))
for case in range(cases):
  [n, m, a, b] = map(int, next(lines).strip().split())

  poss = possible(n, m, a, b)
  ans = "Possible" if poss else "Impossible"
  gr = grid(n, m, a, b)

  print(f'Case #{case+1}: {ans}')
  if poss:
    for row in gr:
      print(row)
