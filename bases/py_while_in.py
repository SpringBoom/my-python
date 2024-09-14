
# ---------------- while ----------------
'''
语法： 
    while(conditions):
        do_somthings
        ...
break 用于跳出循环
continue 用于跳过本次循环

for循环是一种遍历列表的有效方式，但不应在for循环中修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。

'''

# 使用 while 处理列表和字典
s1 = ['a', 'b', 'c']
t2 = []

while s1:
    s = s1.pop()
    print(f"move {s}*2 to t")
    t2.append(s)
    t2.append(s)

print(s1)
print(t2)

# 删除指定元素
'''
remove() 只会删除第一个匹配的元素，所以需要使用 while 将列表中所有匹配的元素删除
'''
to_del = 'a'
while to_del in t2:
    d = t2.remove(to_del)
    print(d)
print(t2)