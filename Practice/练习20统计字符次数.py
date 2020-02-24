str1 = '''李心怡是猪么？我觉得她是，可她偏说自己不是。
我只能再次劝服她了，唉。'''

def countStr(str1):
    list1 = []
    
    for each in str1:
        if each not in list1:
            if each == "\n":
                print("\\n",str1.count(each))
            else:
                print(each,str1.count(each))
            list1.append(each)

countStr(str1)           
        


    
