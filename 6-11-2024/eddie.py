class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = {}
        extras = []
        for a in arr1:
            if a in arr2:
                if a not in counts:
                    counts[a] = 0
                counts[a] += 1
            else:
                extras.append(a)
        
        result = []
        for a in arr2:
            if a in counts:
                count = counts[a]
                result.extend([a]*count)
        
        sorted_extras = sorted(extras)
        result.extend(sorted_extras)
        
        return result

