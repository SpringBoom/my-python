"""
主要内容：
* 文件
* 异常
* json
"""


# ---------------- 从文件中读取数据 ----------------
"""
读取整个文件
"""
file_name = 'bases/data/pi_data.txt'
with open(file_name) as file_obj:
    contents = file_obj.read()
print(contents)


"""
逐行读取
"""
with open(file_name) as file_obj:
    for line in file_obj:
        # 函数调用print()也会加上一个换行符
        print(line)

# 使用列表
with open(file_name) as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())