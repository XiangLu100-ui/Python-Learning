# 循环：重复执行一个事情
# # while 循环：
# # 语法结构：
# # while 条件表达式（结果为布尔类型）：
# #      循环体语句1   
# #      循环体语句2
# #      ......
# # else:
# #      条件为False，循环正常结束时执行

# Question 1：打印十遍“人生苦短，我用Python”
i = 0
while i <10:
    print("人生苦短，我用Python")
    i += 1
else:
    print("循环正常结束，执行完毕")

# Question 2：计算1-100之间所有偶数的累加之和
# 方法一：while循环解法
i = 0
num = 0
while i <= 100:
    if i % 2 == 0:
        num += i
    i += 1
else:
    print(f"偶数之和为：{num}")

# 方法二：for 循环解法
i = 1
num = 0
for i in range(1,101):
    if i % 2 == 0:
        num += i
    i += 1
else:
    print(f"偶数之和为：{num}")

# 简化版：
num = 0
for i in range(0,101,2):
    num += i
print(f"偶数之和为：{num}")

# for 循环：本质为一种轮询遍历机制，对一批内容进行逐个处理
# # for 的语法结构：
# # for 元素 in 待处理数据集：
# #     循环体代码（对元素进行处理）
# # else：
# #     循环结束时，执行的代码

# for循环：遍历输入的字符串
msg = input("请输入需要遍历的字符串：")
for s in msg:    # s 表示遍历出来的元素 ； msg 表示需要遍历的数据
    print(f"元素：{s}")  
else:
    print("遍历结束！")

# while循环 与 for循环 的应用场景：
# # while：用于在某个条件满足时一直循环，循环的次数通常是未知的，只知道循环开始/结束的条件。（关注的是循环的条件）
# # for：用于一个已知的数据集进行遍历或已知次数的循环。（关注的是遍历每一个元素）

# Question 3：计算100 - 500之间所有3的倍数的数字之和
total = 0
i = 100
100 <= range <= 500
for i in range:
    if i % 3 == 0:
        total += i
    i += 1
else:
    print(f"数字之和为：{total}")
# 此处第51行无法运行，可以用到range语句进行解决
# range 语句
# # 作用：生成指定规则的数字序列
# # 用法一：range(5) --- 0,1,2,3,4
# # 用法二: range(2,8) --- 2,3,4,5,6,7
# # 用法三：range(0,10,2) --- 0,2,4,6,8
#重新做一遍，可改为：
total = 0
i = 100
for i in range(100,501):
    if i % 3 == 0:
        total += i
    i += 1
else:
    print(f"数字之和为：{total}")

# 简化版：
num = 0
for i in range(102,501,3):
    num += i
print(f"数字之和为：{num}")

# 嵌套循环学习：
# # 语法结构：
# # for 元素 in 待处理数据集1：   (外层循环)
# #     循环体的代码1
# #     循环体的代码2
# #     ......
# #     for 元素 in 待处理数据集2：     （内层循环）
# #         循环体的代码1
# #         循环体的代码2
# #         ......

# small test：打印一个*长度为10 ，宽度为5 的长方形
m = int(input("请输入该长方形的长度："))
n = int(input("请输入该长方形的宽度："))
for j in range(n):
    for i in range(m):
        print("*",end="  ")  # print自带换行效果，end表示每次输出以什么结束，默认\n，此处为空，即不用换行；
    print() 

# Question 4：打印99乘法表
for j in range(1,10):
    for i in range(1,j+1):
        print(f"{i} * {j} = {i * j}",end = "\t")
    print()

# Question 5: 根据输入的直角边长，打印等腰直角三角形
a = int(input("请输入该等腰直角边的边长："))
for j in range(1,a+1):
    for i in range(1,j+1):
        print("*",end = "  ")
    print()

# Question 6：根据输入的数字，打印对应的数字金字塔
a = int(input("请输入一个数字："))
for j in range(1,a+1):
    for i in range(1,j+1):
        print(f"{i}",end = "  ")
    print()

# Question 7：打印国际象棋棋盘
for j in range(8):  # 外层循环：一共8行，j代表当前行号 0-7
    line = ""       # 存储当前一行的图案
    for i in range(8):      #内层循环：每行8个格子，i代表当前列号 0-7
        if (i + j) % 2 == 0:    #行+列 求和偶数：黑块； 奇数：白块
            line += "■ "
        else:
            line += "□ "
    print(line)         #打印完整的一行
