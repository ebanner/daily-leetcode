def get_counts(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts


def get_row(counts):
    """Also modify counts"""
    row = []
    for key, value in counts.items():
        row.append(key)
        counts[key] -= 1
    return row, counts


def purge(counts):
    return {key: value for key, value in counts.items() if value > 0}


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = get_counts(nums)
        array = []
        while counts:
            row, counts = get_row(counts)
            array.append(row)
            counts = purge(counts)
        return array
        
