# common elements finder function
# define a fuction hich take 2 lists as input and return a ist 
# which contains common elements  of both lists

# example
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

# logic
def common_finder(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common_finder([1,2,5,8], [1,2,7,6]))
