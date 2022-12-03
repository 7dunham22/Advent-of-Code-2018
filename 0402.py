"""
Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 99 * 45 = 4455.)
"""
from datetime import datetime
from functools import reduce

with open('./inputs/0401.txt') as f:
  data = f.read().strip()

observations = data.split('\n')

class Entry:
  def __init__(self, observation, year, month, day, hour, minute) -> None:
    self.observation = observation
    self.date = datetime(year, month, day, hour, minute)

def convert(entry):
  [temp, observation] = entry.split('] ')
  temp = temp[1:]
  [date, time] = temp.split(' ')
  [year, month, day] = date.split('-')
  [hour, minute] = time.split(':')
  return Entry(observation, int(year), int(month), int(day), int(hour), int(minute))

observations = list(map(convert, observations))
observations = sorted(observations, key=lambda x: x.date)

sleepRecord = {}

def fillRecord(guardID, startSleep, endSleep):
  guardRec = sleepRecord[guardID]
  minsAsleep = int((endSleep - startSleep).total_seconds() // 60)
  min = startSleep.minute
  for i in range(minsAsleep):
    guardRec[min] += 1
    min = (min+1)%60
  sleepRecord[guardID] = guardRec

currGuard = None
startAwake = None
startSleep = None
for obs in observations:
  text = obs.observation
  if 'Guard' in text:
    if startSleep:
      fillRecord(currGuard, startSleep, obs.date)
    guardID = text.split(' ')[1]
    currGuard = guardID
    startAwake = obs.date
    startSleep = None
    if guardID not in sleepRecord:
      sleepRecord[guardID] = [0 for i in range(60)]
  elif 'asleep' in text:
    startAwake = None
    startSleep = obs.date
  else:
    fillRecord(currGuard, startSleep, obs.date)
    startSleep = None
    startAwake = obs.date

resGuard = None
mostFreqMinute = 0
minsAsleep = 0
for guard in sleepRecord:
  guardRec = sleepRecord[guard]
  for i in range(len(guardRec)):
    if guardRec[i] > minsAsleep:
      minsAsleep = guardRec[i]
      resGuard = guard
      mostFreqMinute = i

print(int(resGuard[1:]) * mostFreqMinute)
