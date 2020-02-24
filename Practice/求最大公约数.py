def showMaxFactor(num):
        count = num // 2
        while count > 1 :
                if num % count == 0:
                        print("%d的最大约束是%d" % (num,count))
                        break
                count -= 1
        else :
                print("%d是一个素数" % num)
                

num = int(input("请输入一个整数"))
showMaxFactor(num)
        
