from random import randint

count = 0
length = 10
nums = []
for array in range(10):
    nums.append(randint(0, 50))

print(nums)

for item in range(length-1):
    for sort in range(length-1-item):
        if nums[sort] > nums[sort+1]:
            # print("item =", item, "iterations: ", length-1-item, "first num nums[sort]: ", nums[sort], "second num nums[sort+1]: ", nums[sort+1], nums[sort] > nums[sort+1], nums)
            # print(f"Now equalize {nums[sort]} with {nums[sort+1]}")
            count += 1
            nums[sort], nums[sort+1] = nums[sort+1], nums[sort]
            foo = nums[sort]
            nums[sort] = nums[sort+1]
            nums[sort+1] = foo

print(nums)
print("Steps:", count)
