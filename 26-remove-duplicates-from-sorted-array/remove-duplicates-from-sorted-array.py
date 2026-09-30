class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1  # the first element is always unique

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:  # new unique number found
                nums[k] = nums[i]
                k += 1

        return k