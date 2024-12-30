import sys

while True:
    li = list(map(int, sys.stdin.readline().split()))

    if li == [0, 0, 0]:
        break
    
    li.sort()

    if li[0] ** 2 + li[1] ** 2 == li[2] ** 2:
        print('right')
    else:
        print('wrong')