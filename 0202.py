"""
https://adventofcode.com/2018/day/2#part2

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
"""
with open('./inputs/0201.txt') as f:
  data = f.read().strip()

boxes = data.split('\n')

def evaluate(a, b):
  diff = 0
  res = ""
  for i in range(len(a)):
    if a[i] == b[i]:
      res += a[i]
    else:
      diff += 1
      if diff > 1:
        return ""
  return res

boxes = sorted(boxes, key=str.lower)

for i in range(1, len(boxes)):
  common = evaluate(boxes[i-1], boxes[i])
  if len(common) > 0:
    print(common)
    break
