def solution(a, b):
    weekday = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    # 1,3,5,7,8,10,12 : 31일
    # 4,6,9,11 : 30
    # 2 : 28 / 29(윤년)
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    day = b
    for i in range(a):
        day += month[i]
    day %= 7
    
    answer = weekday[day]
    
    return answer