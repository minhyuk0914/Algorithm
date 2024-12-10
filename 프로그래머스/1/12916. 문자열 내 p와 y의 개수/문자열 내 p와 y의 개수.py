def solution(s):
    # 대문자로 변환
    s_upper = s.upper()
    
    # P 와 Y의 요소 숫자가 같다면(모두 없는 경우 .count() == 0), True
    # 그렇지 않다면, False
    if s_upper.count("P") == s_upper.count("Y"):
        return True
    else: 
        return False
