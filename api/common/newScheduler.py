import random
from itertools import combinations
from random import shuffle

teamList = [5,12,76,13,98,45]
teamMap = {teamList[i]: i for i in range(0,len(teamList))}
anonTeamList = [i for i in range(0,len(teamList))]
matchList = [c for c in combinations(anonTeamList, 2)]
shuffle(matchList)

def findNextValid(matchList):
    try:
        (team1, team2)
    except NameError:
        team1 = matchList[0][0]
        team2 = matchList[0][1]
        yield matchList.pop(0)
    while matchList:
        for idx, i in enumerate(matchList):
            if team1 in i or team2 in i:
                pass
            else:
                team1 = i[0]
                team2 = i[1]
                matchList.pop(idx)
                yield i
        team1 = matchList[0][0]
        team2 = matchList[0][1]
        yield matchList.pop(0)


gen = findNextValid(matchList)
for i in range(15):
    print(next(gen))
print(next(gen))


