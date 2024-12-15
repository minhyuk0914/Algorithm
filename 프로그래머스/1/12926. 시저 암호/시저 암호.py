def solution(s, n):
    s = list(s)
    
    for i in range(len(s)):
        # 공백인 경우 패스
        if s[i] == ' ':
            continue
        # 문자가 대문자인 경우
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        # 문자가 소문자인 경우
        else:
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return ''.join(s)