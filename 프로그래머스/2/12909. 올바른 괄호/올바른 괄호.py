def solution(s):
    # 올바른 괄호 찾기를 위해 stack 활용
    stack = []
    
    for i in s:
        # '(' 이라면, stack에 추가
        if i == '(':
            stack.append(i)
        # ')' 일 때, stack안에 값('(')이 존재한다면, stack.pop()으로 비우기
        # 존재하지 않다면, 올바르지 않은 괄호이므로, False 반환
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
    
    # 만약 반복문을 마치고 stack 안에 값이 존재한다면, 올바르지 않은 괄호
    if stack:
        return False
    else:
        return True