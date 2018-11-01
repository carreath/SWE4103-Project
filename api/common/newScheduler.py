import random
from itertools import combinations
from random import shuffle
from common.Scheduler import create_matches


def findNextValid(matchList, dateList):
    try:
        (team1, team2, day)
    except NameError:
        team1 = matchList[0][0]
        team2 = matchList[0][1]
        day = dateList[0][0]
        yield matchList.pop(0), dateList.pop(0)  # init state
    while matchList:
        for idx, i in enumerate(matchList):
            if day == dateList[idx][0] and (team1 in matchList[idx] or team2 in matchList[0]):
                # prevent teams from playing multiple games in one day
                pass
            else:
                team1 = i[0]
                team2 = i[1]
                day = dateList[idx][0]
                matchList.pop(idx)
                yield i, dateList.pop(idx)
        # no optimal date/match pair, use first available match/first available datetime
        team1 = matchList[0][0]
        team2 = matchList[0][1]
        yield matchList.pop(0), dateList.pop(0)


if __name__=="__main__":
    teamList = [5,12,76,13,98,45]  # list of teams
    matchList = create_matches(teamList)
    print(matchList)

    dateList = [1, 1, 1, 3, 4, 4, 5, 6, 6, 8, 9, 9, 9, 10,10]
    print(len(dateList))
    gen = findNextValid(matchList, dateList)
    for i in range(15):
        print(next(gen))


