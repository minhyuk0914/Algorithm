from collections import Counter

def solution(k, tangerine):
    
    counter = Counter(tangerine).most_common()
    x = k
    ans = 0
    idx = 0
    
    while True:
        if x <= 0:
            break
        else:
            x = x - counter[idx][1]
            ans += 1
            idx += 1

    return ans