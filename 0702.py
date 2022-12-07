"""
As you're about to begin construction, four of the Elves offer to help. "The sun will set soon; it'll go faster if we work together." Now, you need to account for multiple people working on steps simultaneously. If multiple steps are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and that each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the same instructions as above, this is how each second would be spent:

Second   Worker 1   Worker 2   Done
   0        C          .
   1        C          .
   2        C          .
   3        A          F       C
   4        B          F       CA
   5        B          F       CA
   6        D          F       CAB
   7        D          F       CAB
   8        D          F       CAB
   9        D          .       CABF
  10        E          .       CABFD
  11        E          .       CABFD
  12        E          .       CABFD
  13        E          .       CABFD
  14        E          .       CABFD
  15        .          .       CABFDE
Each row represents one second of time. The Second column identifies how many seconds have passed as of the beginning of that second. Each worker column shows the step that worker is currently doing (or . if they are idle). The Done column shows completed steps.

Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these steps.

With 5 workers and the 60+ second step durations described above, how long will it take to complete all of the steps?
"""
with open('./inputs/0701.txt') as f:
  data = f.read().strip()

rules = data.split('\n')

pairs = []
for rule in rules:
  words = rule.split(' ')
  pairs.append([words[1], words[7]])

def getNextSteps(steps, pairs):
  nextSteps = sorted([step for step in steps if all(s != step for prereq, s in pairs)])
  return nextSteps

def calculateStepTime(s):
  return (ord(s) - ord('A') + 1) + 60

steps = set([s for steps in pairs for s in steps])
workers = [{"step": None, "time": 0} for i in range(5)]

time = -1
while steps or any(w['time'] > 0 for w in workers):
  for w in workers:
    w["time"] = max(w['time'] - 1, 0)
    if w['time'] == 0:
      if w['step'] != None:
        pairs = [[prereq, s] for [prereq, s] in pairs if prereq != w['step']]
        w['step'] = None
      nextSteps = getNextSteps(steps, pairs)
      if nextSteps:
        step = nextSteps.pop()
        w['time'] = calculateStepTime(step)
        w['step'] = step
        steps.discard(step)
  time += 1

print(time)
