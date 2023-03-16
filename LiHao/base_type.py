# @author :  Hao.Li
# @time : 2023-03-16
# @file : base_type.py
# @describe : 这个地方是写基本数据类型的


#int
a=314

#float
b=3.14159

#bool
c= True
d= False

#string
e= 'longstings'
print(e,type(e))
#list
f= [1,2,3,4,5]
print(type(f))
#元组类型
g=(1,2,3,4,5,6)
g1=tuple('123456')
print(g1,type(g1))
#集合类型
h={1,'ac',2}
h1=set(g)
print(h,type(h))
#字典类型
j={'天':'地','雨':'风','大陆':'长空',5:6}
print(j,type(j))
#类型互转
#int类型转
a=float(a)
print(type(a))#整数转浮点
a=bool(a)
print(type(a))#整数转bool
a=str(a)
print(type(a))#整数转字符串

#float类型转
b=int(b)
print(type(b))#浮点转整数
b=bool(b)
print(type(b))#浮点转bool
b=str(b)
print(type(b))#浮点转字符串
c=int(c)
d=int(d)

#bool类型转
print(c,d,type(c))#bool转int只会出现0，1的结果
c=float(bool(c))
print(c,type(c))#bool转float会出现后面加小数点的情况
c=str(bool(c))
print(c,type(c))#bool转字符串

#string类型转
#不能转，但是程序不报错


f=tuple(f)
print(f,type(f))#列表类型转成元组
f=set(list(f))
print(f,type(f))#列表类型转成集合


g=list(g)
print(g,type(g))#元组转列表
g=set(tuple(g))
print(g,type(g))#元组转集合

h=list(h)
print(h,type(h))#集合转列表
h=tuple(set(h))#集合转元组
print(h,type(h))

j=set(j)#字典转集合
print(j)#只显示zhi
j=tuple(j)#字典转元组，显示值,元组不可以转字典
print(j)
j=list(j)
print(j)#字典转列表，显示值，列表不可以转字典





