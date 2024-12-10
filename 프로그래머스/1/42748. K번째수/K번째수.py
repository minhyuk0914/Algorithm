def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        start_index, end_index, find_num = commands[idx] # 시작 인덱스, 마지막 인덱스, 찾으려는 인덱스
        sort_array = sorted(array[start_index - 1 : end_index]) # 슬라이싱 & 정렬
        ans = sort_array[find_num - 1] # 찾으려는 인덱스에 위치한 ans 찾기 
        answer.append(ans) # answer에 ans 삽입
    
    return answer