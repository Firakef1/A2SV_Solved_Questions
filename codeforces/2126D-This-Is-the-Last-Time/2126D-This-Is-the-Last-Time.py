# print(casinos)

    for casino in casinos:
       if casino[2] > k and casino[0] <= k:
           k = casino[2]
    
    print(k)