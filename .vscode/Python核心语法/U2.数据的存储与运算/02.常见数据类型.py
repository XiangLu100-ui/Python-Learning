# 常见数据类型 ----> type() 获取指定的字面量或变量的类型
print("Hello")
print(type("Hello")) # str

print(type(10)) # int
print(type(3.14)) # float
print(type(True)) # bool
print(type(False)) # bool
print(type(None)) # NoneType


# 常见数据类型 ----> isinstance()---> 判定数据是否是指定类型，如果是：True，否则：False
num = -100
print(type(num))
print(isinstance(num,int)) # True
print(isinstance(num,float)) # False
print(isinstance(num,bool)) # False


# 字符串
# 定义字符串的三种方式
s1 = "Hello" # 双引号定义
s2 = 'Python' # 单引号定义
s3 = """
Hello:
   欢迎大家来到Python的学习 ！
   请大家多多支持哦 ~
   """ # 三引号定义 （多行字符串）

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))


# 定义字符串 ----> It's a good day! 这种情况，单引号定义的字符串中包含了单引号，所以会报错
#s4 = 'It's a good day!' # 报错

#为了使用单引号定义的字符串中包含单引号，可以使用转义字符 \ 来解决

s4 = 'It\'s a good day!' # True
# 转义字符都有：
# \n - 换行
# \t - 制表符
# \\ - 反斜杠
# \' - 单引号
# \" - 双引号

msg1 = 'It\'s a good day!'
print(msg1)

msg2 = "It's a good day!"
print(msg2)

msg3 = "Hello 的意思就是\"你好\""
print(msg3)

print("\t欢迎大家来到Python的学习！\n\t请大家多多支持哦 ~")


# 字符串拼接
s1 = "人生苦短" "我用python" ",OK"
print(s1)

msg1 = "人生苦短"
msg2 = "我用python"
print("龟叔说：" + msg1 + "," + msg2)

# Question 1 ---> str() 将其他类型的数据转换为字符串类型
# 大家好，我是涛哥，今年18岁，学习专业是软件工程，爱好是Python、Java
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
message = "大家好，我是" + name + ", 今年" + str(age) + "岁，学习专业是" + pro + ",爱好是" + hobby
print(message)

# 字符串的拼接还可以使用格式化输出的方式来实现，即使用占位符，格式为（%占位符）
# 需要注意：前面有多少个占位符（%s），后面就需要有多少个变量与之对应，且顺序要一致
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print("大家好，我是%s，今年%s岁，学习专业是%s，爱好是%s" % (name,age,pro,hobby))

# 方式二：使用format()方法来实现字符串的拼接，即f“..{变量名/表达式}..” ---> 企业推荐
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print(f"大家好，我是{name}，今年{age}岁，学习专业是{pro}，爱好是{hobby}")