import sys

N = int(sys.stdin.readline())
tree = {}

for i in range(N):
    root, left_node, right_node = sys.stdin.readline().split()
    tree[root] = [left_node, right_node]


# print(tree)
"""
{'A': ['B', 'C'],
 'B': ['D', '.'],
 'C': ['E', 'F'], 
 'E': ['.', '.'], 
 'F': ['.', 'G'], 
 'D': ['.', '.'], 
 'G': ['.', '.']}
"""

# 전위 순회 : 루트 - 왼쪽 - 오른쪽 
def preorder(root):
    print(root, end = '')
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])

# 중위 순회 : 왼쪽 - 루트 - 오른쪽
def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    print(root, end = '')
    if tree[root][1] != '.':
        inorder(tree[root][1])

# 후위 순회 : 왼쪽 - 오른쪽 - 루트
def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    print(root, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')