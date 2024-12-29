import sys

board = sys.stdin.readline()

board = board.replace('XXXX', 'AAAA').replace('XX', 'BB')

if board.count('X') > 0:
    print(-1)
else:
    print(board)