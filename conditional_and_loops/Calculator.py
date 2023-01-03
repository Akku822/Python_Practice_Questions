while True:
    n = int(input())
    if n == 1:
        x = int(input())
        y = int(input())
        add = x+y
        print(int(x+y))
    elif n == 2:
        x = int(input())
        y = int(input())
        print(int(x-y))
    elif n == 3:
        x = int(input())
        y = int(input())
        print(int(x*y))
    elif n == 4:
        x = int(input())
        y = int(input())
        print(int(x/y))
    elif n == 5:
        x = int(input())
        y = int(input())
        print(int(x % y))
    elif n == 6:
        quit()
    else:
        print("Invalid Operation")
