nums = [1, 0, -1, 0, -2, 2]
target = 0


def four_sum(num_list, target_num):
    """
    :type num_list: List[int]
    :type target_num: int
    :rtype: List[List[int]]
    """
    _len,_dict,ans = len(num_list), {}, set()
    num_list.sort()
    if len(num_list) < 4 or 4*num_list[0] > target_num or 4*num_list[_len - 1] < target_num:
        return []
    for i in range(_len):
        for j in range(i + 1,_len):
            _sum = num_list[i] + num_list[j]
            if _sum not in _dict:
                _dict[_sum] = [(i,j)]
            else:
                _dict[_sum].append((i,j))
    for i in range(_len):
        for j in range(i + 1,_len):
            _cha = target_num - (num_list[i] + num_list[j])
            if _cha in _dict:
                for k in _dict[_cha]:
                    if k[0] > j:
                        ans.add((num_list[i], num_list[j], num_list[k[0]], num_list[k[1]]))
    return list(ans)


four_sum(nums, target)
