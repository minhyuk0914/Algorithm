from itertools import combinations
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for comb in combinations(nums, 3):
        sum_comb = sum(comb)
        
        if isPrime(sum_comb):
            answer += 1

    return answer