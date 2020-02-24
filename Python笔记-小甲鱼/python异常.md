

![image-20200219155315073](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200219155315073.png)

![image-20200219155332715](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200219155332715.png)



****

#### 报错小节

1. AssertionError断言语句，只有当一个条件一定为真时，才会执行程序，否则抛出一个异常。

![image-20200219155934862](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200219155934862.png)

2. AttributeError,尝试访问未知的对象属性，即访问某个不存在的属性或方法。

****

#### 异常处理

##### 1.try-except-finally语句

![image-20200222160505472](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200222160505472.png)

```
try:
	f = open("一个不存在的文件.txt")
	print(f.read())
	f.close()
except OSError:
	print("文件不存在")

#输出	
文件不存在
```

**try后可以跟多个except语句，但是如果异常中出现了未写明的异常时，仍然会抛出异常，导致程序退出。并且，一旦发现错误，会直接跳到相应的except语句，中间的代码不再执行。**

```
try:
	
except OSError as reason:
	print("文件不存在\n错误原因：" + str(reason))
#输出为
文件不存在
错误原因：[Errno 2] No such file or directory: '一个不存在的文件.txt'
#可以将多个异常放到一起
try:
	
except (OSError TypeError):
	print("文件不存在\n错误原因：")

```

**可以不指定异常类型，使任何错误都能执行except语句后的代码**

**但是不推荐这样做**

```
try:
	f = open("一个不存在的文件.txt")
	print(f.read())
	f.close()
except:
	print("出现错误了")
```

**finally语句**后的代码是无论如何都会被执行的代码，用于处理一些必需的操作。比如，当我们`f = open()`一个文件时，在处理过程中出现的异常，会使程序直接跳到末尾而没有`f.close()`操作，因此我们可以把这个代码放在finally语句中。

##### 2. raise语句

手动抛出一个异常

![image-20200219163943401](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200219163943401.png)

