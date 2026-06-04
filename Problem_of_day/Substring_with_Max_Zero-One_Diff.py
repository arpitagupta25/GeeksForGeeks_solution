class Solution:
	def maxSubstring(self, s):
		if s and all(ch=="1" for ch in s):
		    return -1
		else:
	        curr_sum = 0
            max_sum = -1
    
            for ch in s:
    
                if ch == '0':
                    val = 1
                else:
                    val = -1
    
                curr_sum = max(val, curr_sum + val)
    
                max_sum = max(max_sum, curr_sum)
    
            return max_sum
