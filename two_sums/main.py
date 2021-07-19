"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums: list, target: int) -> list:
        d = {}
        index = 0
        for i in nums:
            total = target - i
            if total in d:
                return [d.get(total), index]
            d.update({i: nums.index(i)})
            index += 1    
        return []        

def main():
    nums1 = [2,7,11,15]
    target1 = 10
    nums2 = [3,2,4]
    target2 = 6
    nums3 = [3,3]
    target3 = 6
    print(twoSum(nums1, target1))

if __name__ == "__main__":
    main()