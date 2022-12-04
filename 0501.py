"""
https://adventofcode.com/2018/day/5

You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned?
"""

with open('./inputs/0501.txt') as f:
  data = f.read().strip()

polymers = list(data)
res = [polymers.pop()]

while len(polymers) > 0:
  # print('polymers: ', polymers)
  # print('res: ', res)
  # print('====')
  prev = polymers.pop()
  if prev.lower() == res[-1].lower() and ((prev.islower() and res[-1].isupper()) or (prev.isupper() and res[-1].islower())):
    res.pop()
    if len(res) == 0:
      res.append(polymers.pop())
  else:
    res.append(prev)
res.reverse()
print(len(''.join(res)))
