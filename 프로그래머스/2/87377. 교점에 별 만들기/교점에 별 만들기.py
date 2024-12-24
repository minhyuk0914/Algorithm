def cal_point(line1, line2):
    """
    line1, line2 : 서로 다른 두개의 직선
    두 개의 직선 간 교점이 없는 경우 -> return None
    교점이 있는 경우 -> return [x, y]
    """
    a, b, e = line1
    c, d, f = line2
    
    if a * d - b * c == 0:
        return None
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)
    
    if x == int(x) and y == int(y):
        # 소수점 제거
        x = int(x)
        y = int(y)
        return [x, y]
    else:
        return None
    
def solution(line):
    arr = []

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i] == line[j]:
                continue
            pos_x_y = cal_point(line[i], line[j])
            if pos_x_y:
                arr.append(pos_x_y)
            
            
    min_x = min(x for x, y in arr)
    max_x = max(x for x, y in arr)
    min_y = min(y for x, y in arr)
    max_y = max(y for x, y in arr)

    x_len = max_x - min_x + 1
    y_len = max_y - min_y + 1
    
    ans_arr = [['.'] * x_len for _ in range(y_len)]
    
    # 교점 찍기
    for x, y in arr:
        x = x - min_x
        y = max_y - y
        ans_arr[y][x] = '*'
        
    ans_arr = [''.join(row_ans) for row_ans in ans_arr]
    
    return ans_arr