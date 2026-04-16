from collections import defaultdict
n = int(input())

tree = defaultdict(list)

for child in range(2, n+1):
    node = int(input())
    
    tree[node].append(child)
res = True
# print(tree)
def dfs(node):
    
    if node not in tree:
        return "leaf"

    count = 0
    for child in tree[node]:
        if dfs(child) == "leaf":
            count += 1
    
    if count < 3:
        global res
        res = False



dfs(1)

if res:
    print("Yes")
else:
    print("No")