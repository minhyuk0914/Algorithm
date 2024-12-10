def solution(n):
    list_n = list(map(int, str(n)))
    list_n.sort(reverse = True)
    
    return int("".join(map(str, list_n)))