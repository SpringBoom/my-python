'''
列表由一系列按特定顺序排列的元素组成。
在Python中，用方括号([​])表示列表，并用逗号分隔其中的元素。
可以使用 -1 来访问最后一个元素，但是如果列表为空，则会抛出 'IndexError:list index out of range'
'''

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])

# ---------------- 修改元素 ----------------
bicycles[0] = 'feige'
print(bicycles[0])

## 新增

bicycles.append('foever')
print(bicycles)

bicycles.insert(0,'newone')
print(bicycles)

## 删除

del bicycles[0]
print(bicycles)

popLast = bicycles.pop()
print(popLast)
print(bicycles)

pop1 = bicycles.pop(1)
print(pop1)
print(bicycles)

### 根据元素值删除
rd = 'feige'
bicycles.append(rd)
print(bicycles)
rd = bicycles.remove(rd)
print(bicycles)


# ---------------- 组织列表 ----------------
'''
使用方法sort()对列表永久排序
使用函数sorted()对列表临时排序
reverse()将列表倒序
len()返回列表长度
'''
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(sorted(cars))
print(cars)

cars.reverse()
print(cars)

print(len(cars))