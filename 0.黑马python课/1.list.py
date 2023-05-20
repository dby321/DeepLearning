my_list = [1, 2, 3]
print(my_list)
my_list[0] = 2
my_list.insert(1, "best")# 指定位置新增
print(my_list)
my_list.append("end")# 尾部新增一个
print(my_list)
my_list.extend([3, 4, 5])# 尾部新增一批
print(my_list)
# del my_list[0]# 删除指定索引的元素
my_list.pop(2)# 弹出指定索引的元素
print(my_list)
my_list.remove("end")# 删除指定元素
print(my_list)
# my_list.clear()# 清空所有元素
print(my_list)
print(my_list.count(2))# 统计某个元素的数量
print(len(my_list))# 返回列表的数量
