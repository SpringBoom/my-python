'''
== 用来判断是否相等
要判断两个值是否不等，可结合使用惊叹号和等号(!=)，其中的惊叹号表示不，其他很多编程语言中也是如此。
其它比较运算符：
    >、<、>=、<=
    in
多个条件，逻辑运算符：and、 or、 not
'''

# ---------------- if 语句 ----------------
for n in range(0,5):
    if n % 2 == 0:
        print(f"{n}: orange")
    else:
        print("no")

n = 2 
if n in range(0,3):
    print(f'{n} is in')

if n not in range(0,1):
    print(f'{n} not in')


age = 12
if age <4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


# ---------------- if 处理列表 ----------------
r = []
if r:
    print(f'{r} 不为空')
else:
    print(f'{r} 列表为空')

p = None
if p:
    print(f'{p} ok')
else:
    print(f'{p} not ok')