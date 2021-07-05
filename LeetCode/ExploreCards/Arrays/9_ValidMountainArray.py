'''
Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
    Input: arr = [2,1]
    Output: false

Example 2:
    Input: arr = [3,5,5]
    Output: false

Example 3:
    Input: arr = [0,3,2,1]
    Output: true

Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^4
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Solution below
        if len(arr) < 3:
            return False
        key = None
        flag = False
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                return False
            if arr[i-1] < arr[i] and len(arr)-1 != i and not key:
                flag = True
                continue
            elif arr[i-1] < arr[i] and len(arr)-1 == i and not key:
                return False
            elif not key:
                key = arr[i-1]
            if key and flag:
                if arr[i-1] > arr[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True
        