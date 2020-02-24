print("我爱李心怡啊".center(25,"-"))
import random
secret = random.randint(1,9)
temp = input("猜猜我心里想的是1-9整数中哪个数字？")
if temp.isdigit():
        guess = int(temp)
        num = 1
        while num < 4:
                if guess == secret:
                        print("恭喜你猜对了")
                else:
                        if guess > secret :
                                print("猜错了哟，你猜的太大了")
                        else:
                                print("猜错了哟，你猜的太小了")
                        chance = 3 - num
                        if chance>0:
                                temp = input("再试试吧，你还有{}次机会".format(chance))
                        guess = int(temp)
                num+=1
else:
        print("不想跟不读题的人玩，拜拜")
print("游戏结束，下\"次再玩")       


