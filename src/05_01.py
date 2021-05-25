nums = [1, 2, 12, 67]
i = 0
sum = 0
while i < len(nums):
    if nums[i] > 10:
        sum += nums[i]
    i += 1
print(sum)

sum = 0
while nums:
    i = nums.pop()
    if i > 10:
        sum += i

print(sum)