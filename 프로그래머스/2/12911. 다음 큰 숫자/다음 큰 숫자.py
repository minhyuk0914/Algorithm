def solution(n):
    
    ans = n + 1

    while True:
        
        if bin(n).count('1') == bin(ans).count('1'):
            break
        else:
            ans += 1
    return ans