# coding: utf-8

lst = [1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 9, 9, 10, 99, 99, 99, 100, 100]
intervals = {'{0}-{1}'.format(10 * x + 1, 10 * (x + 1)): 0 for x in range(10)}
for _ in lst:
    for interval in intervals:
        start, end = tuple(interval.split('-'))
        if int(start) <= _ <= int(end):
            intervals[interval] += 1
print(intervals)
