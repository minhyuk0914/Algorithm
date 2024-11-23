from collections import Counter
import sys

N = sys.stdin.readline()
N = N.replace('6', '9')

max_counter = Counter(N)
max_counter['9'] = (max_counter['9'] + 1) // 2 # 올림 
print(max_counter.most_common(1)[0][1])
# print(max(max_counter.values()))