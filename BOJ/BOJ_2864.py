import sys

A, B = sys.stdin.readline().split()

# 두 수의 덧셈에서의 최솟값은 6이 아닌 5로 읽은것 
ab_min = int(A.replace('6', '5')) + int(B.replace('6', '5'))
# 두 수의 덧셈에서의 최댓값은 5이 아닌 6로 읽은것 
ab_max = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(ab_min, ab_max)