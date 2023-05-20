my_set = {"123", "123", "456"}
print(my_set)
print(type(my_set))
my_empty_set = set()
print(my_empty_set)
my_set.add("788")
print(my_set)
my_set.remove("788")
print(my_set)
print(my_set.pop())  # 随机取出一个元素
# my_set.clear()
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)  # 取出set1有，set2没有的元素，返回set
print(set3)
set1.difference_update(set2)  # 消除差集，set1变化了
print(f"set1={set1}")
print(f"set2={set2}")
set4 = set1.union(set2)  # 合并集合
print(f"set4={set4}")
print(f"len(set4)={len(set4)}")
for element in set1:
    print("element=" + str(element))
