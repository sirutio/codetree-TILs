def max_val(idx, nums):
    if max(nums) != nums[idx]:
        return max_val(idx-1,nums)
    else:
        return nums[idx] 

n = int(input())
nums = list(map(int,input().split()))
print(max_val(n-1,nums))