def max_sequence(arr):
    currentSum = 0
    max = float('-inf')
    if all(i < 0 for i in arr):
        return 0
    if not arr:
        return 0
    for i in arr:
        currentSum += i
        if currentSum > max:
            max = currentSum
        if currentSum < 0:
            currentSum = 0
        
    return max

problemlink=https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
