def solution(s):
    answer = []
    s_list = s.split(' ')
    
    for word in s_list:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
    return " ".join(answer)