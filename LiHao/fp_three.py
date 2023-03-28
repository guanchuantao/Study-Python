# @author :  Hao.Li
# @time : 2023-03-20
# @file : fp_three.py
# @describe :
# 定义一个函数
def a_num(a, b):
   a = a + b
   b = a * b
   return a * b
print(a_num(3,5))

# 学生信息输入
stu_infor= {
   '2021221260': {'姓名': '李四', '年龄' : '20','性别':'男', 'math_score':'81','高等代数':'96','解析几何':'89'},
   '2021221261': {'姓名': '张三', '年龄' : '21','性别':'男', 'math_score':'80','高等代数':'95','解析几何':'88'},
   '2021221262': {'姓名': '王五', '年龄' : '22','性别':'女', 'math_score':'88','高等代数':'95','解析几何':'82'},
   '2021221263': {'姓名': '赵六', '年龄' : '23','性别':'男', 'math_score':'86','高等代数':'97','解析几何':'81'},
   '2021221264': {'姓名': '麻七', '年龄' : '24','性别':'女', 'math_score':'89','高等代数':'91','解析几何':'83'}}

# 计算学生平均成绩
def stu_gra(stuent_id):
   # 获取学生数学分析成绩
   math_score = stu_infor[stuent_id]['math_score']
   # 获取学生高等代数成绩
   a_score = stu_infor[stuent_id]['高等代数']
   # 获取学生解析几何的成绩
   g_score = stu_infor[stuent_id]['解析几何']
   # 计算平均成绩
   stu_gra = (int(math_score) + int(a_score) + int(g_score))/3
   return stu_gra


# 定义函数，获取各科最高分
def high_score():
   # 获取数学分析最高分
   # key = lambda 是进行元素字段排序
   math_max = max(stu_infor, key=lambda x: stu_infor[x]['math_score'])
   # 获取数学分析最高分的学生姓名
   math_name = stu_infor[math_max]['姓名']
   # 获取高等代数最高分
   a_max = max(stu_infor, key=lambda x: stu_infor[x]['高等代数'])
   # 获取高等代数最高分的学生姓名
   a_name = stu_infor[a_max]['姓名']
   # 获取解析集合最高分
   g_max = max(stu_infor, key=lambda x: stu_infor[x]['解析几何'])
   # 获取解析几何最高分的学生姓名
   g_name = stu_infor[g_max]['姓名']
   return math_max, math_name, a_max, a_name, g_max, g_name


# 主函数
if __name__ == '__main__':
   # 先计算学生平均成绩
   print(stu_gra('2021221263'))
   # 再计算最高分
   print(high_score())






