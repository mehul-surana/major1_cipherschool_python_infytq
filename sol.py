def twoSum(nums: List[int], target: int):
  d={}
  for i,v in enumerate(nums):
     remain=target-nums[i]
     if remain in d:
      return [i,d[remain]]
     else:
         d[v]=i
