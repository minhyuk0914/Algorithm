import sys
import math

T = int(sys.stdin.readline())

li = []
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split()) # mCn
    
    # factorial을 통한 조합 풀이 m! // (n! * (m-n)!)
    # print(math.factorial(m) // (math.factorial(n) * math.factorial(m-n)))
    # math.comb 을 통한 풀이
    print(math.comb(m, n))