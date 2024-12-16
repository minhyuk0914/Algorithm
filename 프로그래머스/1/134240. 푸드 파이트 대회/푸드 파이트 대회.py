def solution(food):
    ans = ''
    
    for i in range(1, len(food)):
        ans += str(i) * int(food[i] / 2)
    
    ans = ans + '0' + ans[::-1]
    
    return ans