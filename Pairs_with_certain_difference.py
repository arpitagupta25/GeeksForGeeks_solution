class Solution:
    def maxSumPair(self, arr, k):
        arr.sort()
        total_sum = 0
        i = len(arr) - 1
        while i > 0:
            if arr[i] - arr[i - 1] < k:
                total_sum += arr[i] + arr[i - 1]
                i -= 2
            else:
                i -= 1
        return total_sum
