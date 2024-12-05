from itertools import permutations

def checkPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False    
    return True


def solution(numbers):
    answer = []
    li = list(numbers)
    
    nums_li = []
    
    for i in range(1, len(numbers) + 1):
        nums_li.append(list(permutations(numbers, i)))
        
    nums_li = [int(''.join(y)) for x in nums_li for y in x]
    
    for i in nums_li:
        if checkPrime(i):
            answer.append(i)
            
    return len(set(answer))