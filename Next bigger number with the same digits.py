def next_bigger(n):
    number = list(str(n))
    if(len(number) == 1 or number == sorted(number, reverse = True)):
        return -1
    target = 0
    for i in range(len(number)-1,-1,-1):
        if number[i] > number[i-1]:
            target = i-1
            break
    swap = 0
    min = 999
    hold = target
    for i in range(hold,len(number)):
        if number[i] > number[hold] and int(number[i]) < min:
            min = int(number[i])
            swap = i
    print(target,swap)
    number[target] , number[swap] = number[swap] , number[target]
    number1 = number[hold+1:]
    number1.sort()
    del number[hold+1:]
    number = number + number1
    result = ''.join(number)
    return int(result)
#problem link:https://www.codewars.com/kata/55983863da40caa2c900004e
