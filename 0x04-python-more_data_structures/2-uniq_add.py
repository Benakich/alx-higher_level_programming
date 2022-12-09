#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    res = []
    [res.append(x) for x in my_list if x not in res]
    for i in res:
        sum += i
    return sum
