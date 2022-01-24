# Max number from a list
def maxNum(list):
    max=list[0]
    for x in list:
        if x > max:
            max=x
    return max
list=[1,66,2,6,99]
print(maxNum(list))

# 2nd max from a list
list.sort()
print(list[-2])
