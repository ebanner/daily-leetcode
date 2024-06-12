def advance():
    while nums[one_idx] != 1 and legal(one_idx+1, nums, cut_points, bucket=1):
        one_idx += 1


def sortColors(nums: List[int]) -> None:
    cut_points = get_cut_points(nums)
    one_idx, two_idx = get_pointers(cut_points)
    
    i = 0
    while True:
        bucket = get_bucket(i, cut_points)
        if nums[i] == bucket:
            i += 1
            continue

        if bucket == 0:
            if nums[i] == 1:
                nums[one_idx], nums[i] = 1, nums[one_idx]
                one_idx = advance(one_idx, cut_points, nums, pointer='one_idx')
            elif nums[i] == 2:
                nums[i], nums[two_idx] = nums[two_idx], 2
                two_idx = advance(two_idx, cut_points, nums, pointer='two_idx')
        elif bucket == 1:
            if nums[i] == 2:
                nums[i], nums[two_idx] = nums[two_idx], 1
                two_idx = advance(two_idx, cut_points, nums, pointer='two_idx')
        
        if nums[i] == bucket:
            i += 1

