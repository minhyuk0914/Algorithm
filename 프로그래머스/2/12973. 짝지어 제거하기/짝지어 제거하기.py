def solution(s):
    answer = -1
    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        elif stack[-1] != i:
            stack.append(i)
    
    if not stack:
        return 1
    else:
        return 0
    