'''
'''


# ---------------- 创建和使用类 ----------------
'''
类中的函数称为方法。
__init__()是一个特殊方法，每当你根据类创建新实例时，Python都会自动运行它。
每个与实例相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
'''
class Student:
    def __init__(self, name, age):
        print(f"Student init {name}, {age}")
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I'm {self.name}, {self.age} years old.")

    def set_name(self, name):
        self.name = name


stu1 = Student('Wood', 11)
stu1.info()


# ---------------- 使用类和实例 ----------------
'''
修改属性值:
    直接修改属性的值
    通过方法修改
'''
# 
stu1.age = 12
stu1.info()

stu1.set_name('Wood')


# ---------------- 使用类和实例 ----------------
"""
如果要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，将自动获得另一个类的所有属性和方法。
子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。
在既有类的基础上编写新类时，通常要调用父类的方法__init__()。这将初始化在父类__init__()方法中定义的所有属性，从而让子类包含这些属性。

继承语法：
    class 子类(父类)
子类的 init 函数中：
    super().__init()

创建子类时，父类必须包含在当前文件中，且位于子类前面。
"""
class MStudent(Student):
    def __init__(self, name, age, grade):
        print("MStudent init")
        super().__init__(name, age)
        self.grade = grade

mst = MStudent("A", 12, 1)
mst.info()

"""
可在子类中定义一个与要重写的父类方法同名的方法。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。
"""