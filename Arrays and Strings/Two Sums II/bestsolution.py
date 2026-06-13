class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        dict ={}
        for i , n in enumerate(numbers):
            diff = target - n 
            if diff in dict:
                return [dict[diff]+1, i +1]
            dict[n] = i      
        
