class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            nums = self.mark(nums)
            i = 0
            while(i < len(nums)-1):
                if not nums[i] == None:
                    i += 1
                else:
                    j = i + 1
                    while nums[j] == None:
                        if j < len(nums)-1:
                            j += 1
                        else:
                            print(nums)
                            return self.count(nums)
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        print(nums)
        return self.count(nums)

    def mark(self,nums):
        for i in range(len(nums)-1):
            j = i + 1
            while nums[i] == nums[j]:
                nums[j] = None
                if j + 1 < len(nums):
                    j += 1
                else:
                    break
        return nums

    def count(self, nums):
        end = 0
        for num in nums:
            if num != None:
                end += 1
        return end

if __name__ == "__main__":
    nums = [1,2]
    s= Solution()
    print(s.removeDuplicates(nums))