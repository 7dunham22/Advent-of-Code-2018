"""
https://adventofcode.com/2018/day/3#part2

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?
"""

import numpy as np

with open('./inputs/0301.txt') as f:
  data = f.read().strip()

claims = data.split('\n')

fabric = np.zeros((1500,1500), dtype=int)

hasOverlap = [False for i in range(1287)]

def fill(claim):
  mid = claim.index('@')
  id = claim[1:mid-1]
  details = claim[mid+2:]
  [start, dimensions] = details.split(': ')
  [startCol, startRow] = start.split(',')
  [width, length] = dimensions.split('x')
  startCol, startRow, width, length = [int(i) for i in [startCol, startRow, width, length]]
  for r in range(startRow, startRow+length):
    for c in range(startCol, startCol+width):
      if fabric[r][c] != 0:
        hasOverlap[int(id)-1] = True
        hasOverlap[int(fabric[r][c])-1] = True
      else:
        fabric[r][c] = id

for claim in claims:
  fill(claim)

print(hasOverlap.index(False) + 1)
