#Write a function called partition that accepts a list and a callback function (which you can assume returns true or false)
#The function should iterate over each element in the list and invoke the callback function at each iteration
#If the result of the callback function is True, the element should be added into the first list (the truthy one)
#If the result of the callback function is False, the element should go into the second list (the falsey one)
#When it's finished, the partition function should return both lists inside of one larger list, like so: 
# [truthy_list, falsey_list]


def cb(num):
    return num % 2 == 0


def partition(list1, isEven):
    t = []
    f = []
    for x in list1:
        if cb(x):
            t.append(x)
        else:
            f.append(x)
    return [t,f]

print(partition([1,3,4,5,8,2], cb))

print(partition([1,3,5,7,9,10,12,14,25,27,26,412], cb))