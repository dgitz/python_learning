def convert(data):
    tempstr = ''
    for index,item in enumerate(data):
        tempstr += str(item)
        if index < len(data)-1:
            tempstr += ', '
        if index == len(data) - 2:
            tempstr += ' and '
        #if(index == len(data)-1):
        #    tempstr += ' and '
        #else:
        #    tempstr += ','
    return tempstr

print(convert(['apples','bananas','tofu','cats']))
print(convert([1,2,3,4]))