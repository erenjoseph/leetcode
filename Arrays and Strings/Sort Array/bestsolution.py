class Solution(object):
    def sortArray(self, nums):

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Heap Sort
        # Complexity: O(N * log(N)), where N is the number of elements, in all cases (best, average, and worst)
        # def heapify(n, i):
        #     # Initialize largest as root 'i'.
        #     largest = i;
        #     left = 2 * i + 1
        #     right = 2 * i + 2
        #     # If left child is larger than root.
        #     if left < n and nums[left] > nums[largest]:
        #         largest = left
        #     # If right child is larger than largest so far.
        #     if right < n and nums[right] > nums[largest]:
        #         largest = right
        #     # If largest is not root swap root with largest element
        #     # Recursively heapify the affected sub-tree (i.e. move down).
        #     if largest != i:
        #         nums[i], nums[largest] =  nums[largest], nums[i]
        #         heapify(n, largest)

        # def heap_sort():
        #     n = len(nums)
        #     # Build heap; heapify (top-down) all elements except leaf nodes.
        #     for i in range(n // 2 - 1, -1, -1):
        #         heapify(n, i)
        #     # Traverse elements one by one, to move current root to end, and
        #     for i in range(n - 1, -1, -1):
        #         nums[0], nums[i] = nums[i], nums[0]
        #         # call max heapify on the reduced heap.
        #         heapify(i, 0)

        # heap_sort()
        # return nums

        def counting_sort():
            # Counting Sort (useful in situations where the elements in the array have a limited range)
            # Complexity: O(N + K), where N is the number of elements in the array, K is the size of buckets used (difference
            # between the smallest and the larget elements), in all cases (best, average, and worst)
            freqCount = {}
            smallest, largest = min(nums), max(nums)
            index = 0
            # Update the count of each element
            for num in nums:
                freqCount[num] = freqCount.get(num, 0) + 1
            # Place each element in the corrent position
            for val in range(smallest, largest + 1):
                if val in freqCount:
                    for i in range(freqCount[val]):
                        nums[index] = val
                        index += 1
                        
        counting_sort()
        return nums
