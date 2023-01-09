def checkArmstrong(n):
    arr = [int(x) for x in str(n)]
    p = len(arr)
    sum = 0
    for digit in arr:
        sum += digit**p
    return sum

n = int(input())
print(n==checkArmstrong(n))