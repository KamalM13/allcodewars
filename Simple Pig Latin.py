def pig_it(text):
    string = list(text)
    holder = 0
    for i in range(len(string)):
        if string[i] == ' ' or i == len(string) - 1:
            for j in range(i - 1, -1, -1):
                if string[j] == ' ':
                    holder = j + 1
                    break
            if(i != len(string) - 1):
                string.insert(i, string[holder])
            else:
                string.insert(i+1, string[holder])
            string.pop(holder)
    flag = 0
    for j in range(1,10000):
        for i in range(len(string)):
            if string[i] == ' ' or i == len(string) - 1:
                if i == len(string) - 1:
                    flag = 1
                    if string[i].isalpha():
                        string.insert(i+1, 'y')
                        string.insert(i+1, 'a')
                else:
                    string.insert(i, 'y')
                    string.insert(i, 'a')
                    string[i+2] = '1'
                break
        if flag == 1:
            break
    string[:] = [x if x != '1' else ' ' for x in string]
    return ''.join(string)
#problem link:https://www.codewars.com/kata/520b9d2ad5c005041100000f
