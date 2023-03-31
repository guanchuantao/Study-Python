# @author :  Hao.Li
# @time : 2023-03-29
# @file : fp_four.py
# @describe :
# 类

# 从相同目录下lst_list包中引入def_listone模块
from lst_list import def_listone

# 实例化Avelst类
Avelst = def_listone.Avelst()

x = [1, 'a', 6, 9]
# 通过实例化的Avelst类，调用average方法
print(Avelst.average(x))

