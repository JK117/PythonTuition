# Python Note 4: Structure

# List 索引
print('List 索引')
list_a = [1, 2, 3]
list_b = [5, 6]
print('list_a: ' + str(list_a))
print('list_a[1]: ' + str(list_a[1]))
# 使用 len() 获得长度
print('len(list_a): ' + str(len(list_a)))
# list 尾部添加
list_a.append(4)
print('list_a after append: ' + str(list_a))
list_a.extend(list_b)
print('list_a after extend: ' + str(list_a))
print('\n')

# list 插入数据与元素定位
list_a.insert(0, 0)
print('list_a after insert: ' + str(list_a))
print('list_a.index(2): ' + str(list_a.index(2)))
print('\n')

# List 弹出与删除
print('list_a: ' + str(list_a))
# remove(x) 删除内容为x的元素
list_a.remove(6)
print('list_a after remove(6): ' + str(list_a))
# pop(y) 弹出索引为y的元素
list_a.pop(5)
print('list_a after pop(5): ' + str(list_a))
print('\n')

# string 切割与 list 合成
str_alpha = 'a,b,c'
print('str_alpha: ' + str_alpha)
# 用字符串切割函数 split() 进行切割
list_alpha = str_alpha.split(',')
print('list_alpha(splitted from str_alpha): ' + str(list_alpha))
# 用合成函数 join() 合成字符串
str_new_alpha = ' '.join(list_alpha)
print('list_alpha joined with space: ' + str_new_alpha)

# list 求和
total = 0
for num in list_a:
    total += num
print('The sum of list_a is: ' + str(total))
# 使用 sum() 函数
print('Calculate again with sum(): ' + str(sum(list_a)))
print('\n')

# range()的使用
# range(起始值_闭, 结束值_开, 步长)
print('range(10): ' + str(range(10)))
print('range(1, 10): ' + str(range(1, 10)))
print('range(1, 10, 2): ' + str(range(1, 10, 2)))
print('range(10, 1, -2): ' + str(range(10, 1, -2)))
print('\n')


def calc_fibonacci(count):
    first_num = 0
    second_num = 1
    i = 0
    while i < count:
        first_num, second_num = second_num, first_num + second_num
        i += 1
    return first_num


print(calc_fibonacci(9))
