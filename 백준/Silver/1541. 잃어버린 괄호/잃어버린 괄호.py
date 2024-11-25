import sys

sentence = sys.stdin.readline().split("-")

total = 0
for i in sentence[0].split('+'):
    total += int(i)

for i in sentence[1:]:
    for j in i.split('+'):
        total -= int(j)

print(total)