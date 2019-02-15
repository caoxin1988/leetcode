import numpy as np

class Solution:
    def sortColors(self, nums):
        if not nums:
            return nums

        # self.quick_sort(nums, 0, len(nums)-1)
        self.quick_sort_3way(nums, 0, len(nums)-1)

    def quick_sort(self, nums, p, q):
        if q <= p:
            return
        
        pivot = nums[q]
        j = p

        for i in range(p, q+1):
            if nums[i] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        nums[j], nums[q] = nums[q], nums[j]

        self.quick_sort(nums, p, j-1)
        self.quick_sort(nums, j+1, q)

    def quick_sort_3way(self, nums, p, q):
        if q <= p:
            return

        lt, gt = p, q
        pivot = nums[p]

        i = p
        while i <= gt:
            if nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            elif nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
            else:
                i += 1

        self.quick_sort_3way(nums, p, lt-1)
        self.quick_sort_3way(nums, gt+1, q)

# nums = np.random.randint(0, 3, size=3).tolist()
nums = [0,2,1]
print(nums)

solution = Solution()
solution.sortColors(nums)
print(nums)


