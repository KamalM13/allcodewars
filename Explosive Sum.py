def exp_sum(n):
    number = []
    number.append(1)
    for i in range(n) : number.append(0) 
    for i in range(0,n+1):
        for j in range(i,n+1):
            number[j] += number[j-i]
    return number[n]/2
  
#problem link:https://www.codewars.com/kata/52ec24228a515e620b0005ef
