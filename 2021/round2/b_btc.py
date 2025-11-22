#!/usr/bin/python3

import sys
import math
import operator
import random

from collections import defaultdict
from collections import deque

def block(n, edges, freqs):
  #print(f"Edges are: {edges}\n Freqs are: {freqs}")
  fgroups = defaultdict(set)
  for i, f in enumerate(freqs):
    fgroups[f].add(i+1)
  #print(f"Edges are: {edges}\n Freqs are: {fgroups}")

  unblockable = set()
  for f in fgroups:
    #print(f"Expanding frequency {f}")
    if len(fgroups[f]) == 1:
      #print("  skipping lone plant")
      continue

    for start in fgroups[f]:
      #print(f"starting to explore paths beginning in {start}")
      expand(edges, fgroups, f, [start], start, set([start]), unblockable)
      #print(f"finished exploring paths beginning in {start}. unblockables are: {unblockable}")

  # compute blockable edges
  blocks = 0
  for src, dst in edges.items():
    for d in dst:
      if (src, d) not in unblockable:
        blocks += 1

  return int(blocks / 2)  # double counting

def expand(edges, freqs, f, path, current, seen, unblockable):
  # returns paths whose edges cannot be blocked.
  #print(f"{edges}, {freqs}, {f}, {path}, {current}, seen: {seen}, unblockable: {unblockable}")
  seen.add(current)
  nexts = deque()
  if current in edges: # has a path out of it
    for n in edges[current]:
      if len(path) < 2 or n != path[-2]:
        nextp = path.copy()
        nextp.append(n)
        nexts.append(nextp)

  #print(f"nexts: {nexts}")
  while nexts: # list of paths to check
    path = nexts.popleft()
    current = path[-1]
    if current in seen:
      continue # ignore path that ends in plant we've already seen

    # terminating condition: did we arrive at a plant in same frequency?
    if len(path) > 1 and current in freqs[f]:
      # if so, save the path and then keep going.
      #print(f"  went from {path[0]} to {current} in same freq. saving path {path}")
      for i in range(len(path)):
        if i < len(path) - 1:
          unblockable.add((path[i], path[i+1]))

    # expand the path and add to nexts
    seen.add(current)
    if current in edges: # has a path out of it
      for n in edges[current]:
        if len(path) < 2 or n != path[-2]:
          nextp = path.copy()
          nextp.append(n)
          nexts.append(nextp)


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


def large_input():
  print(1)
  N = 800000
  n = random.randrange(2, N)
  print(n)
  for i in range(n-1):
    print(f"{random.randrange(1, n)} {random.randrange(1, n)}")
  fs = []
  for i in range(n):
    fs.append(str(random.randrange(1, n)))
  print(" ".join(fs))

#large_input()
#sys.exit()

# Input
lines = iter(sys.stdin.readlines())
cases = int(next(lines))
for case in range(cases):
  n = int(next(lines).strip())
  edges = defaultdict(list)
  freqs = []
  for i in range(n):
    if i < n - 1:
      edge = list(map(int, next(lines).split()))
      edges[edge[0]].append(edge[1])
      edges[edge[1]].append(edge[0])
    else: # last row
      freqs = list(map(int, next(lines).split()))

  print(f"Case #{(case+1)}: {str(block(n, edges, freqs))}")
