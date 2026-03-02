t = int(input())

for _ in range(t):
    n, k  = [int(x) for x in input().split()]
    lis = input()

    window = lis[0:k]
    white = window.count("W")
    black = window.count("B")
    _min = white
    i = k

    while i < n:

        if lis[i-k] == "W":
            white-= 1
        elif lis[i-k] == "B":
            black -= 1
        
        if lis[i] == "W":
            white += 1
        elif lis[i] == "B":
            black += 1
        
        _min = min(_min, white)
        i+=1

    print(_min)
