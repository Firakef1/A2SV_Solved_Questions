t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    casinos = []

    for _ in range(n):
        casino = [int(x) for x in input().split()]
        casinos.append(casino)

    casinos.sort()

    # print(casinos)

    for casino in casinos:
       if casino[2] > k and casino[0] <= k:
           k = casino[2]
    
    print(k)
