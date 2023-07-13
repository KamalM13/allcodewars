def sum_of_intervals(intervals):
    intervals.sort()
    if len(intervals) == 1:
        return intervals[0][1] - intervals[0][0]
    sum = max = 0
    for i in range(0,len(intervals)):
        if i == 0:
            sum += intervals[i][1]- intervals[i][0]
            max = intervals[i][1]
        if intervals[i][0] > max:
            sum += intervals[i][1] - intervals[i][0]
            max = intervals[i][1]
        elif intervals[i][1] > max:
            sum += intervals[i][1] - max
            max = intervals[i][1]
    return sum
#https://www.codewars.com/kata/52b7ed099cdc285c300001cd
