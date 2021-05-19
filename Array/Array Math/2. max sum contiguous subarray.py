    def maxSubArray(self, A):
        sum_subarray = 0
        max_sum = A[0]
        for i in range(len(A)):
            sum_subarray += A[i]
            max_sum = max(sum_subarray, max_sum)
            if sum_subarray < 0:
                sum_subarray = 0
        return max_sum
        