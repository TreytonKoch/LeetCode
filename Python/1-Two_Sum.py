class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ##Each EX below is taken (very minorly edited) from LeetCode's own solutions
        '''
        #EX1
        for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i,j]
        return[]
        '''

        '''
        #EX2
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
        '''

        #'''
        #EX3
        hashmap = {}
        for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashmap:
                    return [i, hashmap[complement]]
                else:
                    hashmap[nums[i]] = i
        return []
        #'''

##Lists
list1 = [2,7,11,15]
list2 = [3,2,4]
list3 = [3,3]

sol = Solution()

s1 = sol.twoSum(list1, 9)
s2 = sol.twoSum(list2, 6)
s3 = sol.twoSum(list3, 6)

print(s1)
print(s2)
print(s3)








"""
twoSum = Solution(list1, 9)
twoSum = Solution(list2, 6)
twoSum = Solution(list3, 6)

solution = Solution()

# Call the twoSum method with the appropriate arguments
result1 = solution.twoSum(list1, 9)  # Expected output: [0, 1]
result2 = solution.twoSum(list2, 6)  # Expected output: [1, 2]
result3 = solution.twoSum(list3, 6)  # Expected output: [0, 1]

# Print results
print(result1)  # [0, 1]
print(result2)  # [1, 2]
print(result3)  # [0, 1]
"""

'''
##########################
#My initial (bad) attempt
##########################
x = 0
y = 0
for i in nums:
value1 = i
x += 1
for j in nums:
  value2 = j
  y += 1
  if value1 + value2 == target:
      list1 = [x, y] 
      return list1
  else:
      return False


##Each example below is taken from LeetCodes solution section (Editorial tab on the problem)
##Example 1
class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
#########
for i in range(len(nums)):
  for j in range(i + 1, len(nums)):
      if nums[j] == target - nums[i]:
          return [i, j]
## Return an empty list if no solution is found
return []

##Example 2
class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:

######
hashmap = {}
for i in range(len(nums)):
  hashmap[nums[i]] = i
for i in range(len(nums)):
  complement = target - nums[i]
  if complement in hashmap and hashmap[complement] != i:
      return [i, hashmap[complement]]
## If no valid pair is found, return an empty list
return []

##Example 3
class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
hashmap = {}
for i in range(len(nums)):
  complement = target - nums[i]
  if complement in hashmap:
      return [i, hashmap[complement]]
  hashmap[nums[i]] = i
## Return an empty list if no solution is found
return []

'''
 
