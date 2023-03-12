# @author : Yongqi.Kang
# @time : 2023-03-09
# @file : task3_k.py.py
# @describe :

# 循环语句（while,whlie else,for,break,continue,pass)
# while循环
count1 = 0
while count1 < 3:
    # 当count小于3时，执行循环体
    print(count1)
    count1 += 1
# 运行结果为 0 1 2

# while-else语句
count2 = 0
while count2 < 6:
    print(count2)
    count2 += 1
else:
    # 当while循环结束时，执行else语句
    print("循环结束")
# 运行结果为 0 1 2 3 4 5 循环结束

# for循环
list1 = ["one", "two", "three", "four"]
for number in list1:
    # 遍历列表中的所有元素
    print(number)
# 运行结果为 one two three four

# break语句
count3 = 0
while count3 < 10:
    count3 += 1
    if count3 == 6:
        # 本人总是在这写一个 = 号，要写两个！！！！！
        break
    # 这里是，最后一次输出count3=5时，跳出循环
    print(count3)
# 运行结果是 1 2 3 4 5

count4 = 0
while count4 < 10:
    count4 += 1
    print(count4)
    if count4 == 6:
        break
    # 当count3=6时，跳出循环
# 运行结果为 1 2 3 4 5 6

# continue语句
count5 = 0
while count5 < 16:
    count5 += 1
    if (count5 % 2) == 0:
        continue
    # 当count5可以被2整除时，跳出本次循环
    print(count5)


# 运输结果为 1 3 5 7 9 11

# pass语句
def empty_function():
    pass


# pass语句表示什么都不做，占位符号，保证代码正确
# 调用函数，空函数，不会输出任何函数
empty_function()

# 使用for循环遍历列表里面每一个元素
fruits = ["apple", "pear", "banana", "grape"]
i = 0
extent = len(fruits)
for i in range(extent):
    print(fruits[i])
    i += 1
# 运行结果为 apple pear banana grape

# 使用for循环生成列表

list_length = 10
list2 = []
for i in range(list_length):
    # list2[i] = i 该写法错误
    list2.append(i)
print(list2)

list_test = [i for i in range(list_length)]
print('list_test', list_test)

# 运行结果为 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
