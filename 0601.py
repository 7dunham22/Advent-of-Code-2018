"""
https://adventofcode.com/2018/day/6

The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?
"""

with open('./inputs/0601.txt') as f:
  data = f.read().strip()

coordinates = list(map(lambda x: list(map(lambda x: int(x), x.split(', '))), data.split('\n')))

maxRow = 0
maxCol = 0
for [c, r] in coordinates:
  if r > maxRow:
    maxRow = r
  if c > maxCol:
    maxCol = c

df = [['.' for i in range(maxCol+1)] for i in range(maxRow+1)]
n = len(df)
m = len(df[0])

def fillDistance(R, C):
  for r in range(n):
    for c in range(m):
      dist = abs(R-r) + abs(C-c)
      if df[r][c] == '.' or dist < int(df[r][c]):
        df[r][c] = dist
      elif df[r][c] == dist:
        df[r][c] = str(df[r][c])

def countArea(r, c, prev=-1, visited=set()):
  if r<0 or r==n or c<0 or c==m:
    return float('-inf')
  key = str(r) + ',' + str(c)
  if key in visited or df[r][c] == '.' or df[r][c] != prev+1:
    return 0
  visited.add(key)
  return 1 + countArea(r-1,c,prev+1,visited) + countArea(r+1,c,prev+1,visited) + countArea(r,c-1,prev+1,visited) + countArea(r,c+1,prev+1,visited)

for [c, r] in coordinates:
  fillDistance(r,c)
for r in range(n):
  for c in range(m):
    if isinstance(df[r][c], str):
      df[r][c] = '.'

maxArea = 0
for [c, r] in coordinates:
  area = countArea(r, c)
  if area > maxArea:
    maxArea = area

print(maxArea)
