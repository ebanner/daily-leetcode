class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_g = list(sorted(g))
        sorted_s = list(sorted(s))

        n = len(g)
        m = len(s)

        i = 0
        j = 0
        num_cookies = 0
        while j < m:
            if i == n:
                break # satisfied all the children

            if sorted_s[j] < sorted_g[i]:
                j += 1
                continue # this cookie will satisfy no child → throw it out

            num_cookies += 1 # hand out cookie
            i += 1 # move onto the next child
            j += 1 # move onto the next cookie
        return num_cookies
