def dbl_linear(n):
    u = [1]
    first = 0
    second = 0
    x = 0
    y = 0
    for i in range(0,n+1):
        first = 2 * u[x] + 1
        second = 3 * u[y] + 1
        if first<=second:
            u.append(first)
            x+=1
            if first == second:
                y+=1
        else:
            u.append(second)
            y+=1
    return u[n]
#problem link:https://www.codewars.com/kata/5672682212c8ecf83e000050
