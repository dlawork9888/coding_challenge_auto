from collections import defaultdict

def solution(participant, completion):
    par_dict = defaultdict(int)
    for par in participant:
        par_dict[par] += 1
    for com in completion:
        par_dict[com] -= 1
    for key in par_dict.keys():
        if par_dict[key] == 1:
            return key