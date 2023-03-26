# @author :  Chuantao.Guan
# @time : 2023-03-26
# @file : question_1.py
# @describe :

"""
1、自定义函数（
def 函数名(入参列表):
    //实现特定功能的多行代码
    [return [返回值]]/[pass]
）
2、定义一个全局变量和两个函数：全局变量为存储学生信息，包含内容有学生学号、姓名、年龄、性别、数学分析考试分数、高等代数考试分数、解析几何考试分数（全局变量类型可由列表、元组、集合、字典中类型任意），并且该全局变量需要输入有五条数据；
定义的第一个函数：入参为学生学号，输出内容为该学生数学分析、高等代数、解析几何三门课考试平均分；
定义的第二个函数：无需传入参数，输出内容为该全局变量中数学分析、高等代数、解析几何分别最高分的学生的学号、姓名
要求：构建main函数（if __name__ == '__main__':）对以上两个函数进行调用，并且输出打印返回内容
"""


# 定义函数，计算学生平均分
def avg_score(student_id):
    # 获取学生数学成绩
    math_score = student_info[student_id]['math_score']
    # 获取学生代数成绩
    algebra_score = student_info[student_id]['algebra_score']
    # 获取学生几何成绩
    geometry_score = student_info[student_id]['geometry_score']
    # 计算学生平均分
    avg_score = (math_score + algebra_score + geometry_score) / 3
    # 返回学生平均分
    return avg_score


# 定义函数，获取最高分
def highest_score():
    # 获取数学最高分
    math_max = max(student_info, key=lambda x: student_info[x]['math_score'])
    # 获取数学最高分的学生姓名
    math_name = student_info[math_max]['name']
    # 获取代数最高分
    algebra_max = max(student_info, key=lambda x: student_info[x]['algebra_score'])
    # 获取代数最高分的学生姓名
    algebra_name = student_info[algebra_max]['name']
    # 获取几何最高分
    geometry_max = max(student_info, key=lambda x: student_info[x]['geometry_score'])
    # 获取几何最高分的学生姓名
    geometry_name = student_info[geometry_max]['name']
    # 返回最高分及其对应的学生姓名
    return math_max, math_name, algebra_max, algebra_name, geometry_max, geometry_name


# 定义学生信息字典
student_info = {
    '001': {'name': 'Tom', 'age': 18, 'gender': 'male', 'math_score': 90, 'algebra_score': 80, 'geometry_score': 70},
    '002': {'name': 'Jerry', 'age': 19, 'gender': 'male', 'math_score': 80, 'algebra_score': 70, 'geometry_score': 60},
    '003': {'name': 'Lucy', 'age': 20, 'gender': 'female', 'math_score': 70, 'algebra_score': 60, 'geometry_score': 50},
    '004': {'name': 'Lily', 'age': 21, 'gender': 'female', 'math_score': 60, 'algebra_score': 50, 'geometry_score': 40},
    '005': {'name': 'Bob', 'age': 22, 'gender': 'male', 'math_score': 50, 'algebra_score': 40, 'geometry_score': 30}
}

# 主函数
if __name__ == '__main__':
    # 计算学生001的平均分并输出
    print(avg_score('001'))
    # 获取最高分及其对应的学生姓名并输出
    print(highest_score())
