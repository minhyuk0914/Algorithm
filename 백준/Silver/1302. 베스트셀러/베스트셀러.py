import sys

N = int(sys.stdin.readline())

book_dict = {}
for _ in range(N):
    name = sys.stdin.readline().strip()
    if name not in book_dict.keys():
        book_dict[name] = 1
    else:
        book_dict[name] += 1

sorted_dict_list = sorted(book_dict.items(), key = lambda x : (-x[1], x[0]))

print(sorted_dict_list[0][0])