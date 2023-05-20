import time

# 读取
f = open('file/python.txt', 'r', encoding='UTF-8')
print(type(f))
# print(f.read(10))  # 从上次调用结尾处继续读取
# print(f.read())
# print(f.readlines())  # 读取所有行
# print(f.readline())  # 读取一行
for line in f:
    print(line)
f.close()  # 关闭文件流
with open('file/python.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line)
# 写入
# f = open('file/python.txt', 'w')
# f1 = open('file/python1.txt', 'w')
# f.write("hello world")  # 写入内存
# f1.write("hello world")
# f.flush()  # 刷盘
# f1.flush()
# f.close() # 调用close会自动调用flush

# 追加写入
f = open('file/python.txt', 'a', encoding='UTF-8') # 文件不存在会创建文件
f.write("\nhello world")
f.close()
