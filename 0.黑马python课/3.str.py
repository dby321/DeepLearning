my_str = "1121122hello world121221"
new_my_str = my_str.replace("hello", "Hello")
print(new_my_str)
my_list = my_str.split(" ")
print(my_list)
print(my_str.strip("12"))
print(my_str.count("1"))
print(len(my_str))
for i in my_str:
    print(i)
