import sys

def solve():
    n = int(input())
    s = input()
    
    for length in [2, 3, 4, 7]:
        for i in range(n - length + 1):
            sub = s[i : i + length]
            counts = {'a': 0, 'b': 0, 'c': 0}
            for char in sub:
                counts[char] += 1
            
            if counts['a'] > counts['b'] and counts['a'] > counts['c']:
                print(length)
                return

    print(-1)

t = int(input())
for _ in range(t):
    solve()
