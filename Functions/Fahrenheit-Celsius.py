def printTable(start,end,step):
    for curr_temp in range(start, end+1, step):
        c = 5/9 * (curr_temp-32)
        print(curr_temp, " ", int(c))
   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)