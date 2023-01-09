num = int(input())
copy = num
n=0
while(copy>0):
    n=n+1  # counting number of digits
    copy=copy//10

sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n #number of digits in power
   temp //= 10
if num == sum:
    print("true")
else:
    print("false")