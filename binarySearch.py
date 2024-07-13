import random

def binarySearch(nums, target, left, right):
        """
        Search for the index of target
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        while(left <= right):
            middle = (left + right)//2

            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                return binarySearch(nums, target, left, middle - 1)
            else:
                return binarySearch(nums, target, middle + 1, right)
        
        return -1

def run_binary_search():
    nums = [random.randint(0, 100) for _ in range(10)]
    nums.sort()
    target = random.randint(0, 100)
    print(nums)
    print(target)
    print(binarySearch(nums, target, 0, len(nums) - 1))

run_binary_search()