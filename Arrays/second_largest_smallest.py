def sec_largest(nums):
    largest = nums[0]
    sec_largest = float('-inf')
    
    if len(nums) < 2:
        return None
    
    for num in nums:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num > sec_largest and num != largest:
            sec_largest = num
            
    return sec_largest
    
    
print(sec_largest([1, 2, 3, 4, 5]))


def sec_smallest(nums):
    smallest = nums[0]
    sec_smallest = float('inf')
    
    for num in nums:
        if num < smallest:
            sec_smallest = smallest
            smallest = num
        elif num < sec_smallest and num != smallest:
            sec_smallest = num
            
    return sec_smallest
    
    
print(sec_smallest([1, 2, 3, 4, 5]))