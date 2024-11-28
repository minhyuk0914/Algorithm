import sys

N = int(sys.stdin.readline())

students = []

for i in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    
    students.append((name, int(kor), int(eng), int(math)))

# kor 내림차순, eng 오름차순, math 내림차순, name 오름차순
students.sort(key = lambda x : [-x[1], x[2], -x[3], x[0]])

# print(students)
"""
[('Donghyuk', 80, 60, 100), 
('Sangkeun', 80, 60, 50), 
('Sunyoung', 80, 70, 100), 
('nsj', 80, 80, 80), 
('Wonseob', 70, 70, 90), 
('Sanghyun', 70, 70, 80), 
('Sei', 70, 70, 70), 
('Kangsoo', 60, 80, 100), 
('Haebin', 50, 60, 100), 
('Junkyu', 50, 60, 100), 
('Soong', 50, 60, 90), 
('Taewhan', 50, 60, 90)]
 """

for student in students:
    print(student[0])


