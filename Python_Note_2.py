# Python Note 2: Programming
import sys


def max_pow(a, b):
    # 函数需要在使用前被定义
    # 函数定义形式如下
    if a > b:
        pow_ab = a ** b
        return pow_ab
    pow_ba = b ** a
    return pow_ba


# Python 规范中应使用下划线命名法(underscore naming)
# 而非类似于Java的驼峰命名法(camel-case naming)


# help() & dir(): import sys required
help(len)
print(dir(sys))
# help() 返回函数定义
# dir() 返回一个模组中所有被定义的函数方法的列表
help(sys.exit)
help('abc'.split)
print(dir(list))

