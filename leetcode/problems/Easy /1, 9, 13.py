#Two sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  
        for i, num in enumerate(nums):
            complement = target - num  
            if complement in num_map:  
                return [num_map[complement], i]  
            num_map[num] = i  
        return []  
    
#Palindrome Number 
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  
            return False

        reversed_num = 0
        original = x

        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num
#Roman to Integer
class Solution3:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    
        total = 0
        prev_value = 0  
    
        for char in reversed(s):  
            value = roman_values[char]
            if value < prev_value:
                total -= value  
            else:
                total += value  
        
            prev_value = value  
    
        return total