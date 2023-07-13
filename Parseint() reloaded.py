def parse_int(string):
    map = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, 
  "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, 
  "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30, "forty":40, "fifty":50, 
  "sixty":60, "seventy":70, "eighty":80, "ninety":90};
    multiMap = {"hundred":100, "thousand":1000, "million":1000000};
    if string in map:
        return map[string]
    if string in multiMap:
        return multiMap[string]
    temp = []
    string = string.replace("-"," ")
    temp = string.split(" ")
    holder = 0
    previousMulti = 0
    multi = []
    current = []
    for i in range(len(temp)):
        if temp[i] in map:
            holder += map[temp[i]]
            if(i == len(temp) - 1):
                current.append(holder)
                holder = 0
        if temp[i] in multiMap:
            if holder == 0:
                holder = 1
            holder *= multiMap[temp[i]]
            current.append(holder)
            multi.append(multiMap[temp[i]])
            holder = 0

    result = "0"
    if len(current) == 1:
        return current[0]
    for i in range(0,len(current)-1):
        if(current[i] < current[i+1]):
            #print(current)
            if(current[i + 1] == 1000):
                result = str(int(result) + current[i] *current[i+1] )
                continue
            current[i]= int(current[i]/multi[i])
            result += str(current[i]) + str(current[i+1])
            current[i+1] = int(result)
        else:
            if(result != "0"):
                result = str(int(result) + current[i+1])
            else:
                result = str(int(result) + current[i + 1] + current[i])
    hold = list(result)
    if hold[0] == '0':
        hold.insert(2,'0')
        hold.remove('0')
        result=''.join(hold)
        print(hold)
    return int(result)
#problem link:https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
