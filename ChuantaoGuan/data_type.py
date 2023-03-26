# @author :  Chuantao.Guan
# @time : 2023-03-26
# @file : data_type.py
# @describe : 掌握数据基本类型、定义方式和要求、类型之间互转


# 不同类型的数据
# 定义不同类型的数据
a = 10  # 整数类型，定义方式为直接赋值
b = 3.14  # 浮点数类型，定义方式为直接赋值
c = True  # 布尔类型，定义方式为直接赋值
d = "Hello, World!"  # 字符串类型，定义方式为直接赋值
e = [1, 2, 3, 4, 5]  # 列表类型，定义方式为用中括号括起来，元素之间用逗号隔开
f = (1, 2, 3, 4, 5)  # 元组类型，定义方式为用小括号括起来，元素之间用逗号隔开
g = {1, 2, 3, 4, 5}  # 集合类型，定义方式为用大括号括起来，元素之间用逗号隔开
h = {"name": "John", "age": 30, "city": "New York"}  # 字典类型，定义方式为用大括号括起来，元素之间用逗号隔开，每个元素由键和值组成，用冒号隔开

# 数据类型转换
i = float(a)  # 将整数类型转换为浮点数类型
j = int(b)  # 将浮点数类型转换为整数类型
k = bool(a)  # 将整数类型转换为布尔类型
l = int(c)  # 将布尔类型转换为整数类型
m = list(d)  # 将字符串类型转换为列表类型
n = tuple(e)  # 将列表类型转换为元组类型
o = set(f)  # 将元组类型转换为集合类型
p = list(g)  # 将集合类型转换为列表类型
q = list(h)  # 将字典类型转换为列表类型
r = dict(zip(h.keys(), h.values()))  # 将字典类型转换为字典类型

# 打印数据类型和转换后的结果
print(type(a), i)
print(type(b), j)
print(type(c), k)
print(type(d), m)
print(type(e), n)
print(type(f), o)
print(type(g), p)
print(type(h), q)
print(type(r), r)


