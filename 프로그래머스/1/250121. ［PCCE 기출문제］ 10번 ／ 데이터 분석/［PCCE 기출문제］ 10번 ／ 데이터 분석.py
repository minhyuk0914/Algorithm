def solution(data, ext, val_ext, sort_by):
    answer = []
    # ext에서 나오는 카테고리를 리스트에 저장 -> index() 활용 
    ext_cat = ['code', 'date', 'maximum', 'remain']
    
    
    for row in data:
        # ext에 맞는 index 번호를 ext_cat를 활용해, ext_idx를 얻음
        ext_idx = ext_cat.index(ext)

        # row[ext_idx] 의 값이 val_ext 보다 작거나 같으면 answer에 저장
        if row[ext_idx] <= val_ext:
            answer.append(row)
    
    # sort_idx 또한 동일하게 구함
    sort_idx = ext_cat.index(sort_by)
    # sort(key = lambda x : x) 활용하여 올바르게 정렬 
    answer.sort(key = lambda x : x[sort_idx])
    
    return answer