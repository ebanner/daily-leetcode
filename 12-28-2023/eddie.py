def filter_min(S):
    min_len = min(len(s) for s in S)
    mins = [s for s in S if len(s) == min_len]
    return mins


def rle(s):
    rle_str = []
    i = 0
    while i < len(s):
        c = s[i]
        j = i

        while j < len(s) and s[j] == c:
            j += 1

        if j-i > 1:
            r = f'{c}{j-i}'
        else:
            r = c

        rle_str.append(r)
        i = j

    return ''.join(rle_str)


def expand(rle_str):
    i = 0
    s = []
    while i < len(rle_str):
        j = i+1
        k = j
        while k < len(rle_str) and rle_str[k].isdigit():
            k += 1
        if k-j >= 1:
            digits = rle_str[j:k]
            chunk = rle_str[i]*int(digits)
        else:
            chunk = rle_str[i]
        s.append(chunk)
        i = k
    return ''.join(s)


def getOptimalCompressionRLEs(s, i, k_):
    """

    Optimal compression RLEs of s starting at index i taking away k_ elements

    """
    n = len(s)
    if k_ == 0:
        return [rle(s[i:])]
    elif i == n-1:
        return [rle('')]

    try_remove_rles = getOptimalCompressionRLEs(s, i+1, k_-1)
    dont_remove_rles = getOptimalCompressionRLEs(s, i+1, k_)
    dont_remove_rles = [rle(s[i] + expand(rle_str)) for rle_str in dont_remove_rles]
    dont_remove_rles = filter_min(dont_remove_rles)

    try_remove_rles_min = min(len(rle_str) for rle_str in try_remove_rles)
    dont_remove_rles_min = min(len(rle_str) for rle_str in dont_remove_rles)

    if try_remove_rles_min < dont_remove_rles_min:
        return try_remove_rles
    elif dont_remove_rles_min < try_remove_rles_min:
        return dont_remove_rles
    else:
        return try_remove_rles + dont_remove_rles



class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        min_length = 100
        min_rle_strs = getOptimalCompressionRLEs(s, 0, k)
        print(min_rle_strs)
        min_rle_str = min_rle_strs[0]
        return len(min_rle_str)
