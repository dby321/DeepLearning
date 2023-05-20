# python支持多继承
# 同名的属性和方法以左边为准
class Father:
    father_name = "baba"

    def father_method(self):
        print(1111)


class MyClass(Father):
    def child_method(self):
        super().father_method()
        print(super().father_name)


myClass = MyClass()
myClass.child_method()
