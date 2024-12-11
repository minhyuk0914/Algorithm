def solution(numbers):
    list_10 = [i for i in range(0, 10)]
    
    for x in numbers:
        list_10.remove(x)
    
    answer = sum(list_10)
    return answer