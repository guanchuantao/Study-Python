# @author :  Chuantao.Guan
# @time : 2023-03-26
# @file : handle_operation.py
# @describe : 运算操作（加、减、乘、除、整除、取余、幂运算、赋值、加赋值、减赋值、大于、小于、等于、不等于、大于等于、小于等于、且、或、非）


# 加法操作
a = 5
b = 3
c = a + b
print(c)  # 8

# 减法操作
a = 5
b = 3
c = a - b
print(c)  # 2

# 乘法操作
a = 5
b = 3
c = a * b
print(c)  # 15

# 除法操作
a = 5
b = 3
c = a / b
print(c)  # 1.6666666666666667

# 整除操作
a = 5
b = 3
c = a // b
print(c)  # 1

# 取余操作
a = 5
b = 3
c = a % b
print(c)  # 2

# 幂运算操作
a = 5
b = 3
c = a ** b
print(c)  # 125

# 赋值操作
a = 5
b = a
print(b)  # 5

# 加赋值操作
a = 5
a += 3
print(a)  # 8

# 减赋值操作
a = 5
a -= 3
print(a)  # 2

# 大于操作
a = 5
b = 3
c = a > b
print(c)  # True

# 小于操作
a = 5
b = 3
c = a < b
print(c)  # False

# 等于操作
a = 5
b = 3
c = a == b
print(c)  # False

# 不等于操作
a = 5
b = 3
c = a != b
print(c)  # True

# 大于等于操作
a = 5
b = 3
c = a >= b
print(c)  # True

# 小于等于操作
a = 5
b = 3
c = a <= b
print(c)  # False

# 且操作
a = 5
b = 3
c = a > b and b < 10
print(c)  # True

# 或操作
a = 5
b = 3
c = a > b or b < 10
print(c)  # True

# 非操作
a = 5
b = 3
c = not (a > b)
print(c)  # False
