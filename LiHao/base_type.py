# @author :  Hao.Li
# @time : 2023-03-16
# @file : base_type.py
# @describe : 这个地方是写基本数据类型的


#int
a = 314

# float
b = 3.14159

#bool
c = True
d = False

# string
e = 'longstings'
print(e, type(e))
# list
f = [1,2,3,4,5]
print(type(f))
# 元组类型
g = (1,2,3,4,5,6)
tup_g = tuple('123456')
print(tup_g, type(tup_g))
# 集合类型
h = {1,'ac',2}
set_h = set(g)
print(h, type(h))
# 字典类型
j = {'天':'地','雨':'风','大陆':'长空',5:6}
print(j, type(j))
# 类型互转
# int类型转
a = float(a)
# 整数转浮点
print(type(a))
a = bool(a)
# 整数转bool
print(type(a))
a = str(a)
# 整数转字符串
print(type(a))

# float类型转
b = int(b)
# 浮点转整数
print(type(b))
b = bool(b)
# 浮点转bool
print(type(b))
b = str(b)
# 浮点转字符串
print(type(b))
c = int(c)
d = int(d)

# bool类型转
# bool转int只会出现0，1的结果
print(c, d, type(c))
c = float(bool(c))
# bool转float会出现后面加小数点的情况
print(c, type(c))
c = str(bool(c))
# bool转字符串
print(c, type(c))

# string类型转
# 可以转，当字符串内容为数字的时候



f = tuple(f)
# 列表类型转成元组
print(f, type(f))
f = set(list(f))
# 列表类型转成集合
print(f,type(f))

g = list(g)
# 元组转列表
print(g, type(g))
g = set(tuple(g))
# 元组转集合
print(g, type(g))

h = list(h)
# 集合转列表
print(h,type(h))
# 集合转元组
h = tuple(set(h))
print(h, type(h))

# 字典转集合
j = set(j)
# 只显示zhi
print(j)
# 字典转元组，显示值,元组不可以转字典
j = tuple(j)
print(j)
j = list(j)
# 字典转列表，显示值，列表不可以转字典
print(j)





