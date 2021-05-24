'''二分查找实现'''
from sys import maxunicode
from typing import List

class BinarySearch:

    def solution1(self, array: List[int], value: int) -> int:
        '''
            有序数组中不存在重复元素的情况，如何存在重复的元素，返回位置为其中一个，无法确定
            非递归实现
        '''
        low, high = 0, len(array) - 1
        # 判断条件，注意 <=
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == value:
                return mid
            elif array[mid] < value:
                low += 1
            else:
                high -= 1
        return -1
    
    def solution2(self, array: List[int], value: int) -> int:
        '''
            有序数组中不存在重复元素的情况，如何存在重复的元素，返回位置为其中一个，无法确定
            递归实现
        '''
        return self.solution2_action(array, value, 0, len(array)-1)
    
    def solution2_action(self, array: List[int], value: int, low: int, high: int) -> int:
        if low > high:
            return -1
        mid = low + ((high - low) >> 1)
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            return self.solution2_action(array, value, mid+1, high)
        else:
            return self.solution2_action(array, value, low, mid-1)
    
    def solution3(self, array: List[int], value: int) -> int:
        '''查找第一个值等于给定值的元素'''
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] < value:
                low = mid + 1
            elif array[mid] > value:
                high = mid - 1
            else:
                if mid == 0 or array[mid-1] != value:
                    return mid
                else:
                    high = mid - 1
        return -1

    def solution4(self, array: List[int], value: int) -> int:
        '''查找最后一个值等于给定值的元素'''
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] < value:
                low = mid + 1
            elif array[mid] > value:
                high = mid - 1
            else:
                if mid == len(array) - 1 or array[mid+1] != value:
                    return mid
                else:
                    low = mid + 1
        return -1

    def solution5(self, array: List[int], value: int) -> int:
        '''查找第一个大于等于给定值的元素'''
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] >= value:
                if mid == 0 or array[mid-1] < value:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return -1

    def solution6(self, array: List[int], value: int) -> int:
        '''查找最后一个小于等于给定值的元素'''
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] <= value:
                if mid == len(array) - 1 or array[mid+1] > value:
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1
        return -1


class BinarySearchApplication:

    def square_root(self, digit: float, accuracy: float) -> float:
        '''求一个数的平方根，精确到小数点后六位'''
        low, high = 0, digit / 2
        while low <= high:
            mid = low + (high - low) / 2
            square_mid = mid * mid
            diff = square_mid - digit
            if abs(diff) <= accuracy:
                return round(mid, 6)
            elif diff > 0:
                high = mid
            else:
                low = mid
        return -1
