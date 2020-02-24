print("RESTART".center(15,"="))
temp1 = int(input("请输入一个整数："))
for i  in range(1,temp1+1):
        print(i,end="\n")

print("RESTART".center(15,"="))

temp2 = int(input("请输入一个整数："))
while temp2>0:
        a = "*" * temp2
        b = " " * (temp2 - 1)
        temp2 -= 1
        print(b+a)
