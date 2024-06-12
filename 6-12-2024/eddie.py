def get_cut_points(nums):
    num_zeros = 0
    num_ones = 0
    for num in nums:
        if num == 0:
            num_zeros += 1
        elif num == 1:
            num_ones += 1
    
    one_idx = num_zeros
    two_idx = num_zeros + num_ones
    
    return one_idx, two_idx


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one_idx, two_idx = get_cut_points(nums)
        nums[:one_idx] = [0]*one_idx
        nums[one_idx:two_idx] = [1]*(two_idx-one_idx)
        nums[two_idx:] = [2]*(len(nums)-two_idx)

