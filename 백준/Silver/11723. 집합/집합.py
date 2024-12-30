import sys

M = int(sys.stdin.readline())

S = set()
for _ in range(M):

    oper = list(sys.stdin.readline().split())
    if len(oper) > 1:
        if oper[0] == 'add':
            S.add(int(oper[1]))
        elif oper[0] == 'remove' and int(oper[1]) in S:
            S.remove(int(oper[1]))
        elif oper[0] == 'check':
            if int(oper[1]) in S:
                print(1)
            else:
                print(0)
        elif oper[0] == 'toggle':
            if int(oper[1]) in S:
                S.remove(int(oper[1]))
            else:
                S.add(int(oper[1]))
    else:
        if oper[0] == 'all':
            S = set([i for i in range(1, 20 + 1)])
        elif oper[0] == 'empty':
            S = set()
