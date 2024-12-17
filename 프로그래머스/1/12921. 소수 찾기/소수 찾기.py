def solution(n):
    answer = 0
    for number in range(2, n + 1):
        check = 1

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                check = 0
                break
        answer += check
    return answer