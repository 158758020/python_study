#### 随机数种子

1. 随机数种子（random seed)在伪随机数生成器中用于生成伪随机数的初始数值。对于一个伪随机数生成器，从相同的随机数种子出发，可以得到相同的随机数序列。随机数种子通常由当前计算机状态确定，如当前的时间。

   > 同一种子，只能得到相同的随机序列。所以在只有在特定地方使用同一种子。一般情况下都是通过random.seed（）不指定种子数，而由计算机当前时间来确定种子以产生随机数。

   > 当我们需要再现随机过程，我们就设定种子。
   >
   > 而当我们只是需要一个随机数而不关心再现过程的时候就不设种子。

   ```
   random.seed(10)
   random.random()-->0.5714025946899135
   random.seed(10)
   random.random()-->0.5714025946899135
   random.random()-->0.4288890546751146
   #与下表一致
   ```

   

![image-20200222145337291](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200222145337291.png)

![image-20200222150017333](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200222150017333.png)



****

#### 随机函数

##### ![image-20200222151646759](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200222151646759.png)

> randint(a,b),产生的整数值包括a和b。
>
> randrange(),不包括n值，即randrange(0,4,2)不能产生4.

![image-20200222151746761](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200222151746761.png)

![image-20200222151806664](C:\Users\DoubleStar\AppData\Roaming\Typora\typora-user-images\image-20200222151806664.png)

> choice()中的元素必须是序列，即可以使用index的序列。集合{1,2,3}不能使用该方法。
>
> shuffle()同上。