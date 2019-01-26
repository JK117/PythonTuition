# 18. 4Sum
class Solution4Sum:
    def four_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        num_len = len(nums)
        buff_dict = {}
        ans = set()
        nums.sort()

        # border conditions
        if len(nums) < 4 or 4 * nums[0] > target or 4 * nums[num_len - 1] < target:
            return []

        # sum of every 2-element pair
        for i in range(num_len):
            for j in range(i + 1, num_len):
                _sum = nums[i] + nums[j]
                if _sum not in buff_dict:
                    buff_dict[_sum] = [[i, j]]
                else:
                    buff_dict[_sum].append([i, j])

        # match the sum of other 2-element pair, and check they are not the same elements as the first 2 elements
        for i in range(num_len):
            for j in range(i + 1, num_len):
                _cha = target - (nums[i] + nums[j])
                if _cha in buff_dict:
                    for k in buff_dict[_cha]:
                        if k[0] > j:
                            ans.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return list(ans)


if __name__ == '__main__':
    nums_list = [1, 0, -1, 0, -2, 2]
    target_num = 0
    test_case = Solution4Sum()
    print(test_case.four_sum(nums_list, target_num))
