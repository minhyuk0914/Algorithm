def solution(s):
    # 소수 일 경우 int형 변환을 통한 버림
    mid = int(len(s) / 2)
    
    # 길이가 짝수 일 경우 
    if len(s) % 2 == 0:
        answer = s[mid - 1 : mid + 1]
    # 길이가 홀수 일 경우
    else:
        answer = s[mid]
    
    return answer