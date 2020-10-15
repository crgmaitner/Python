#operations.py
#Craig Maitner

nums = [0,1,1,5,4,5,9,7,8,9]

def count(nums, n):
    num = 0
    for n in nums:
        if n == n:
            num = num + 1
    return num

def isin(nums, n):
    for i in nums:
        if i == n:
            return True
    return False

def index(nums, n):
    for i in range(len(nums)):
        if n == nums[i]:
            return i
    return None

def reverse(nums):
    for i in range(len(nums)):
        nums2 = []
    i.reverse()
    return i

print(count(nums, 5))
print(isin(nums, 17))
print(index(nums, 3))
print(reverse(nums))