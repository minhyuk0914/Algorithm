import sys

N = int(sys.stdin.readline())

li = []
for idx in range(N):
    age, name = sys.stdin.readline().split() # [age, name]
    age = int(age) # age는 int 형으로 변환
    age_name_idx = [age, name, idx] # [age, name, idx]
    li.append(age_name_idx)


li.sort(key = lambda x : [x[0], x[2]]) # 나이(x[0])순 정렬, 나이가 같으면, 가입한(x[2]) 순

for i in range(N):
    print(*li[i][:2]) # 20 Sunyoung
    # print(' '.join(li[i][:2]))
    # print(f'{li[i][0]} {li[i][1]}')