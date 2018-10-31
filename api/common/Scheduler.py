from itertools import combinations
import random
from random import shuffle

def rotate(n):
    return n[1:] + n[:1]


def create_matches(team_ids):
    num_teams = len(team_ids)
    matches = []
    if num_teams % 2 == 0:
        for i in range(num_teams-1):
            for j in range(num_teams // 2):
                matches.append((team_ids[j], team_ids[num_teams-1-j]))
            constant = team_ids[0]
            team_ids.pop(0)
            team_ids = rotate(team_ids)
            team_ids = [constant] + team_ids

    else:
        for i in range(num_teams-1):
            for j in range(num_teams // 2):
                matches.append((team_ids[j], team_ids[num_teams-2-j]))
            team_ids = rotate(team_ids)

    return matches