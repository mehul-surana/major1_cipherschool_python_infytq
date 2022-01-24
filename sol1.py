##brute force
nums=list(map(int,input().split()))
target=int(input())
def tarsum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j]==target:
        return i,j
print(tarsum(nums,target))
      


#optimize

def tarsum(nums,target):
  d={}
  for i,v in enumerate(nums):
     remain=target-nums[i]
     if remain in d:
      return [i,d[remain]]
     else:
         d[v]=i
print(tarsum(nums,target))
