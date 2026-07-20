# 字面量的写法
print(100) # 整数(int)
print(3.14) # 浮点数(float)
print(True) # 布尔值(bool)
print(False) # 布尔值(bool)
print('Hello World!') # 字符串(str)
print("---------------") # 字符串(str)
print(None) # 空值(NoneType)

# 布尔类型本质也是整数类型，True等于1，False等于0
print(True + 1)  # 输出: 2
print(False - 1) # 输出: -1


# 变量 ---->Python是动态类型语言，一个变量可以存储不同类型的值（但是项目开发中，推荐一个变量只存储一种类型的值）
num = 1114.1
print(num)

num = num + 1
print(num)

num = "OK"
print(num)

num = True
print(num)

a,b = 1,"python"
print(a)
print(b)

#Question 1
#课程基础播放量为：20.7万，每月新增播放量为：50万，请输出未来两个月每个月的播放总量。
# 方案1
base = 20.7 #基础播放量
incr = 50 #每月新增播放量
print("未来第一个月的播放总量为：", base + incr, "万")
print("未来第二个月的播放总量为：", base + incr * 2, "万")

# 方案2
base,incr = 20.7,50
print("未来第一个月的播放总量为：", base + incr, "万")
print("未来第二个月的播放总量为:", base + incr + incr, "万")


#变量交换 ---->Python中变量交换非常简单，直接使用 a,b = b,a 即可
a,b,c = 100,200,300
a,b,c = c,a,b
print(a,b,c) 