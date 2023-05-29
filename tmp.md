# [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

###### tags: `leedcode` `easy`

Design a class to find the <code>k^th</code> largest element in a stream. Note that it is the <code>k^th</code> largest element in the sorted order, not the <code>k^th</code> distinct element.

Implement <code>KthLargest</code> class:

- <code>KthLargest(int k, int[] nums)</code> Initializes the object with the integer <code>k</code> and the stream of integers <code>nums</code>.
- <code>int add(int val)</code> Appends the integer <code>val</code> to the stream and returns the element representing the <code>k^th</code> largest element in the stream.


**Example 1:** 

```
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

 **Constraints:** 

- <code>1 <= k <= 10^4</code>
- <code>0 <= nums.length <= 10^4</code>
- <code>-10^4 <= nums[i] <= 10^4</code>
- <code>-10^4 <= val <= 10^4</code>
- At most <code>10^4</code> calls will be made to <code>add</code>.
- It is guaranteed that there will be at least <code>k</code> elements in the array when you search for the <code>k^th</code> element.

## Solution 1
```python=

```

>### Complexity
>|             | Time Complexity | Space Complexity |
>| ----------- | --------------- | ---------------- |
>| Solution 1  | O(n)            | O(1)             |


## Note
x


