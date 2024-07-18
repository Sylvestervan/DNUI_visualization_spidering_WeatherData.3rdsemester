#用列表推导式得到多层嵌套中的数是2的倍数的平方组成的列表并输出
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

new_list = [x**2 for i in a for x in i if x % 2 == 0]

print(new_list)

#TODO#

A_list = tuple('ABCDEFGH')

for i in range(len(A_list)):
    # 使用*操作符进行解包，将第一个元素赋给变量，其余的放在变量中
    head, *tail = A_list[i:]
    print(f"{head}：{tuple(tail)}")


# 有值 li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90],将所有大于66的值保存至字典的第一个key中，将小于66的值保存至
# 第二个key的值中
# {'k1':[77,88,99,90],'k2':[11,22,33,44,55]}

li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

list_1 = [i for i in li if i > 66]
list_2 = [i for i in li if i < 66]

result_dict = {'k1': list_1, 'k2': list_2}
print(result_dict)

#集合练习

# 定义经理和技术人员的集合
manager = {'刘备', '曹操', '孙权'}
technical = {'曹操', '孙权', '张飞', '关羽'}

# 1.既是经理也是技术员的有谁？
both_manager_and_technical = manager.intersection(technical)

# 2.是技术员但不是经理的人有谁？
technical_not_manager = technical.difference(manager)

# 3.是经理，但不是技术员的有谁？
manager_not_technical = manager.difference(technical)

# 4.身兼一职的人有谁？
one_position = manager.symmetric_difference(technical)

# 5.经理和技术员共有几人？
total_people = manager.union(technical)

# 打印结果
print("既是经理也是技术员的有：", both_manager_and_technical)
print("是技术员但不是经理的人有：", technical_not_manager)
print("是经理，但不是技术员的有：", manager_not_technical)
print("身兼一职的人有：", one_position)
print("经理和技术员共有几人：", len(total_people))


