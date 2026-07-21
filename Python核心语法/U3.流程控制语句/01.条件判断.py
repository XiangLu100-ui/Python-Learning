# if条件判断：只有满足指定条件，才会执行对应的代码逻辑
# Question 1：如果我的分数超过695，我就去清华读书
score = 695
if score >= 695:
    print("欢迎你来到清华读书！")
    print("也恭喜你即将踏入精彩的大学生活！")
print("-----------------------")

# 通过前面的缩进来判断if的归属，如最后一行即使False也会输出

# Question 2：结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现（正确账号和密码为18888888/666888）
a = int(input("请输入您的账号（8位数）："))
b = int(input("请输入您的该账户密码（共6位）："))
if a == 18888888 and b == 666888 :
    print("恭喜!登陆成功")
    print("已进入B站首页~")

if a != 18888888 or b != 666888 :
    print("很抱歉，账户或密码错误")
    print("请重新输入账号或密码")

# if语句的进阶：if-else
 #格式： if 要判断的条件:
            #条件成立时，执行对应的操作一
       # else:
            #条件不成立时，执行的操作二
 
a = int(input("请输入您的账号（8位数）："))
b = int(input("请输入您的该账户密码（共6位）："))
if a == 18888888 and b == 666888 :
    print("恭喜!登陆成功")
    print("已进入B站首页~")

else:
    print("很抱歉，账户或密码错误")
    print("请重新输入账号或密码")

# Question 3：根据用户输入的年份，判断这一年是闰年还是平年（非整百年份，且能被4整除的年份是闰年；整百年必须被400整除才是闰年）
year = int(input("请输入您想要查询的年份："))
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year}年份为闰年")
else:
    print(f"{year}年份为平年")

# Question 4: 根据用户输入的数字，判断该数字是奇数还是偶数
num = float(input("请您随机输入一个数："))
if num.is_integer():
    if int(num) % 2 == 0:
        print(f"{int(num)}是偶数")
    else:
        print(f"{int(num)}是奇数")
else:
    print(f"{num}既不是奇数也不是偶数")

# # Question 5：根据用户输入的年龄，判断该用户是否已经成年
age = int(input("请输入您的年龄："))
if age >= 18:
    print("该用户已经成年")
else:
    print("该用户为未成年")

# if...elif...else... 可用来进行多条件的判断，elif可以进行多次
# # Question 6：根据用户输入的数字，判断该数字是正数还是负数
num = float(input("请您随机输入一个数字："))
if num >= 0:
    print("该数字为正数")
elif num == 0:
    print("该数字为既不是正数也不是负数")
else:
    print("该数字为负数")

# Question 7：根据用户输入的考试分数，判断该分数是否及格
mark = float(input("请输入您这次考试的得分："))
if mark >= 85:
    print("优秀")
elif mark >=75 and mark < 85:
    print("良好")
elif mark >=60 and mark < 75:
    print("合格")
else:
    print("不合格")

# Question 8：根据输入用户名、密码进行登录系统。
# #（用户名、密码为 admin/666888 或 root/547527 或 zhangsan/123456，则输出登录成功
# # 否则就提示用户名或密码错误
account = input("请输入您的账户用户名：")
password = int(input("请输入您的账户密码："))
if account =="admin" and password == 666888:
    print("用户名、密码正确，恭喜您登录成功")
elif account == "root" and password == 547527:
    print("用户名、密码正确，恭喜您登录成功")
elif account == "zhangsan" and password == 123456:
    print("用户名、密码正确，恭喜您登录成功")
else:
    print("很抱歉，您的用户名或密码输入错误，请重新尝试")

# Question 9:购物折扣计算：根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
# # 金额 >= 500: 8折； 300 <= 金额 <=500：9折；
# # 100 <= 金额 <=300：95折； 金额 <= 100：无折扣。
consumption = float(input("请输入您这次消费的金额为（元）："))
if consumption >= 500:
    print("谢谢惠顾！您这次的折扣为8折，消费共计%s"% (consumption*0.8))
elif 300 <= consumption <= 500:
    print("谢谢惠顾！您这次的折扣为9折，消费共计%s"% (consumption*0.9))
elif 100 <= consumption <= 300:
    print("谢谢惠顾！您这次的折扣为95折，消费共计%s"% (consumption*0.95))
else:
    print(f"谢谢惠顾！您这次的消费共计{consumption}")

# Question 10：根据输入的三个边的边长（正整数），判定是：
# # 等边三角形、等腰三角形、普通三角形，还是不能构成三角形
a = float(input("请输入第一个边的长度："))
b = float(input("请输入第二个边的长度："))
c = float(input("请输入第三个边的长度："))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:  
        if a == b == c:
            print("等边三角形")
        elif a == b or a == c or b == c:
            print("等腰三角形")
        else:
            print("普通三角形")
    else:
        print("这三条边不能构成三角形")
else:
    print(f"{a} {b} {c}这三条边存在0或负数，不能构成图形")

# 根据输入的用电度数，计算电费：
# # 阶梯电价规则：第一档：2880度以下，电费单价0.4883元/度
# # 第二档：2880--4800度，电费单价0.5383元/度；第三档：4800度以上，电费单价0.7883元/度
elec_consump = float(input("请输入您已使用的用电度数："))
if elec_consump < 2880:
    print("您所需要支付的电费为：%s 元"% (elec_consump * 0.4883))
elif 2880 <= elec_consump < 4880:
    print("您所需要支付的电费为：%s 元"% (elec_consump * 0.5383))
else:
    print("您所需要支付的电费为：%s 元"% (elec_consump * 0.7883))