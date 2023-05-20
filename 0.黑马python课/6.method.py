# 位置参数和关键字参数在混用时，位置参数要放在前面
# 默认参数必须写在最后面
# 不定长参数

def user_info(name, age, gender="男"):
    print(f'姓名是{name},年龄是{age},性别是{gender}')


user_info("董滨雨", "25")


def user_info(*args, **kwargs):
    print(args, kwargs)


user_info("name", 'age', key="value", key2="value2")


# 函数作为参数传递
def test_func(func):
    result = func(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)
# lambda表达式
test_func(lambda x, y: x + y)
