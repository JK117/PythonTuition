from typing import List


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        temp = []
        result = []
        self.backtracking(candidates, target, 0, temp, result)
        return result

    def backtracking(self, candidates, target, start, temp_arr, res_arr):
        if target == 0:
            res_arr.append(temp_arr)
            return
        else:
            for i in range(start, len(candidates)):
                if target >= candidates[i]:
                    temp_arr.append(candidates[i])
                    self.backtracking(candidates, target - candidates[i], i+1, temp_arr[:], res_arr)
                    temp_arr.pop()
                else:
                    break


candidates = [2, 2, 4]
target = 6
test_case = CombinationSum()
result = test_case.combinationSum(candidates, target)
print(result)
