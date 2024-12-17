def solution(name, yearning, photo):
    ans = []
    # 두개의 리스트 name, yearning을 zip으로 묶어서 dict로 변환
    name_year_dict = {key : val for key, val in zip(name, yearning)}
    
    for per_list in photo:
        total = 0
        for per in per_list:
            if per in name_year_dict:
                total += name_year_dict[per]
            
            # name_year_dict에 그리운 사람이 없으면 pass 
            # else:
            #     continue
        # 그리움 점수를 합한 사진의 추억 점수를 ans에 삽입
        ans.append(total)
    return ans