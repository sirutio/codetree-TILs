n = int(input())
nums = list(map(int,input().split()))
temp = 1

def FindGCD(ans, newnum):
    GCD = 0
    if ans == newnum:
        return ans
    elif ans > newnum: # 10 5
        if ans%newnum == 0:
            return ans
        for i in range(2,ans):
            if ans%i == 0 and newnum%i == 0:
                GCD = i
                break 
        if GCD != 0:
            return (ans//i)*newnum
    else:
        if newnum%ans == 0:
            return newnum
        for i in range(2,newnum):
            if ans%i == 0 and newnum%i == 0:
                GCD = i
                break 
        if GCD != 0:
            return (newnum//i)*ans
    return ans*newnum


def FindLCM(N, Temp_LCM):
    # Break 
    if N == 0:
        return Temp_LCM 
    # 1
    idx = len(nums)-N # 6 -> 0,1,2,3,4,5 
    LCMBetween2 = FindGCD(Temp_LCM, nums[idx])
    return FindLCM(N-1, LCMBetween2)
    
print(FindLCM(n,temp))