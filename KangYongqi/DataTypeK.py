# @author :  Chuantao.Guan
# @time : 2023-03-05
# @describe : 这个文件是康永棋写python数据类型的地方

# Python基本数据类型的初始定义方式

# 整数类型int
a = 666

# 浮点类型float
b = 3.1444

# 布尔类型bool
c = True

# 字符串类型str
d = "hello,world! "

# 列表类型list
e = [6,7,8,'六']

# 元组类型tuple
f = (1,6,'liu',6.6)

# 字典类型dict
g = {"六":6,"liu":"六"}

# 类型之间的转换
# 将整数类型转换为浮点类型
h = float(a)
print(h,type(h))

# 将浮点类型转换为整数类型
i = int(b)
print(i,type(i))

# 将字符串类型转换为整数类型
j = int("666666")
print(j,type(j))

# 将整数类型转换为字符串类型
k = str(88888888)
print(k,type(k))

# 将列表类型转换为元组类型
l = tuple(e)
print(l,type(l))

# 将元组类型转换为列表类型
m = list(f)
print(m,type(m))

# 将字典类型转换为列表类型
n = list(g)
print(n,type(n))