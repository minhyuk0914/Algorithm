def solution(x):
    # int x -> str x -> list, map(int)
    list_x = list(map(int, str(x)))
    
    # x % sum(list) == 0 인 경우, 하샤드 수(True)
    if x % sum(list_x) == 0:
        return True
    else:
        return False
