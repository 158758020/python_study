def hanoi(n, x, y, z):
        if n == 1:
                print(x, " --> ", z)
        else:
                hanoi(n-1, x, z, y)       #把n-1个盘子从x放到y上
                print(x, " --> ", z)       #把x下最后一个盘子放到z上
                hanoi(n-1, y, x, z)       #把y上的n-1个盘子放到z上
n = int(input("请输入汉诺塔盘子的个数："))
hanoi(n, "X", "Y", "Z")
