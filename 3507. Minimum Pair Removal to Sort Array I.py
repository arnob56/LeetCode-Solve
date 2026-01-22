class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
            return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))
        
        operations = 0
        
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            index = 0
            
            # Find leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    index = i
            
            # Replace the pair with their sum
            nums[index:index + 2] = [min_sum]
            operations += 1
        
        return operations
