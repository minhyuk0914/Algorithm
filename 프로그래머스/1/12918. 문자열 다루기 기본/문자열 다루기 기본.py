def solution(s):
    # isdigit() str 내 모든 요소가 숫자인 경우 True, 아니면 False
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        answer = True
    else:
        answer = False
    return answer