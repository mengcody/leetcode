# preface

all the question are traverse all the element and do some action when we visit the element.

then it becomes another question: 

* how to traverse all the element?

  * array/linkedlist： 
    * from begin to the end or from the end to begin
    * with two iterator to traverse
  * tree
  * graph

* how to traverse all the element with the fast way:

  * dynamic pragraming
  * greedy algorithm
  * backtracking algorithm
  * some other tricks

* how to deal the element which traversed in the way

  * it depends on the question which you are going to solve

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

## 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

## 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## 45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 