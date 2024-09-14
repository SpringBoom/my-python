"""
def 关键字定义函数

"""

# ---------------- 定义函数 ----------------
from to_import import the_imp_hello


def say_hello():
    print('hello')

say_hello()

def hello(name):
    print(f'hello {name}')

hello('gaga')

"""
使用关键字实参
"""
def name_age(name, age):
    print(f'{name} is {age} years old')

name_age('LiMing', 15)
name_age(15, 'LiMing')
name_age(age = 15, name = 'LiMing')


"""
定义形参的默认值
指定默认值的形参前面不可以有没有默认值的形参
"""
def name_age(age, name='Uname'):
    print(f'{name} is {age} years old')

name_age(18)


"""
返回值
"""
def to_full_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

f = to_full_name('li', 'ming')
print(f)


"""
传递列表
"""
def letter_count(letters):
    count = 0
    for l in letters:
        count = count + len(l)
    return count

letters = ['a', 'b', 'c', 'd00']
lc = letter_count(letters)
print(lc)

"""
将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的
"""
def letter_to_title(before_letters, after_letters):
    while before_letters:
        l = before_letters.pop()
        after_letters.append(l.title())

bl = ['abc', 'efg']
tl = []
letter_to_title(bl, tl)
print(bl)
print(tl)

# 传递列表的副本
t = []
letter_to_title(tl[:], t)
print(tl)
print(t)

"""
使用 * 定义变长参数
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
"""
def too_many_args(*aaas):
    print(aaas)

too_many_args()
too_many_args(1,2,3)
too_many_args(1,'aaa',3)

"""
使用任意数量的关键字实参
有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键值对——调用语句提供了多少就接受多少。

形参 ** 两个星号让Python创建一个名为形参的空字典，并将收到的所有名称值对都放到这个字典中。
"""
def build_p(first, last, **info):
    info['first'] = first
    info['last'] = last
    return info

ir = build_p('a', 'b', c='c', d='d')
print(ir)


"""
将函数存储在模块中
将函数存储在称为模块的独立文件中，再将模块导入到主程序中。
要使用其它模块中的函数，需要先将其导入：
    导入整个模块
        improt module_name
    导入指定函数
        from module_name import function_name [,function_name1,...]
        from mudule_name import *
            然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法。
            这是因为如果模块中有函数的名称与当前项目中使用的名称相同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。

如果要导入函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名：函数的另一个名称，类似于外号。要给函数取这种特殊外号，需要在导入它时指定。
    from module_name import function_name  as itn
另外，导入的 module 也可以指定别名
"""
the_imp_hello()