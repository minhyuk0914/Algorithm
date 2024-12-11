def solution(absolutes, signs):
    answer = 0  # 초기 값을 0으로 설정
    for idx in range(len(absolutes)):
        if signs[idx]:  # signs[idx]가 True인 경우
            answer += absolutes[idx]
        else:  # signs[idx]가 False인 경우
            answer -= absolutes[idx]
    return answer