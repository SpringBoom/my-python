'''
字典可存储的信息量几乎不受限制，因此我们会演示如何遍历字典中的数据。
'''


# ---------------- 字典示例 ----------------
'''
{} 定义字典
[] 获取指定键值时，如果键不存在则抛出 KeyError 异常
    推荐使用 get()，提供一个默认值，避免抛出异常
        get 如果不指定第二个参数（默认值），则返回 None

del 通过键 删除 键值对，如果键不存在则抛出 KeyError 异常

'''
fruit_0 = {
    "name": "apple",
    "cal": 100 
}
print(fruit_0)
print(fruit_0["name"])
print(fruit_0["cal"])

fruit_0['color'] = 'red'
print(fruit_0)

fruit_0 = {}
print(fruit_0)
fruit_0['name'] = 'banana'
fruit_0["color"] = "yellow"
print(fruit_0)

fcal = fruit_0.get('cal', None)
print(fcal)


print("\n")
# ---------------- 遍历字典 ----------------
'''
遍历方式：可遍历字典的所有键值对，也可仅遍历键或值。
'''

print("for k,v in items:")
for k,v in fruit_0.items():
    print(f"{k}:{v}")

print("for k in fruit_0.keys():")
for k in fruit_0.keys():
    print(f"{k}")

print("for k in fruit_0:")
for k in fruit_0:
    print(f"{k}")

print("for v in fruit_0.values():")
for v in fruit_0.values():
    print(f"{v}")


print("\n")
# ---------------- 嵌套 ----------------
'''
有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
'''

fruit_list = []
for i in range(1,5):
    f = {'name': 'apple', 'weight': i}
    fruit_list.append(f)
for f in fruit_list:
    print(f)