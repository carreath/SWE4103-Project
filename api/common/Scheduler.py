from itertools import combinations
import random
from random import shuffle

teamList = [1,2,3,4,5,6,7,8]
timeList = [6,7,8,9]
dayList = [1,2,4,7,8,9,12,15,18]  # placeholder for different days with available times
datetimeList = [(d, random.choice(timeList)) for d in dayList] # assume these are also mapped to fields
# TODO make a dummy dataset with enough game slots for the whole league to play each other at least once
weekList = [int(i/7) for i in dayList]  # assign week numbers to days
teamTimeWeights = {}
teamWeekWeights = {}
for t in teamList:
    teamTimeWeights[t] = [{timeList[i]: 1} for i in range(len(timeList))]  # for tracking if a team has played a lot of games in a given timeslot
    teamWeekWeights[t] = [{list(set(weekList))[i]: 1} for i in range(len(set(weekList)))]  # for tracking if a team has played in a given week
pairList = []
for comb in combinations(teamList, 2):
    pairList.append(comb)  # pairs of team matchups
shuffle(pairList)
print(pairList)
print(datetimeList)
#TODO will need to duplicate pairs in pair list to meet game requirements
assignList = {}

while datetimeList:
    x = pairList.pop(0)
    assignList[x] = datetimeList.pop(0) #TODO implement week and time weightings
