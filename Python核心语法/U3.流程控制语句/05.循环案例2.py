"""
    猜数字游戏：
        1.系统随机生成一个随机数
        2.用户根据提示猜数字，并将所猜的数字输入系统
        3.如果猜错，系统会给出提示是猜大了，还是猜小了，然后继续输入猜的数字
        4.如果猜对，系统自动退出，游戏结束

    关键字：
        import random       导入模块，和先下定义类似
        random_number = random.randint(a:1, b:100)    随机生成1-100的随机数，包含1和100

"""

import random
random_num = random.randint(1,100)

while True:

    x = int(input("请随机输入一个数字："))
    
    if x > random_num:
        print("您输入的数字太大了！")

    elif x < random_num:
        print("您输入的数字太小了！")

    else:
        print("！？这么强？！")
        break

# print(f"随机数字为{random_num}您输入的数字刚刚好~")

#  Question 1：将 1 - 1000 之间（含1000）所有5的倍数的数字累加起来
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print(f"总和为{total}")

#  Question 2：统计字符串“akijshwkcjslkekwicawkkshawjshajjekdhwc” 字符串中有多少个a和k
x=0
y=0
complex_str = "akijshwkcjslkekwicawkkshawjshajjekdhwc"
for i in complex_str:
    if i == 'a':
        x += 1
    elif i == 'k':
        y += 1
print(f"a的数量有{x}个")
print(f"k的数量有{y}个")