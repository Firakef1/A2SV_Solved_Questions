if __name__ == '__main__':
    n = int(input().strip())
        
    if n%2 == 1 or n in range(6, 21):
        print("Weird")
    elif n > 20 or n in range(2, 6):
        print("Not Weird")
        