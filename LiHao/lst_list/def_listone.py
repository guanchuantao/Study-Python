# @author :  Hao.Li
# @time : 2023-03-29
# @file : def_listone.py.py
# @describe :
class Avelst:
    # 这是一个计算平均值的类

        def average(self, lst):
            # 这里需要写一个异常捕获（捕获情况为：当出现lst传入的值不是int或者float，  m += i  会报错）
            try:
                m = 0
                for i in lst:
                    m += i
                return m / len(lst)
            except TypeError:
                print('请输入数字')









