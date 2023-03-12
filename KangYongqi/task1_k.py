# @author : Yongqi.Kang
# @time : 2023-03-07
# @file : task1_k.py
# @describe :

# 列表，元组，集合，字典类型数据的操作（添加数据，删除数据，替换数据，查询数据，判断某数据是否存在该列表中）
# 列表类型的数据操作
my_list = [1, 2, 3, 4, 5, 6]

# 在列表末尾添加数据
my_list.append(7)
print(my_list)
# 运行结果——>[1,2,3,4,5,6,7]

# 删除列表中的指定元素
my_list.remove(7)
print(my_list)
# 运行结果——>[1,2,3,4,5,6]

# 替换掉列表中指定下标的元素
my_list[5] = 8
print(my_list)
# 运行结果——>[1,2,3,4,5,8]

# 查询列表中指定元素的索引值，即下标,没有即查找错误
index = my_list.index(5)
print(index)
# 结果4

# 判断某个元素是否存在于列表中
if 8 in my_list:
    print("8在列表中")
else:
    print("8不在列表中")
# 结果——>8在列表中

# 元组类型数据的操作
my_tuple = (1, 2, 3, 4, 5)
# 元组不支持添加、删除和替换元素的操作，但可以查询元素是否存在，方法类似列表
if 6 in my_tuple:
    print("6在元组中")
else:
    print('6' + "不在元组中")
# 结果——>6不在元组中

# 集合类型数据的操作
my_set = {1, 2, 3, 4, 5, 6}

# 添加元素到集合中，添加的重复元元素不会生效
my_set.add(8)
print(my_set)
# 结果为{1, 2, 3, 4, 5, 6, 8}

# 删除集合中指定的元素，元素不存在就会报错
my_set.remove(3)
print(my_set)
# {1, 2, 4, 5, 6, 8}

# 集合中不支持替换元素的替换

# 查询元素是否存在于集合中
if 5 in my_set:
    print("5在集合中")
else:
    print("5不在集合中")
# 5在集合中

# 字典数据类型
my_dict = {"name": "KYQ", "age": 21, "gender": "male"}

# 添加键与值到字典中
my_dict["city"] = "Anhui"
print(my_dict)
# 结果为{'name': 'KYQ', 'age': 21, 'gender': 'male', 'city': 'Anhui'}

# 删除字典中指定键对应的键值，若键不存在则报错
del my_dict["gender"]
print(my_dict)
# 输出的结果为{'name': 'KYQ', 'age': 21, 'city': 'Anhui'}

# 替换字典指定键对应的键值对，若键不存在则报错
my_dict["age"] = 999
print(my_dict)
# 运行结果为{'name': 'KYQ', 'age': 999, 'city': 'Anhui'}

# 查询字典中指定键对应的值，不存在就报错
age = my_dict["age"]
print(age)
# 运行结果是999

# 判断字典中是否存在指定键
if "gender" in my_dict:
    print("字典中存在gender这个键")
else:
    print("字典中不存在gender这个键")
