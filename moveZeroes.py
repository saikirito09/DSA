class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in nums:
            if i != 0:
                temp.append(i)
        for i in range(len(temp),len(nums)):
            temp.append(0)
        for i in range(len(nums)):
            nums[i] = temp[i]
