def solution(n):
    rev_base_3 = ''

    while n > 0:
        mod = n % 3
        n = n // 3
        rev_base_3 += str(mod)

    return int(rev_base_3, base = 3)