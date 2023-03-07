# @author : Chuantao.Guan
# @time : $(YEAR}-03-07
# @file : task_k2.py
# @describe :

# 基本的运算操作(加、减、乘、除、整除、取余、幂运算、赋值、加赋值、减赋值、大于、小于、等于、不等于、大于等于、小于等于、且、或、非)
a = 66
b = 88

# 加法
c = a+b
print("a+b=",c)
# 运行结果为a+b= 154

# 减法
c = a-b
print("a-b=",c)
# 运行结果为a-b= -22

# 乘法
c = a*b
print("a*b=",c)
# 运行结果为a*b= 5808

# 除法
c = a/b
print("a/b=",c)
# 运行结果为a/b= 0.75

# 整除运算
c = a//b
print("a//b=",c)
# 运行结果为a//b= 0

# 取余运算
c = a%b
print("a%b=",c)
# 运行结果为a%b= 66

# 幂运算
c = a**b
print("a**b=",c)
# 运行结果为a**b= 13178510522716872655319238066254261900640428904597084991...

c = 99
# 加赋值运算
c+=a
print("c+=a的值为",c)
# 运行结果为 c+=a的值为 165

c = 99
# 减赋值运算
c-=a
print("c-=a的值为",c)
# 运算结果为 c-=a的值为 33

# 大于
if a>b:
    print("a大于b")
# 小于
if a<b:
    print("a小于b")
# 等于
if a==b:
    print("a等于b")
# 不等于
if a!=b:
    print("a不等于b")
# 大于等于
if a>=b:
    print("a大于等于b")
# 小于等于
if a<=b:
    print("a小于等于b")
# ”且“操作
if a>b and b>6:
    print("a大于b且b大于6")
# ”或“操作
if a>b or b>6:
    print("a大于b或b大于6")
# ”非“操作
if not(a>b):
    print("a不大于b")

# 判断语句（if，else,elif)

a = 6666

if (a%6==0) or (a/8)>211:
    print("a满足条件被6整除或者a的八分之一大于211")
elif (a%8==0) and (a/7)>211:
    print("满足条件被8整除且a的六分之一大于211")
else:
    print("a啥也不是")

