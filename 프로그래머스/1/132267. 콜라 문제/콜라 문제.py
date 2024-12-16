def solution(a, b, n):
    answer = 0
    while n >= a:
        rec = n // a * b
        remain = n % a
        
        answer += rec 
        n = rec + remain
    return answer