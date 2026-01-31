class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        target_val = ord(target)
        
        while left <= right:
            mid = (left + right) // 2
            
            if ord(letters[mid]) <= target_val:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left] if left < len(letters) else letters[0]
