nums = "0123456789"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = r'''!@#$%^&*()_=-/,.?<>;:[]{}|\\'''

pwd = input("请输入要检查的密码：")

#判断是否有空格或是空字符串
while " " in pwd or len(pwd) == 0:
        pwd = input("您输入的密码为空或包含空格，请重新输入：")
        
#密码长度
length_lv = 0
length = len(pwd)
if length <= 8:
        length_lv = 1
elif length >=16:
        length_lv = 3
else:
        length_lv = 2

#密码是否包含数字
con_lv = 0
for i in pwd:
        if i in nums:
                con_lv += 1
                break

#密码是否包含字母
for i in pwd:
        if i in chars:
                con_lv += 1
                break
                
#密码是否包含特殊字符
for i in pwd:
        if i in chars:
                con_lv += 1
                break

#判断密码等级
if length_lv ==1 or   con_lv == 1:
        level = "低"
elif length_lv == 3 and con_lv == 3 and (pwd[0] in chars):
        level = "高"
else:
        level = "中"

#输出等级并提示
print("您的密码安全等级为：",level)
if level == "高":
        print("请您继续保持")
else:
        print("请按以下方式提高您的密码安全等级：\n\
\t1.密码由数字、字母及特殊字符三种组合\n\
\t2.密码由字母开头\n\
\t3.密码长度不低于16位")

print("评定结束".center(25,"="))
