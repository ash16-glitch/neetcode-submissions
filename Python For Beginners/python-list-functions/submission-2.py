from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    n = 0
    for i in nums:
        n+=i
    return(n)

        
def get_min(nums: List[int]) -> int:
    c = nums[0]
    for i in nums:
        if i<c:
            c=i
    return c

def get_max(nums: List[int]) -> int:
    c = nums[0]
    for i in nums:
        if c<i:
            c=i
    return c

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
