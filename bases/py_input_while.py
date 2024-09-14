'''
使用函数input()
使用 while 循环
'''


# ---------------- input() ----------------
'''
函数input()让程序暂停运行，等待用户输入一些文本。
'''
prompt = "We use input() in python to receipt what you are input here:"
inmsg = input(prompt)
print(f'You input:\n{inmsg}')


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

cn = 1
while cn <= 5:
    print(cn)
    cn += 1


while inmsg != 'quit':
    inmsg = input(prompt)
    if inmsg == 'quit':
        print('Bye')
        break
    print(inmsg)   

# 使用 while 处理列表和字典
s1 = ['a', 'b', 'c']
t2 = []

while s1:
    s = s1.pop()
    print(f"move {s} to t")
    t2.append(s)

print(s1)
print(t2)