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

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.

```python
def solution(arr):
    fast, slow = 0, 0
    for fast in arr:
        if fast != arr[slow]:
            arr[slow + 1] = fast
            slow += 1

    return slow + 1
```

## 27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements in nums which are not equal to val.

## 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements
in nums.

## 80. Remove Duplicates from Sorted Array II

## 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

`Boyer-Moore Voting Algorithm`

## 189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

`reverse two times is ok`

## 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to
sell that stock.

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

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

## 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## 45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at
nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach
nums[n - 1].

## 274. H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith
paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the
given researcher has published at least h papers that have each been cited at least h times.

## 380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

* RandomizedSet() Initializes the RandomizedSet object.
* bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false
  otherwise.
* bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false
  otherwise.
* int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element
  exists when this method is called). Each element must have the same probability of being returned.
* You must implement the functions of the class such that each function works in average O(1) time complexity.

## 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## 134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)
th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once
in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

## 135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children

## 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.

## 13. Roman to Integer

## 12. Integer to Roman

## 58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

## 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## 151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only
have a single space separating the words. Do not include any extra spaces.

## 6. Zigzag Conversion

## 28. Find the index of the first occurrence in a string

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

## 29. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra
spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

## 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## 392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "
abcde" while "aec" is not).

## 167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <=
index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## 11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## 209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
sum is greater than or equal to target. If there is no such subarray, return 0 instead.

## 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
