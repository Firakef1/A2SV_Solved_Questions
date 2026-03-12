n = int(input())

lis = [int(x) for x in input().split()]

lis.sort()

print(lis[(n-1)//2])