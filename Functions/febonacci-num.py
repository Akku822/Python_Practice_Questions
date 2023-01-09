def checkFib(n):
    if n==1 or n==0:
        return True
    a = 1
    b = 1
    while a<n:
        a, b = a+b, a
    if a==n:
        return True
    return False

n = int(input())
if checkFib(n):
    print("true")
else:
    print("false")