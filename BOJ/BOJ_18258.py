import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.append(order[1])
    if order[0] == 'pop':
        if not queue:
            print(-1)
        else:
            pop_num = queue.popleft()
            print(pop_num)
    if order[0] == 'size':
        print(len(queue))
    if order[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    if order[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    if order[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])


# # list활용한 방법
# import sys

# N = int(sys.stdin.readline())

# queue = []

# for i in range(N):
#     order = sys.stdin.readline().split()

#     if order[0] == 'push':
#         queue.append(order[1])
#     elif order[0] == 'pop':
#         if not queue:
#             print(-1)
#         else:
#             pop_num = queue.pop(0)  # .pop(x)에서 x는 해당하는 x인덱스의 값을 뺀다.
#             print(pop_num)
#     elif order[0] == 'size':
#         print(len(queue))
#     elif order[0] == 'empty':
#         if not queue:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'front':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[0])
#     elif order[0] == 'back':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[-1])



