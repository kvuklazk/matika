def rec(nums, i=0):
    if i < len(nums):
        if nums[i] < 9:
            nums[i] += 1
            print(nums, i)
            rec(nums, i+1)
        else:
            nums[i] = 1
            rec(nums, i-1)



rec([1, 2])
