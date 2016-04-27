class Solution(object):
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     res = [[]]
    #     res.append(list(nums))
    #     for ls in range(1, len(nums)):
    #         self.get_subsets(res, nums, [], ls, 0)
    #     return res
    #
    # def get_subsets(self, res, nums, curr_set, ls, index):
    #     # recursive
    #     if ls == 0:
    #         res.append(list(curr_set))
    #     elif index < len(nums):
    #         curr_set.append(nums[index])
    #         self.get_subsets(res, nums, curr_set, ls - 1, index + 1)
    #         curr_set.pop()
    #         self.get_subsets(res, nums, curr_set, ls, index + 1)

    def subsets(self, nums):
        # https://leetcode.com/discuss/89343/c-8-lines-bit-operation
        # doesn't work when len(nums) > 32
        nums.sort()
        res = []
        for i in range(1 << len(nums)):
            res.append(self.get_subsets(nums, i))
        return res

    def get_subsets(self, nums, magic):
        res = []
        for i in range(len(nums)):
            if (1 << i) & magic != 0:
               res.append(nums[i])
        return res




if __name__ == "__main__":
    s = Solution()
    print s.subsets([1,2,3])