D = 10
N = 300


def do_dp(job_difficulties, D):
    n = len(job_difficulties)

    #
    # Minimum job schedule difficulty for d buckets on suffix jobDifficulty[i:]
    #
    DP = [[-1]*n for i in range(D+1)]

    #
    # Maximum value in the d'th bucket for the minimum job schedule difficulty
    #
    dp = [[-1]*n for i in range(D+1)]

    for i in range(n-1, -1, -1):
        for d in range(1, D+1):
            if d == 1 and i == n-1:
                dp[d][i] = job_difficulties[i]
                DP[d][i] = dp[d][i]
                continue
            
            suffix_len = n-i
            if d > suffix_len:
                dp[d][i] = -1
                DP[d][i] = dp[d][i]
                continue

            if d == 1:
                dp[d][i] = max(job_difficulties[i], dp[1][i+1])
                DP[d][i] = dp[d][i]
                continue

            own_bucket = job_difficulties[i] + DP[d-1][i+1]
            add_to_bucket = (DP[d][i+1] - dp[d][i+1]) + max(job_difficulties[i], dp[d][i+1]) 

            if add_to_bucket >= own_bucket:
                #
                # Prefer add_to_bucket in a tie because it maximizes flexibilty 🤷
                #
                dp[d][i] = max(job_difficulties[i], dp[d][i+1])
                DP[d][i] = own_bucket
            else:
                dp[d][i] = job_difficulties[i]
                DP[d][i] = add_to_bucket
    return DP


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        DP = do_dp(jobDifficulty, d)
        for row in DP:
            print(row)
        min_difficulty = DP[d][0]
        return min_difficulty

