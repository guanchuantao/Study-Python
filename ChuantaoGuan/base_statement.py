# @author :  Chuantao.Guan
# @time : 2023-03-26
# @file : base_statement.py
# @describe : 基本循环、判断语句

# 基本循环语句
# while循环语句
# while 判断条件：
#     执行语句
# else:
#     执行语句
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("i is no longer less than 5")

# for循环语句
# for iterating_var in sequence:
#     statements(s)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# break语句
# while 判断条件：
#     执行语句
#     if 条件语句：
#         break  # 跳出循环
# else：
#     执行语句
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

# continue语句
# while 判断条件：
#     执行语句
#     if 条件语句：
#         continue  # 跳过本次循环
# else：
#     执行语句
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# pass语句
# while 判断条件：
#     pass
# else：
#     执行语句
i = 1
while i < 5:
    pass
    i += 1
else:
    print("i is no longer less than 5")

# 判断语句
# if 判断条件：
#     执行语句
# elif 判断条件：
#     执行语句
# else:
#     执行语句
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


