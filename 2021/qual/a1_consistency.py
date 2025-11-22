#!/usr/bin/python

import sys
import math
import operator

from collections import defaultdict

VOWELS = 'AEIOU'

def min_moves(s):
  #print s
  vowels = defaultdict(int)
  consonants = defaultdict(int)
  for c in s:
    if c in VOWELS:
      vowels[c] += 1
    else:
      consonants[c] += 1
  vcount = sum(vowels.values())
  ccount = sum(consonants.values())
  #print vowels
  #print consonants
  vtarget = max(vowels.iteritems(), key=operator.itemgetter(1))[0] if len(vowels) > 0 else None
  ctarget = max(consonants.iteritems(), key=operator.itemgetter(1))[0] if len(consonants) > 0 else None
  #print vtarget
  #print ctarget

  vscore = ccount + 2 * (vcount - vowels[vtarget])
  cscore = vcount + 2 * (ccount - consonants[ctarget])
  return min(vscore, cscore)

# Input
lines = iter(sys.stdin.readlines())
cases = int(lines.next())
for case in range(cases):
  word = lines.next().strip()
  m = min_moves(word)

  print 'Case #' + str(case+1) + ': ' + str(m)
