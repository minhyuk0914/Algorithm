def solution(s):
    
    s_int = list(map(int, s.split(' ')))
    answer = f'{min(s_int)} {max(s_int)}'
    return answer 