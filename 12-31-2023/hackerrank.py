def parse_input():
    N = int(input())
    A = [int(num) for num in input().split()]
    T = int(input())
    S = [int(input()) for i in range(T)]
    return N, A, T, S


def get_reversed_cumsum(A):
    reversed_A = list(reversed(A))
    cumsum = 0
    cumsum_A = []
    for a in reversed_A:
        cumsum += a
        cumsum_A.append(cumsum)
    return cumsum_A


def get_min_subset(cumsum, s):
    # binary search
    
    n = len(cumsum)
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo+hi) // 2
        if cumsum[mid] == s:
            return mid+1 # size
        elif s < cumsum[mid]:
            hi = mid-1
        elif cumsum[mid] < s:
            lo = mid+1

    if lo == n:
        return -1 # ran off the end

    return lo+1 # size


if __name__ == '__main__':
    N, A, T, S = parse_input()
    cumsum = get_reversed_cumsum(A)
    for s in S:
        min_subset = get_min_subset(cumsum, s)
        print(min_subset)
