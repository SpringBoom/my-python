'''
1. for 遍历列表
2. 使用 range() 创建数值列表
'''

# ---------------- 遍历列表 ----------------
magicians = ['alice', 'david', 'carolina']
for magi in magicians:
    print(magi)

## for 循环的变量作用域不只是在 for 循环体中
print(magi)


# ---------------- 创建数值列表 ----------------
'''
range() 产生一个整数序列
list() 将 range 转换为 列表
'''
for v in range(3):
    print(v)

print()
for v in range(0, 3):
    print(v)

print()
print("range(1, 10, 2):")
for v in range(1, 10, 2):
    print(v)

print()
print(list(range(3)))


## 对数字列表进行简单的统计
print()

dglist = list(range(1,10))
print(dglist)
print(f'max:{max(dglist)}')
print(f'min:{min(dglist)}')
print(f'sum:{sum(dglist)}')

## 列表解析
sq = [ n**2 for n in range(1,3) ]
print(sq)


# ---------------- 列表中的一部分 ----------------
'''
# 切片
创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python在到达第二个索引之前的元素后停止。
# 复制列表
要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引([:])。
'''
l = list(range(0,5))
print(l)
print(l[0:3])
print(l[:3])
print(l[2:])

## 复制列表
print("\n复制列表")
copyl = l[:]
print(copyl)
print(l==copyl)


# ---------------- 元组 ----------------
'''
有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可使用索引来访问其元素，就像访问列表元素一样。
试图修改元组中元素的值，导致Python返回类型错误消息。由于试图修改元组的操作是被禁止的，因此Python指出不能给元组的元素赋值：
TypeError:'tuple'object does not support item assignment

相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，就可以使用元组。
'''
print("\n# ---------------- 元组 ----------------")

d = (2, 5)
print(d)
print(d[0])

