# @author :  Chuantao.Guan
# @time : 2023-03-05
# @describe : 这个文件是魏子豪写python数据类型的地方
#整数类型
a=1234
#浮点类型
b=3.1415926
#布尔类型
c=True
#字符串类型
d="abcd"
#元组类型
e=(1,2,3,"wei",b)
#字典类型
f={"wei":1,"guan":1}
#列表类型
gg=[6,7,8]
#强制类型转换
#整数转换为浮点类型
g=float(a)
print(g,type(g))
#浮点转换为整数类型
h=int(b)
print(h,type(h))
#将整数类型转换为字符串类型
I=str(11111)
print(I,type(I))
#将列表类型转换为元组类型
J=tuple(gg)
print(J,type(J))
#将元组类型转换为列表类型
K=list(e)
print(K,type(K))
#将字典类型转换为列表类型
L=list(f)
print(L,type(L))

