# array/string

## 88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.


```python
def solution(arr):
    fast, slow = 0, 0
    for fast in arr:
        if fast != arr[slow]:
            arr[slow+1] = fast
            slow += 1

    return slow + 1

```

## 27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

## 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

## 80. Remove Duplicates from Sorted Array II

