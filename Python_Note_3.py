# Python Note 3: String

# 转义字符
print('转义字符')
# 字符串内容包含引号时需要使用转义字符(\)
str_a = 'I don\'t know.'
# 双引号中包含单引号时不用添加转义字符(\)
str_b = "I don't know."
print('str_a: ' + str_a)
print('str_b: ' + str_b)
print('\n')

# 使用\分行
print('\\分行')
str_c = 'This is line part 1;\
This is line part 2;\
This is line part 3.'
print('str_c: ' + str_c)
print('\n')

# Python 字符串一旦创建即不可改变
# 所有字符串运算实际上在不断创建新字符串
# 如以下代码中str_a的内存对象已发生改变
str_a = str_a + str_b

# Upper case & Lower case
print('Uppercase & lowercase')
# r(raw)使字符串内转义字符失效
str_m = 'i am\n tom'
str_n = r'I am\n Tom'
print('str_m: ' + str_m)
print('str_n: ' + str_n)
print('str_m.upper():' + str_m.upper())
print('str_n.lower(): ' + str_n.lower())
print('\n')

# 字符串检测
print('字符串检测')
str_x = 'HelloabcdWord'
str_y = 'abcd'
print('str_x.isalpha(): ' + str(str_x.isalpha()))
print('str_x.isdigit(): ' + str(str_x.isdigit()))
print('str_x.startswith(\'Hello\'): ' + str(str_x.startswith('Hello')))
print('str_x.endswith(\'World\'): ' + str(str_x.endswith('World')))
print('\n')

# 字符串索引
print('字符串索引')
# 切取操作(Slice)前闭后开
print('str_x[1:4]: ' + str_x[1:4])
print('str_x[3:]: ' + str_x[3:])
print('str_x[:-2]:' + str_x[:-2])
print('\n')

# 查找与替换
print('查找与替换')
weather = 'rainy'
bag = 'empty'
print('bag: ' + bag)
if weather.find('rainy') != -1:
    bag = bag.replace('empty', 'umbrella')
print('bag: ' + bag)
print('\n')

# 字符串格式化
print('字符串格式化')
name = 'Tom'
age = 24
height = 178
print(name + 'is a ' + str(age) + 'years old young man with ' + str(height) + ' cm height.')
print('{0} is a {1} years old young man with {2}cm height.'.format(name, age, height))
print('%s is a %d years old young man with %gcm height.' % (name, age, height))
print('\n')

# 批量替换字符串
print('批量替换字符串')
str_z = 'We use python.'
print(str_z)
if str_z.find(' ') != -1:
    str_z = str_z.replace(' ', ' fucking ')
print(str_z)