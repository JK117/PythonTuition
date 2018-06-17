# Python Note 5: Sort & Tuple


def test_sort(input_list):
    # 简单排序
    # 在字典序(lexicographical order)中比较第一个不同字符的编码值
    # sort() 不带返回值
    # x = list_nums.sort()
    # -> x: None
    print('Original list: ')
    print(input_list)
    input_list.sort()
    print('List after sort() operation: ')
    print(input_list)


def test_sorted(input_list):
    # 基本排序
    # sorted() 带返回值
    # sorted(list) 后不改变初始list
    print('Original list: ')
    print(input_list)
    print('Sorted(list): ')
    print(sorted(input_list))
    print('List after last operation: ')
    print(input_list)
    print('Sorted(list, reverse=True): ')
    print(sorted(input_list, reverse=True))
    print('List after last operation: ')
    print(input_list)


def mid_value(item):
    # 中间值函数
    if item == 'china':
        return 0
    else:
        return len(item)


def test_customized_sort(input_list):
    # 利用中间值函数进行自定义排序
    print('The original list: ')
    print(input_list)
    print('The list sorted by len: ')
    print(sorted(input_list, key=len))
    print('The list sorted by mid_value(china first)')
    print(sorted(input_list, key=mid_value))


def test_cross_sort(str_input):
    list_num = []
    list_a = []
    list_b = []
    list_result = []

    # str_input = input()
    print(str_input)
    list_input = str_input.split(' ')

    for x in list_input:
        list_num.append(int(x))

    len_num = len(list_num)
    i = 1
    while i <= len_num:
        if (i % 3 != 0) and (i % 2 == 0):
            list_a.append(list_num[i - 1])
        elif i % 3 == 0:
            list_b.append(list_num[i - 1])
        i += 1

    print(list_a)
    print(list_b)
    list_asc = sorted(list_a)
    list_des = sorted(list_b, reverse=True)
    print(list_asc)
    print(list_des)

    i = 1
    m = 0
    n = 0
    while i <= len_num:
        if (i % 3 != 0) and (i % 2 == 0):
            list_result.append(str(list_asc[m]))
            m += 1
        elif i % 3 == 0:
            list_result.append(str(list_des[n]))
            n += 1
        else:
            list_result.append(str(list_num[i - 1]))
        i += 1

    print(list_result)
    str_result = ' '.join(list_result)
    print(str_result)


def main():
    list_nums = [1, 4, 2, 3, 8, 3, 0]
    list_country = ['jp', 'china', 'usa', 'thai']
    str_input = '13 14 3 10 11 6 7 8 9 4 5 12 1 2 15'
    # test_sort(list_nums)
    # test_sorted(list_nums)
    # test_customized_sort(list_country)
    test_cross_sort(str_input)


if __name__ == '__main__':
    main()