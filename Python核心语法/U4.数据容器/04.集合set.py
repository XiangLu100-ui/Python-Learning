"""

集合（set）
    介绍：集合（set）是一种无序、不可重复、可修改的数据容器
    定义：
    # 定义集合：
    s1 = {"C", "D", "X", "T", "O", "U"}

    # 定义空集合：
    s2 = set()

    注意：空集合的定义不可以使用{}，{}代表的是空字典；
            由于集合是无序的，因此是不支持下标索引访问的

"""
# 定义 ---> 无序，不可重复，可修改
s1 = {5,3,2,0,9,12,43,64,22,5,0}

print(s1)
print(type(s1))

# 定义空集合
s2 = set()

print(s2)
print(type(s2))

"""

add(..)         添加元素到集合中                           s1.add('t')
remove(..)      移除集合中的指定元素（不存在会报错）        s1.remove('t')
pop()           随机删除集合中的元素并返回                  e = s1.pop()
clear()         清空集合                                  s1.clear()
difference()    求取两个集合的差集（包含在第一个集合但不包含在第二个集合的元素）s1.difference(s2)
union()         求取两个集合的并集                         s1.union(s2)
intersection()  求取两个集合的交集                         s1.intersection(s2)

"""
s1 = {100,200,300,400,500,600,700,800}
print(s1)

s1.add(1200)
print(s1)

s1.remove(200)
print(s1)

e = s1.pop()
print(e)
print(s1)

s1.clear()
print(s1)

s2 = {"A", "B", "C", "D", "E", "X", "Y"}
s3 = {"C", "E", "Y", "Z"}

print(s2.difference(s3))
print(s3.difference(s2))

print(s2.union(s3))
print(s3.union(s2))

print(s2.intersection(s3))
print(s3.intersection(s2))

# ---------------------------------集合 set 案例 ---------------------------------------------
# Question 1：根据提供的班级学生的选课情况，完成如下需求：
#         1.找出同时选修了法语和艺术的学生
#         2.找出同时选修了所有四门课程的学生
#         3.找出选修了足球，但是没有选修篮球的学生
#         4.统计每一个学生选修的课程数量
football_set = {"王林", "曾牛", "徐立国", "天运子", "韩丽", "武丑","紫灵" }
basketball_set = {"张秩", "王林", "姜老道", "曾牛", "韩丽", "丽华苑"}
french_set = {"许木", "王卓", "姜老道", "天运子", "韩丽", "曾牛"}
art_set = {"天运子", "韩丽", "姜老道", "紫灵", "遁天", "虎跑"}

print(french_set.intersection(art_set)) 
#⬆️或者可用& ---> 交集 即french_set & art_set

all_set = football_set & basketball_set & french_set & art_set
print(f"{all_set}")

print(football_set.difference(basketball_set)) 
#⬆️或者可用- ---> 差集 即football_set - basketball_set
#⬆️或者可用“集合推导式” ---> 快速构建集合 即{s for s in football_set if s not in basketball_set}

all_set = football_set.union(basketball_set).union(french_set).union(art_set)
#⬆️或者可用并集 --> ( | ) 即football_set | basketball_set | french_set | art_set
all_list = [*football_set, *basketball_set, *french_set, *art_set]
for s in all_set:
    print(f"{s} 选修了 {all_list.count(s)} 课程")