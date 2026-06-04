from collections import defaultdict
import bisect

class Solution:
    def freqInRange(self, arr, queries):

        freq = defaultdict(list)

        for i, num in enumerate(arr):
            freq[num].append(i)

        result = []

        for l, r, x in queries:

            # If x not present
            if x not in freq:
                result.append(0)
                continue

            positions = freq[x]

            left = bisect.bisect_left(positions, l)
            right = bisect.bisect_right(positions, r)

            result.append(right - left)

        return result
