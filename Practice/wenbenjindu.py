import time
scale = 10
print("----------执行开始----------")
for i in range(scale + 1):
        a = "-" * i
        b = "_" * (scale - i)
        c = (i/scale)*100
        print("{2:^3.0f}%[{0}->{1}]".format(a,b,c))
        time.sleep(0.1)
print("----------执行结束----------")
        
        
