# 算术运算符 ---> + - * / % // **
print("5 + 3 = ",5 + 3) # 8
print("5 - 3 = ",5 - 3) # 2
print("5 * 3 = ",5 * 3) # 15
print("5 / 3 = ",5 / 3) # 1.66
print("5 % 3 = ",5 % 3) # 2
print("5 // 3 = ",5 // 3) # 1
print("5 ** 3 = ",5 ** 3) # 125

# # Question 1 ---> 要求输入两个数x与y，分别输出x + y的结果和x - y的结果
x = float(input("请输入要的x值:"))
y = float(input("请输入要的y值:"))
print("得到的x + y的值为:",x + y)
print("得到的x - y的值为:",x - y)

# 0.09999999999999998 ---> 精度损失；由于计算机是基于 二进制 进行数据的存储与处理，二进制是无法准确的表示所有的小数，因此涉及到浮点数的运算，可能会损失精度。

# 算术运算符的优先级 --> (**) --> (* / // %)  --> (+ -)

# Question 2 ---> 计算输入的三个数的平均数
a = float(input("请输入a的数值："))
b = float(input("请输入b的数值："))
c = float(input("请输入c的数值："))
print("这三个数的平均值为：",(a + b + c)/3)

# Question 3 ---> 要求输入梯形的上底、下底、高，然后计算梯形的面积
Upper_bottom = float(input("请输入上底的大小："))
Bottom = float(input("请输入下底的大小："))
Height = float(input("请输入高的大小："))
print("该梯形的面积大小为：",(Upper_bottom + Bottom)*Height / 2)

# Question 4 --->要求输入圆的半径，然后计算圆的周长和面积（周长：2πr，面积：πr*2）
pi = 3.14
Radius = float(input("请输入圆的半径大小："))
print("该圆的周长为：",2 * pi *Radius)
print("该圆的面积为：",pi * Radius ** 2)

# Question 5 --->身体质量指数BMI的计算（BMI = 体重（kg）/ 身高（m）*2）
Weight = float(input("您的体重为(kg)："))
Height = float(input("您的身高为(m)："))
print("您的BMI值为：",Weight / Height ** 2)

# 赋值运算符 ---> +=  -=  *=  /=  //=  %=  **=

# 比较运算符 ---> ==  !=  >  >=  <  <=

# 逻辑运算符 ---> and(逻辑与，并且，即需要同时符合条件才行)  or(逻辑或，或者，只要一个符合条件即可)  not(逻辑非，取反，即True变成False，反之亦然)

# Question 1: 键盘输入一个整数，判断这个数是否在10到20之间
num = int(input("请输入一个整数："))
print(f"{num}在10到20之间：",num >= 10 and num <= 20)

# Question 2: 键盘上输入一个整数，判断这个数字是否不在10-20之间
num = int(input("请输入一个整数："))
print(f"{num}不在10到20之间：",num < 10 or num > 20)