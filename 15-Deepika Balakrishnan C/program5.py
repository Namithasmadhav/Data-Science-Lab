def common_data(list1, list2):
    result = False  
    for x in list1:
        for y in list2:
            if x == y:
                result = True  
                return result
    return result
a=[1,2,3,4,5]
b=[5,6,7,8,9]
c=[6,7,8,9]

print(common_data(a,b))  
print(common_data(a,c)) 
