
print("Hello Python!")

msg = "Hello Python world!"
print(msg)

msg = "Crash Course"
print(msg)

# 变量指向特定的值
tips='''
* 变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字打头。
* 变量名不能包含空格，但能使用下划线来分隔其中的单词。
'''
print(tips)


# ---------------- 字符串 ----------------
# 字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号。
print('\n# ---------------- 字符串 ----------------')
s1 = 'this is a string'
s2 = "This is also a string."
s3 = 'with tow seg, "I love python"'
print(s3)

## 字符串方法
name = 'ada lovelace'
print(name.title()) # Ada Lovelace
print(name.lower())
print(name.upper())

lrp = ' python '
print(lrp.rstrip()) # ' python'
print(lrp.lstrip()) # 'python '
print(lrp.strip())  # 'python'


## 字符串中使用变量
'''
f字符串是Python 3.6引入的。
这种字符串名为f字符串。f是format（设置格式）的简写，因为Python通过把花括号内的变量替换为其值来设置字符串的格式。
'''
print(f's1:{s1}; s2:{s2} s3:{s3}')
print(f"name to title: {name.title()}")



# ---------------- 数字 ----------------
''' 四则运算：+ - * / 
 ** 表示乘方
'''
## 浮点数
'''
Python将所有带小数点的数称为浮点数。大多数编程语言使用了这个术语，它指出了这样一个事实：小数点可出现在数的任何位置。
每种编程语言都必须细心设计，以妥善地处理浮点数，确保不管小数点出现在什么位置，数的行为都是正常的。

将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除。
无论是哪种运算，只要有操作数是浮点数，Python默认得到的总是浮点数，即便结果原本为整数也是如此。
'''
print(0.1 + 0.2)
print(2/1)  # 2.0
print(1*2.0)    # 2.0
print(2.0/2)    # 1.0

print(14_000_000)

## 常量
'''
程序员会使用全大写来指出应将某个变量视为常量
'''