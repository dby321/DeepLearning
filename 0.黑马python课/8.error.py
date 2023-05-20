# 异常
try:
    f = open("file/abc.txt", 'r', encoding="UTF-8")
except (FileNotFoundError, NameError) as e:
    print("捕获异常", e)
except Exception as e:
    print("顶级异常", e)
else:
    print('没有异常，我就执行')
finally:
    print("无论如何都执行")
# 异常具有传递性
