def solution(A,B):
    A.sort(reverse = False)
    B.sort(reverse = True)
    
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer