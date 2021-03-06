# Python Note 1: Basic

# 语言简介
# 动态解释型语言(字节码编译)
# 变量、参数、函数在声明时无需说明类型

# 赋值 & 输入 & 输出
name = input('Please input your name：')
print('Your name is ' + name)
a, b, c = (int(x) for x in input().split(' '))
print(a + b + c)

# 数学运算
# Python3 中除法运算(/)默认执行精确出除(exact division)
# 取整除使用 // 作为运算符
print(3/2)
# -> 1.5
print(3//2)
# -> 1
print(3.//2.)
# -> 1.0
# + * 运算符可对字符串类型数据自动重载
a = 'aaa'
b = 'bbb'
print(a + b)
# ->aaabbb
print(a*3 + b)
# ->aaaaaaaaabbb

# 字符串
# len() 获取字符串长度
a_len = len(a)
# str() 强制类型转换匹配字符串输出
c = 'The length of string a is: '
print(c + str(a_len))


def main():
    print('This is a main function')


if __name__ == '__main__':
    main()