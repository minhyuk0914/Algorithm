import math

def solution(arr):
    ans = 1
    for x in arr:
        ans = int(ans * x / math.gcd(ans, x))
    return ans