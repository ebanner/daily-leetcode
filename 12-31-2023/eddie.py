def get_first(s):
    first = {}
    for i, c in enumerate(s):
        if c in first:
            continue
        else:
            first[c] = i
    return first


def get_last(s):
    last = {}
    n = len(s)
    for i in range(n-1, -1, -1):
        c = s[i]
        if c in last:
            continue
        else:
            last[c] = i
    return last


def subtract(last, first):
    import string
    distances = {}
    for c in string.ascii_lowercase:
        if not (c in last and c in first):
            continue
        else:
            distances[c] = last[c] - first[c] - 1
    return distances


def get_max_distance(distances):
    return max(distances.values())


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = get_first(s)
        last = get_last(s)
        distances = subtract(last, first)
        max_distance = get_max_distance(distances)
        return max_distance
