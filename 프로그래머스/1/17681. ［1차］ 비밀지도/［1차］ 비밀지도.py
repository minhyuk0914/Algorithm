def solution(n, arr1, arr2):
    answer = []
        
    for i in range(n):
        # 비트 연산 OR 
        result_or = arr1[i] | arr2[i]
        
        # 2진수로 변환 후 자릿수가 부족할 시 n(지도의 한 변 크기)만큼 0으로 채움
        # zfill()은 문자열 형태에서 지정한 길이만큼 0으로 채움
        bin_str = bin(result_or)[2:].zfill(n)
        # 1 -> #, 0 -> 공백 으로 치환
        bin_str = bin_str.replace('1', '#').replace('0', ' ')
        answer.append(bin_str)
    return answer