def solution(participant, completion):
    participant.sort()
    completion.sort()
    for idx, name in enumerate(completion):
        if participant[idx] != completion[idx]:
            return participant[idx]
    
    return participant[-1]