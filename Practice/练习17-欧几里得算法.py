def Euclidean(x,y):
    while y:
        t = x % y
        x = y
        y = t

    return x

print(Euclidean(144,12))

print("".center(25,"="))

def toBin(x):
    list1 = []
    result = ""
    
    while x:
        t = x % 2
        x = x // 2
        list1.append(t)

    '''方法1
    while list1:
        list2 = [str(i) for i in list1]
        list2.reverse()
        temp = int(("").join(list2))
    '''
    
    #方法2
    while list1:
        result += str(list1.pop())
    
    return result

print(toBin(255))


    
        
    
            
        
