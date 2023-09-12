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


## 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

`Boyer-Moore Voting Algorithm`

## 189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

`reverse two times is ok`

## 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

```python
def max_profix(nums):
    min = 0
    max_profit = 0
    for n in nums:
        if n < min:
            min = n
        if n - min > max_profit:
            max_profit = n - min
    return max_profit
```