import json

my_dict = [{"name": "中文", "age": "18"}, {"name": '英文'}]
json_str = json.dumps(my_dict, ensure_ascii=False)  # 字典/列表转json
print(json_str)
my_dict2 = json.loads(json_str)  # json转字典/列表
print(my_dict2)
