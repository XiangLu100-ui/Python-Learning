"""

    案例1： 根据输入的用户名与密码执行登录操作，具体要求如下：
        1.正确的用户名和密码为admin/666888,zhangsan/123456,taoge/888666
        2.输入用户名和密码进行登录，直到登录成功，程序结束运行；若登录失败，则继续输入用户名和密码进行登录
        3.输入的用户名和密码不能为空！
        4.登录成功，输出“登陆成功，进入B站首页~”
        5.登录失败，输出“用户名和密码错误，请重新输入！”

    关键字：
        break：用于循环正确时，可直接跳出循环，结束循环的运行
        continue：只用于循环中，表示中断本次循环，直接进入下一次循环

"""

while True:

    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")

    if username == "" or password == "":
        print("输入的用户名或密码不能为空！请重新输入")
        continue

    if username == "admin" and password == "666888":
        print("登录成功！进入B站首页~")
        break

    elif username == "zhangsan" and password == "123456":
        print("登录成功！进入B站首页~")
        break

    elif username == "taoge" and password == "888666":
        print("登录成功！进入B站首页~")
        break

    else:
        print("用户名或密码错误，请重新输入！")

"""

    需求：
        用户名密码登录，正确的用户名和密码为admin/666888,zhangsan/123456,taoge/888666
        有5次登录机会，输入错误5次，就不允许再操作了

"""
i = 0
while (i < 5):

    print(f"您有{5 - i}次登录机会，请谨慎输入信息")
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    
    if username == "" or password == "":
        print("输入的用户名或密码不能为空！请重新输入")
        i += 1
        continue

    elif username == "admin" and password == "666888":
        print("登录成功！已进入B站首页~")
        break

    elif username == "zhangsan" and password == "123456":
        print("登录成功！已进入B站首页~")
        break

    elif username == "taoge" and password == "888666":
        print("登录成功！已进入B站首页~")
        break

    else:
        print("用户名或密码错误！请重新输入")
        i += 1

print("很抱歉，请等待1小时后再次输入！")