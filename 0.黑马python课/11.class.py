class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'MyClass{self.name},{self.age}'

    def __lt__(self, other):
        """小于
        :param other:
        :return:
        """
        return self.age < other.age

    def __le__(self, other):
        """小于等于
        :param other:
        :return:
        """
        return self.age <= other.age

    def __eq__(self, other):
        """相等
        :param other:
        :return:
        """
        return self.name == other.name


myClass = MyClass("周杰伦", '31')
print(myClass)  # 默认输出地址值，重写__str__后，相当于toString()
print(str(myClass))
myClass2 = MyClass("林俊杰", '32')
print(myClass < myClass2)
print(myClass > myClass2)
print(myClass <= myClass2)
print(myClass == myClass2)
