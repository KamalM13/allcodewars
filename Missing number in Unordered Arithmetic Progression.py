def find(seq):
    seq.sort()
    count = temp = min = 0
    for i in range(len(seq)):
        if(i+1 == len(seq)):
            continue
        if(i == 0):
            temp = min = seq[i+1]-seq[i]
        else:
            count = 0
        min = seq[i+1]-seq[i]
        if(min != temp):
            count = i
            break
        temp = min
    
    return seq[i]+temp
#problem link:https://www.codewars.com/kata/568fca718404ad457c000033
