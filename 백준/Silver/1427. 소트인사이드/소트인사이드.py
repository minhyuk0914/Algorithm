import sys

N = list(str(sys.stdin.readline()))

N.sort(reverse = True)

print(''.join(N))