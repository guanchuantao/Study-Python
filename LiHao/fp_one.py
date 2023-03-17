# @author :  Hao.Li
# @time : 2023-03-16
# @file : fp1.py
# @describe :
# 列出列表、元组、字典、集合
lst = [2, 4, '张三', 'abc']
tup = (1, 3, 5, '李四', 'bcd',)

dic = {'天': '地', '雨': '风', 'ab': 'cd',5:6 }
se = {3, 5, 54, 'abd', '王五'}
# 列表数据变化
# del是根据索引删除目标，从0开始计数
del lst[2]
print(lst)
# pop是随机删除一项
lst.pop()
print(lst)
# remove是默认移除第一个，但是可指定移除
lst.remove(2)
print(lst)
# clear清空列表内容
# 列表添加数据一般
# append()在列表后面添加数据，列表都可以,但是一次只能添加一个元素
lst.append(['dadada', 'lalala'])
lst.append(5)
print(lst)
# extend属于添加进列表中的数据，如果是列表则一一添加
lst.extend('235')
lst.extend([3, 5, 6])
print(lst)
# 列表替换数据有多种方式
# 直接替换单个或者多个，按照索引进行替换
lst[2] = 44
print(lst)
# 索引列表替换列表，索引数字替换数字
lst[3:] = [666]
print(lst)
# 数据查询方式，一般函数进行判断
# index指定查询,但是返回索引的位置
print(lst.index(44))
# count查询列表中重复数据的次数
lst.append(666)
print(lst.count(666))
# 查询数据是否在列表中，可以用count，或者if或者for循环
if 666 in lst:
    print('666存在')
else:
    print('none')

# 元组是一个不可变对象，不接受单个元素的删除，替换，想要添加数据只能进行元组与元组之间的添加
tup1 = (555,666,999)
print(tup+tup1)
# 进行索引查找元素
print(tup[2])
# 判断元素是否在元组中，采用in、if进行判断
if 3 in tup:
    print('存在')

# 集合中的数据更改
# 集合中添加元素一般是add（）函数,但是集合序列数无序的，位置会随机变化
se.add(100)
print(se)
# 集合中可以添加元组，列表等元素,用update
se.update([22], (6546,), {246:557})
print(se)
# 集合中删除元素，有remove，pop,discard
# remove删除指定元素，不接受索引，没有这个元素会报错
se.remove(3)
se.discard(6546)
print(se)
# pop删除第一个元素
se.pop()
print(se)
# 集合中由于数据的无序，不能通过索引直接替换元素，需要替换元组可以转换成列表的模式进行替换
# 集合中查找元素也是通过if in的函数方法来进行判断。

# 字典中的键值对数据变换
# 字典中添加元素
# 直接添加
dic['春'] = '冬'
print(dic)
# update可以添加元素也可以在输入的时候，根据相同的键会进行替换原来的值
dic.update({'冬天': '春来'})
print(dic)
# 字典中删除元素,删除键值对中删除键会删除值，删除值没有反应
del[dic['冬天']]
print(dic)
# pop可以删除指定key
dic.pop('ab')
print(dic)
# 替换键值对中的值可以用update或者直接替换的方法进行替换，但是替换键的时候，就需要用pop函数了
dic[8]=dic.pop(5)
print(dic)

#数字运算
a = 666
b = 222
c = 212
d = a / b
# 赋值运算
a += b
b -= c
c = a * b
# 取余数
e = 10 // 3
#幂运算
f = 3**3
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# 比较运算 >,<,==,<=,>=
print(a > b)
a == b
# 不等于
a != b
# 逻辑运算
# and是两边都为真的时候才是报True
print(a ==b and c>=d)
# or是两边都为jia的时候才是报True
print(a ==b or c >= d)
# not属于bool运算，返回已有值相反的变化
a = True
print(not a)

x = int(input('请输入一个数：'))
y = int(input('请输入一个数：'))
if x > y:
    print(x+y)
elif x < y:
    print(x**2)
else:
    print(x+y**2)
# 要是输入的不是数字如何修改提醒输入者输入错误

