def solution(s):
    num_dict = {
        "0" : "zero",
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine"
    }
    answer = s
    for number, alpha in num_dict.items():
        answer = answer.replace(alpha, number)
    
    return int(answer)