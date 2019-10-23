"""


    步骤：
        （一）
        数据模型类：StudentModel
            数据：编号 id,姓名 name,年龄 age,成绩 score
        逻辑控制类：StudentManagerController
            数据：学生列表 __stu_list
            行为：获取列只读属性 stu_list,
                 添加学生 add_student(stu_info)
                      给stu_info创建学生编号
                      存储学生
        测试：添加学生功能、获取所有学生功能.
        （二）在逻辑控制类中，完成删除学生功能，返回是否删除成功.
              remove_student(stu_id)

"""


class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0.0):
        self.id = 0  # 真实数据在添加学生时确定
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    """
        学生管理控制器：主要负责处理程序的主要逻辑（算法）。
    """
    # 学生的初始编号
    __init_id = 1000

    @classmethod
    def __generate_id(cls):
        cls.__init_id += 1
        return cls.__init_id

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加学生，由界面获取学生信息方法调用。
        :param stu_info:需要添加的学生对象(信息)
        """
        stu_info.id = StudentManagerController.__generate_id()
        self.__stu_list.append(stu_info)

    def remove_student(self, stu_id):
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True  # 删除成功
        return False  # 删除失败


# 测试代码
manager = StudentManagerController()
s01 = StudentModel("赵敏", 26, 100)
manager.add_student(s01)
manager.add_student(StudentModel("灭绝", 56, 85))

manager.remove_student(1002)
for item in manager.stu_list:
    print(item.name, item.score)
