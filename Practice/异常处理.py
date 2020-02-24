try:
        f = open("一个不存在的文件.txt")
        print(f.read())
        f.close()
except OSError as reason:
        print("文件不存在\n错误原因：" + str(reason))
        
