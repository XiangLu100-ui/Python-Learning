"""

字符串的特点
    不可变性（无法修改）；有序性；可迭代性

字符串的索引
    与列表一致，分正向、反向索引

字符串-切片
    介绍：切片是指对操作的对象截取其中一部分的操作。
          字符串、列表、元组都支持切片操作

    语法：序列数据[开始索引（包含）：结束索引（不包含）：步长]
        1.不包含结束索引位置对应的元素
        （开始索引未指定默认为0；结束索引未指定默认为列表长度（直至列表末尾）
          步长未指定默认为1）
        2.索引采用正向、反向索引都可以
        3.步长是选取间隔，默认步长为1（如果是-1，表示从后往前）

        举例：
            s = "Python"
            s[0:5:1] --- Pytho
            s[0:5:2] --- Pto

"""
# 字符串 --- 基本操作 ---> 不可变的（无法修改）
s = "Hello-Python"

print(s[4])  # 正向索引
print(s[-8])  # 反向索引

for i in s:
    print(i)

# 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:1])
print(s[6::1])

# 步长 ---> 正数：从前往后；  负数：从后往前
print(s[-1:-7:-1])
print(s[::-1])


"""

字符串-常用方法
    find()      在字符串中查找子串，返回第一次出现的索引位置，找不到就返回-1  s.find('Python')
    count()     统计子串在字符串中出现的次数                               s.count('H')
    upper()     将字符串中所有字母转换为大写                               s.upper()
    lower()     将字符串中所有字母转换为小写                               s.lower()
    split()     将字符串按指定分隔符分割成列表                             s.split()
    strip()     去除字符串两边的空白字符或指定字符                         s.strip()/s.strip('*')
    replace()   将字符串中的指定子串替换为新的子串                          s.replace('H','C')
    startswith() 检查字符串是否以指定子串开头，返回布尔值                   s.startwith('P')

"""

# --------------------------------------- 字符串常用方法 ------------------------------------------
s = "Hello-Python-Hello-World"

index = s.find("-")
print(index)   #index = 5

c = s.count("o")
print(c)       #c = 4

su = s.upper()
print(su)       # HELLO-PYTHON-HELLO-WORLD

sl = s.lower()
print(sl)       # hello-python-hello-world

slist = s.split("-")
print(slist)    # ['Hello', 'Python', 'Hello', 'World']

ss = s.strip()
print(ss)       # Hello-Python-Hello-World

sr = s.replace("-","_") 
print(sr)       # Hello_Python_Hello_World

print(s.startswith("Hello"))  # True
print(s.endswith("Python"))  # False

# ------------------------------------- 字符串案例 ------------------------------------------------
# Question 1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确
#           （包含一个@和至少一个.），若正确，则输出“邮箱格式正确”，反之输出“错误”
# 方式1：
mail = input("请输入邮箱：")

if mail .count("@") == 1 and mail.count(".") >= 1:
    print(f"{mail}是合法的邮箱")
else:
    print(f"{mail}是非法的邮箱")

# 方式2：  in 运算符 ---> 判断子串是否存在于字符串中，返回bool值
mail = input("请输入邮箱：")

if mail .count("@") == 1 and "." in mail:
    print(f"{mail}是合法的邮箱")
else:
    print(f"{mail}是非法的邮箱")

# Question 2：输入一个字符串，判断该字符串是否是回文（两边对称）
# 黄三落叶落山黄；  上海自来水来自海上
str_1 = input("请输入一串字符串：")

str_2 = str_1[-1::-1]
if str_1 == str_2:
    print("该字符串是回文结构")
else:
    print("该字符串不是回文结构")

# Question 3：将用户输入的10个字符串，反转后全部转换为大写
#             然后记录在列表中，最后将列表内容，遍历输出出来
lst = []

for i in range(10):
    text = input("请输入10个字符串：")
    lst.append(text)

reverse_lst = lst[::-1]

upper_list = []
for word in reverse_lst:
    upper_list.append(word.upper())

print("反转并全部大写后的列表：",upper_list)