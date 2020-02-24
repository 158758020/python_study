def findstr(desStr,subStr):
    count = 0
    length = len(desStr)

    if subStr not in desStr:
        print("父字符串中没有子字符串")
    else:
        for i in range(length-1):
            if desStr[i] == subStr[0]:
                if desStr[i+1] == subStr[1]:
                    count += 1
    print("子字符串在父字符穿中出现的次数为：{}".format(count))


desStr = "You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted."
subStr = "im"

findstr(desStr,subStr)
