# @author :  Hao.Li
# @time : 2023-03-18
# @file : fp_two.py
# @describe :
# while语句
# 举例说明,100以内求和
i = 1
s = 0
while i <= 100:
    s = i + s
    i += 1

print(s)

# while else
i = 1
s = 0
n = 1
while i <= 100:
    s = i + s
    i += 1
else:
    n = i - n
    i -= 1
print(n)
print(s)

# for语句,for循环也是遍历
# 找水仙花数第一步，找范围选数
for a in range(100, 1000):
    x = a // 100
    y = a // 10 - a // 100 * 10
    z = a - a // 10 * 10
    if x ** 3 + y ** 3 + z ** 3 == a:
        print(a)
# break语句则是在打破循环，以上式为例，若是只取一个水仙花数的情况下，可添加一个break
for a in range(100, 1000):
    x = a // 100
    y = a // 10 - a // 100 * 10
    z = a - a // 10 * 10
    if x ** 3 + y ** 3 + z ** 3 == a:
        print(a)
        break
# continue语句,跳出本次循环

for m in range(- 1, 10):
    n = 100
    if m == 0:
        continue
    l = n / m
    print(l)

# pass语句是直接跳过这个语句，而且不报错
for m in range(- 1, 10):
    if m == 6:
        pass
    print(m)

# for遍历列表元素
lst = [1, 8, 3, 52, 83, 183, 789]
for i in lst:
    print(i)

# 使用for循环生成列表
list_lst = [i % 6 for i in lst ]
print(list_lst)



