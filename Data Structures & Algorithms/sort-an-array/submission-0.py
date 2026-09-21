class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
   

        def merge(array, left_start, middle, right_end):

            left_half = array[left_start:middle + 1]
            right_half = array[middle + 1:right_end + 1]

            left_index = 0
            right_index = 0
            array_index = left_start

            while left_index < len(left_half) and right_index < len(right_half):

                if left_half[left_index] <= right_half[right_index]:
                    array[array_index] = left_half[left_index]
                    left_index += 1

                else:
                    array[array_index] = right_half[right_index]
                    right_index += 1

                array_index += 1

            while left_index < len(left_half):
                array[array_index] = left_half[left_index]
                left_index += 1
                array_index += 1

            while right_index < len(right_half):
                array[array_index] = right_half[right_index]
                right_index += 1
                array_index += 1


        def merge_sort(array, left, right):

            if left >= right:
                return

            middle = (left + right) // 2

            merge_sort(array, left, middle)
            merge_sort(array, middle + 1, right)

            merge(array, left, middle, right)


        merge_sort(nums, 0, len(nums) - 1)

        return nums