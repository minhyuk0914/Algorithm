def route(x, y, direction, distance):
    if direction == 'E':
        y += distance
    elif direction == 'W':
        y -= distance
    elif direction == 'N':
        x -= distance
    elif direction == 'S':
        x += distance
        
    return (x, y)

def solution(park, routes):
    now_x, now_y = 0, 0
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == 'S':
                now_x, now_y = x, y
                break
    
    # 명령 수행
    for op in routes:
        direction, distance = op.split(' ')
        distance = int(distance)
        
        move_x, move_y = now_x, now_y
        valid = True  # 이동 가능 여부
        
        # 한 칸씩 이동 경로 확인
        for _ in range(distance):
            move_x, move_y = route(move_x, move_y, direction, 1)
            
            # 왼쪽 벽(0), 오른쪽 벽(최대 길이), 위(0), 아래(최대 길이), 장애물(X) 확인
            if not (0 <= move_x < len(park) and 0 <= move_y < len(park[0])) or park[move_x][move_y] == 'X':
                valid = False
                break
        
        # 유효한 경우에만 이동
        if valid:
            now_x, now_y = move_x, move_y
        
    return [now_x, now_y]
   

