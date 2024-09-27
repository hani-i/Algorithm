def solution(participant, completion):

    mydic = dict()
    for part in participant:
        mydic[part] = 0
    
    for part in participant:
        mydic[part] +=1
    
    for com in completion:
        mydic[com] -=1
    
    for part in participant:
        if mydic[part] != 0:
            return part