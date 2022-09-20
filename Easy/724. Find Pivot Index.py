"""Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1."""


def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        totalNums = sum(nums)
        
        for i in range(len(nums)):
            if(leftSum == totalNums - leftSum - nums[i]):
                return i
            else:
                leftSum = leftSum + nums[i]
        return -1
            
            
          
nums = [1,7,3,6,5,6]
print(pivotIndex(nums))

