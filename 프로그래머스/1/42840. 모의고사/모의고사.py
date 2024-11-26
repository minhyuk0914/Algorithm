def solution(answers):
    ans = []
    per_1 = [1, 2, 3, 4, 5]
    per_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    per_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score_list = [0] * 3
    
    for idx, check in enumerate(answers):
        if check == per_1[idx % len(per_1)]:
            score_list[0] += 1
        if check == per_2[idx % len(per_2)]:
            score_list[1] += 1
        if check == per_3[idx % len(per_3)]:
            score_list[2] += 1

    for idx, score in enumerate(score_list):
        if score == max(score_list):
            ans.append(idx+1)            
    return ans