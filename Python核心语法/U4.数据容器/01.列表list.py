# 列表操作
# 定义列表:[元素1，元素2，元素3，....] 可以存放不同类型元素，可重复，有序，元素可以修改
s = [56,90,88,65,90,"A","Hello",True]

print(type(s))

# 访问列表元素
# 获取
print(s[0]) #正向索引，从0开始
print(s[-8]) #反向索引 从-1开始

print(s[2])
print(s[-6])

# 修改
s[5] = "ABC"
print(s)

# 删除
# # 关键字：del s[]
del s[6]
print(s)

# 遍历
for item in s:
    print(item)

# # 注意：如果指定的索引值超出范围，将会报错！！！

"""
列表-切片
    介绍：切片是指对操作的数据截取其中一部分的操作。
            列表、字符串、元组都支持切片操作。

    语法：序列数据[开始索引（包含）：结束索引（不包含）：步长]
        1.不包含结束索引位置对应的元素
        （开始索引未指定默认为0；结束索引未指定默认为列表长度（直至列表末尾）
          步长未指定默认为1）
        2.索引采用正向、反向索引都可以
        3.步长是选取间隔，默认步长为1

"""
s = ["A","C","H","K","L","X","C","U"]

print(s[0:5:1])
print(type(s[0:5:1]))
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[0:5:2])
print(s[0:-2:1])

"""

列表-常见方法：
    append()    在列表尾部追加元素     s.append(具体数据)
    insert()    在指定索引之前插入该元素  s.insert(0, 92)
    remove()    删除列表中第一个匹配到的值 s.remove(75)
    pop()       删除列表中指定索引位置的元素（若没有，默认删最后一个）  s.pop(2)/s.pop()
    sort()      对列表进行排序（元素数据类型需要一致）  s.sort()
    reverse()   反转列表元素            s.reverse()

"""
# # Question 1:将用户输入的10个数字，存储到一个列表中，并将列表中的
#            # 数字进行排序，输出其中的最小值、最大值和平均值
num_list = []

for i in range(10):
    num = int(input("请输入一个有效的数字："))
    num_list.append(num)

print("数字列表：",num_list)

num_list.sort()
print("排序后的数字列表：",num_list)

print("最小值：",num_list[0])  #或者min（）
print("最大值：",num_list[-1])  #或者max（）
print("平均值：",sum(num_list)/len(num_list))

# Question 2：合并两个列表中的元素，并对合并的结果进行去重处理
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]

for num in num_list2:       #此段循环也可简洁改为：
    num_list1.append(num)   # num_list = [*num_list1,*num_list2]
                            # 或者改为：
print(num_list1)            # num_list = num_list1 + num_list2

new_list = []

for num in num_list1:
    if num not in new_list: #布尔值，若不存在，则返回True
        new_list.append(num)

new_list.sort()
print("合并之后的列表为：",new_list)

"""

列表推导式：
    1.含义：就是按照一定规则快速生成一个列表的方法
    2.格式1：列表名称=[要插入列表的数据 for i in 列表]
    3.格式2：列表名称=[要插入列表的数据 for i in 列表 if条件]

"""

# Question 3：生成1-20的平方列表
# 传统法：
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)

# print(num_list)
# # 简约版（列表推导式）：
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)

# Question 4：从如下数字列表中提取所有偶数，并计算其平方，组成一个新列表
# num_list = [12,32,45,77,88,92,33,57,97,98,110,122]
# new_list = [i**2 for i in num_list if i % 2 == 0]

# print(new_list)

# Question 5：将如下多个列表合并为一个列表，并去重，排好序输出
list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
list2 = ['X','Z','T','Y','D','E','F','G']
list3 = ['W','A','S','D']

new_list = []
num_list = list1 + list2 + list3
for i in num_list:
    if i not in new_list:
        new_list.append(i)

new_list.sort()
print(new_list)

# Question 6：将如下可被3 或 5整除的元素提出，获取对应平方组成新列表
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22]
new_list = [num**2 for num in list1 if num % 3 == 0 or num % 5 == 0]
print(new_list)

# Question 7：将如下列表中的正数提取出，封装为一个新的列表
list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
new_list = [num for num in list1 if num > 0]
new_list.sort()
print(new_list)