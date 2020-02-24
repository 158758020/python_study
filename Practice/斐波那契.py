def fibnacci(n):
        if n< 1:
                print("输入有误1")
                return -1
        if n ==1 or n ==2:
                return 1
        else:
                result = fibnacci(n-1) + fibnacci(n-2)
                return result
n = int(input("请输入斐波那契数列的位置："))
result = fibnacci(n)
print("第 %d 位数是：%d" % (n,result))
