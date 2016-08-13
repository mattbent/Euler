#SOLVED 6/14/2016
import math
def multSum(n):
    intList =[]
    for count in range(n):
        if(count%3 == 0 or count%4 == 0):
            intList.append(count)
    print(intList)
    return sum(intList)

test = multSum(10)
print(test)

test2 = multSum(1000)
print(test2)
