def solution(babbling):
    answer = 0
    can_li = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        for can in can_li:
            # 연속해서 같은 발음인 경우
            if can * 2 in word:
                break
            # 정상인 경우, 가능한 발음을 ' '(공백)으로 대체
            word = word.replace(can, ' ')
        
        # 공백 제거 
        if word.strip() == '':
            answer += 1
    
    return answer