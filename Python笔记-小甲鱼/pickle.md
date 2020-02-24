1. pickle.dump(要写入的数据，写入的文件)

   ```
   my_list = [123, 3.14, "小甲鱼", ["another list"]]
   pickle_file = open("D:\\test.pkl","wb")
   pickle.dump(my_list,pickle_file)
   pickle_file.close()
   ```

2. pickle.load(载入的文件)

   ```
   pickle_file = open("D:\\test.pkl","rb")
   my_list2 = pickle.load(pickle_file)
   print(my_list2)
   [123, 3.14, '小甲鱼', ['another list']]
   ```

   

