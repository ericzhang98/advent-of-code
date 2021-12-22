import collections
with open('input7.txt') as f:
    nums = list(map(int,f.readline().strip().split(',')))
nums.sort()
median = nums[len(nums)//2]
print(sum(abs(median-v) for v in nums))
