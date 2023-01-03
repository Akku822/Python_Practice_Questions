number = int(input())

reverse = 0
temp = number

while(temp > 0):
    Reminder = temp % 10
    reverse = (reverse * 10) + Reminder
    temp = temp //10
 

if(number == reverse):
    print("true")
else:
    print("false")