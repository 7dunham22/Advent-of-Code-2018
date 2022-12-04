"""
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
"""

with open('./inputs/0501.txt') as f:
  data = f.read().strip()

polymers = list(data)

def getLength(polymers):
  res = [polymers.pop()]
  while len(polymers) > 0:
    prev = polymers.pop()
    if prev.lower() == res[-1].lower() and ((prev.islower() and res[-1].isupper()) or (prev.isupper() and res[-1].islower())):
      res.pop()
      if len(res) == 0:
        res.append(polymers.pop())
    else:
      res.append(prev)
  res.reverse()
  return len(''.join(res))

rec = set()
for char in polymers:
  char = char.lower()
  rec.add(char)

minLen = float('inf')
for char in rec:
  filteredChars = list(filter(lambda x: x.lower() != char, polymers))
  reduced = getLength(filteredChars)
  if reduced < minLen:
    minLen = reduced

print(minLen)
