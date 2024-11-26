from itertools import combinations

def solution(numbers):
    answer = []
    # itertools.combinations(리스트, 숫자) :
    # 리스트 내 숫자크기의 조합을 얻고, 리스트로 변환 후
    # 두 개의 숫자 합을 answer 리스트에 추가/삽입
    for li in list(combinations(numbers, 2)):
        answer.append(sum(li))
        
    ans = set(answer)   # 중복 제거(집합 변환)
    ans = list(ans) # 출력 양식에 맞는 리스트 변환
    ans.sort()
    return ans