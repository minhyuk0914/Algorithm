def solution(clothes):    
    cate_dict = {}
    for _, cate in clothes:
        if cate not in cate_dict:
            cate_dict[cate] = 1
        else:
            cate_dict[cate] += 1
    
    # 조합 계산
    answer = 1
    for key, val in cate_dict.items():
        # 각 카테고리별로 의상을 입지 않는 경우를 포함해 (val + 1) 곱해줌
        answer *= (val + 1)
    return answer - 1