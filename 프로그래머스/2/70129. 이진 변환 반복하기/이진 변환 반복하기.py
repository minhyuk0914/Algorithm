def solution(s):
    zero_cnt = 0
    cnt = 0
    
    while True:
        if s == '1':
            break
        
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        c = len(s)
        s = bin(c)[2:]
        
        cnt += 1
    return [cnt, zero_cnt]