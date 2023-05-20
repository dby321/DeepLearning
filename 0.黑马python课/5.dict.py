my_dict = {"key1": 'value1'}
print(my_dict, type(my_dict))
print(my_dict["key1"])
my_dict["key2"] = "value2"  # 新增
my_dict["key1"] = "value3"  # 更新
value3 = my_dict.pop("key1")  # 弹出
print(value3)
# my_dict.clear() # 清空
print(my_dict)
keys = my_dict.keys()
print(keys)
for key in keys:
    print(key, my_dict[key])
for key in my_dict:
    print(key, my_dict[key])
print(len(my_dict))
