"""

元组： 
    介绍：不可变的序列，类似于列表，但创建后不能修改
    特点：
        1.可以储存不同类型的元素
        2.元素可以重复、有序、不可以修改（支持索引访问、切片）
    定义：
        #定义元组：
            元组名称 = （元素1，元素2，...）
        #定义空元组：
            元组名称 = tuple（）

    方法：
        count（）：统计某元素在元组中出现的次数
        index（）：查找某个元素在元组中的索引位置（第一次出现的位置） 

"""

# ---------------------------- 元组基本操作 - tuple -----------------------------------
#定义
t1 = (80,95,78,50,76,88,85,20)

print(t1)
print(type(t1))

# 索引访问
print(t1[0])
print(t1[-1])

# 切片
print(t1[0:5:1])

# count() 统计元素的个数
print(t1.count(80))

# index() 获取元素的索引（第一个元素的位置）
print(t1.index(80))

# 注意点：如果定义单元素的元组，单个元素之后要加上逗号，比如(100,)
t2 = ()
print(t2)
print(type(t2)) # 空元组

t3 = (100)
print(t3)
print(type(t3)) # int类型

t3 = (100,)
print(t3)
print(type(t3)) # 单元组类型

# --------------------------------- 元祖-组包与解包 --------------------------------
#组包(Packing)：将多个值合并到一个容器（元组、列表）中。
#解包(Unpacking)：将容器（元组、列表）解开成独立的元素，分别赋值给多个变量

"""

    定义元组，组包
    t1 = (5,7,9,1)
    定义元组，组包
    t2 = 5,7,9,1


    基础解包
    a,b,c,d = t1

    （*）扩展解包
    x, *y, z = t2   #x为5，y为[7,9]，z为1
    s, *o = t2      #s为5，o为[7,9,1]
    *0, e = t2      #o为[5,7,9],e为1

    说明：在元组解包时，*表示收集剩余的所有元素，允许我们处理不确定数量的元素
            （生成列表，以便于可以进行进一步处理）
    
"""
# 组包操作
t1 = (5,7,9,10,2,23,12)

t2 = 5,7,9,10,2,23,12

print(t1)
print(t2)

# 解包操作
# 基础解包（变量数量与容器的元素个数一致）
a,b,c,d,e,f,g = t1
print(a,b,c,d,e,f,g)

# 扩展解包（*收集剩余的所有元素，封装列表list中）
first,second,*other,last = t2
print(first,second)
print(other)
print(last)

# Question 1：现有两个变量：分别为a = 10，b = 20，现进行值交换后输出至控制台
a = 10
b = 20
a,b = b,a   #组包和解包的操作 ---> a,b = t; t = b,a
print(a)
print(b)

# Queation 2：现有三个变量：a = 100，b = 200，c = 300，使得a,b,c = c,a,b，最后输出
a,b,c = 100,200,300
a,b,c =c,a,b
print(a,b,c)

# Question 3：
#       1.计算每个学生的总分、各科平均分、然后一并输出出来
#       2.统计各科成绩的最低分、最高分、平均分，并输出
#       3.查找成绩优秀（平均分大于90）的学生，并输出
students = (
    ("S001","王林", 85, 92, 78),
    ("S002","李慕婉", 92, 88, 95),
    ("S003","十三", 78, 85, 82),
    ("S004","曾牛", 88, 79, 91),
    ("S005","周秩", 95, 96, 89),
    ("S006","王卓", 76, 82, 77),
    ("S007","红蝶", 89, 91, 94),
    ("S008","徐立国", 75, 69, 82),
    ("S009","许木", 86, 89, 98),
    ("S010","遁天", 66, 59, 72)
    )

print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
# 方式一：
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t {s[1]}\t {s[2]}\t {s[3]}\t {s[4]}\t {total}\t {avg:.1f}")

# 方式二： 元组解包
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id}\t {name}\t {chinese}\t {math}\t {english}\t {total}\t {avg:.1f}")

print()

chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文最低分：{min(chinese_scores)},最高分：{max(chinese_scores)},平均分：{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分：{min(math_scores)},最高分：{max(math_scores)},平均分：{sum(math_scores)/len(math_scores)}")
print(f"英语最低分：{min(english_scores)},最高分：{max(english_scores)},平均分：{sum(english_scores)/len(english_scores)}")

print()

print("优秀学生（平均分>90）名单如下：")
# 方式一：
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"学号：{s[0]} 姓名：{s[1]} 平均分：{avg:.1f}")

# 方式二：
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号：{id} 姓名：{name} 平均分：{avg:.1f}")