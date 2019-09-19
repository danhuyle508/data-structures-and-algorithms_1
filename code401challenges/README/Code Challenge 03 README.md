# Challenge Summary
This is the code challenge for Binary Search.
## Challenge Description
Given an ordered array and a key, find if the key is in the array and return the index. Otherwise return -1 if not found.
## Approach & Efficiency
I overloaded this code challenge in order to use recursion without passing in start and end the first time around.
Time: O(logn2)
everytime the key is not found, the sample size becomes half.
Space: O(1)
No new variable of significance is made aside from start, end, and mid which should not be a big deal.
## Solution
![image]()