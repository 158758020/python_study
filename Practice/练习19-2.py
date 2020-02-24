def palindrome(string):
    list1 = list(string)
    list2 = list(reversed(list1))
    
    print(list2)
    if list1 == list2:
        print("这是一个回文联")
    else:
        print("这不是一个回文联")

palindrome("海上自来水来自上海")
