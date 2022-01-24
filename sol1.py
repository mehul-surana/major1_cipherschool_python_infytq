##brute force
def twoSum(self, nums: List[int], target: int) -> List[int]:
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j]==target:
        return i,j
    
      


#optimize

def twoSum(nums: List[int], target: int):
  d={}
  for i,v in enumerate(nums):
     remain=target-nums[i]
     if remain in d:
      return [i,d[remain]]
     else:
         d[v]=i
