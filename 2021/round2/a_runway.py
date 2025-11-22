#!/usr/bin/python3

import sys
import math
import operator

from collections import defaultdict

def min_switches(n, m, P):
  #S = sorted(S)
  #P = map(sorted, P)
  print(f"Solving for {n} rounds, {m} models, and P of {P}")
  #print(" ".join(map(str,S)))
  print("\n".join(map(str,P)))
  ds = 0
  maxTricks = m # max number of times we can avoid a diff
  usedTricks = 0 # number of times we actually avoided a diff
  for i in range(len(P)):
    #print(f"Comparing rows {i} and {i+1}")
    if i+1 < len(P):
      d = diff(P[i], P[i+1])
      tricksLeft = maxTricks - usedTricks
      print(f"Diff between {P[i]} and {P[i+1]} is {d}. {tricksLeft} tricks remain")
      if tricksLeft < d:
        d = d - tricksLeft
        usedTricks += tricksLeft
      else: # more tricks left than diffs
        usedTricks = d
        d = 0
      print(f"  used {usedTricks} in total so far")
      ds += d

  return ds

def diff(row1, row2):
  i = 0
  j = 0
  diffs = 0
  eqs = 0
  while True:
    if i >= len(row1) or j >= len(row2):
      break
    if row1[i] == row2[j]:
      eqs += 1
      i += 1
      j += 1
    elif row1[i] < row2[j]:
      diffs += 1
      i += 1
    elif row1[i] > row2[j]:
      diffs += 1
      j += 1
  return len(row1) - eqs


# Input
lines = iter(sys.stdin.readlines())
cases = int(next(lines))
for case in range(cases):
  [n, m] = map(int, next(lines).strip().split())
  P = [sorted(list(map(int, next(lines).strip().split())))]
  for i in range(n):
    P.append(sorted(list(map(int, next(lines).strip().split()))))

  print(f"Case #{(case+1)}: {str(min_switches(n, m, P))}")
