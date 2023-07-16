def sum_strings(x, y):
    if len(x) == len(y) == "":
        return "0"
    if len(x) == len(y) == 1:
        return str(int(x)+int (y))
    diff = min(len(x),len(y))
    lastx = len(x) - 1
    lasty = len(y) - 1
    result = ""
    carry = 0
    for i in range(diff):
        sum = int(x[lastx]) + int(y[lasty]) + carry
        if sum >= 10: 
            sum-=10
            carry = 1
        else: carry = 0
        result += str(sum)
        lastx-=1
        lasty-=1
    if lasty>lastx:
        for i in range(lasty,-1,-1):
            sum = int(y[i]) + carry
            if sum >= 10: 
                sum -= 10
                carry = 1
            else:
                carry = 0
            if i == 0 and sum == 0 and carry == 0:
                continue
            result += str(sum)
        if carry == 1:
            result += str(carry)
            
    elif lastx>lasty:
        for i in range(lastx,-1,-1):
            sum = int(x[i]) + carry
            if sum >= 10:  
                sum-=10
                carry = 1
            else:
                carry = 0
            if i == 0 and sum == 0 and carry == 0:
                continue
            result += str(sum)
        if carry == 1:
            result += str(carry)
    else:
        if carry == 1:
            result += str(carry)
    result = list(result[::-1])
    for i in range(len(result)):
        if result[i] == "0":
            result.pop(i)
        if int(result[i]) > 0:
            break
    if len(result) == 0: result = '0'
    return ''.join(result)
  #problem link: https://www.codewars.com/kata/5324945e2ece5e1f32000370
