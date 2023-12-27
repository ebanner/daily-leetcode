def get_argmax(A):
    max_a = max(A)
    maxes = [(i, a) for i, a in enumerate(A) if a == max_a]
    first = maxes[0]
    i_max, max_a = first
    return i_max


def pick_mins(neededTime, color_range):
    i, j = color_range
    needed_times = neededTime[i:j+1]

    k = get_argmax(needed_times)
    picked_times = [needed_time for l, needed_time in enumerate(needed_times) if l != k]

    return sum(picked_times)


def get_len(color_range):
    """

    (2, 2) should have a length of 1

    """
    start, end = color_range
    return (end-start) + 1


def safe_index(colors, k):
    if k >= len(colors):
        return None
    else:
        return colors[k]


def get_color_ranges(colors):
    i = 0
    color_ranges = []
    while i < len(colors):
        color = colors[i]
        j = i

        while safe_index(colors, j+1) == color:
            j += 1

        color_range = (i, j)
        color_ranges.append(color_range)

        i = j+1

    return color_ranges


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0
        for color_range in get_color_ranges(colors):
            if get_len(color_range) > 1:
                min_time += pick_mins(neededTime, color_range)
        return min_time
