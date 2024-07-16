# 滑动窗口

## 1.介绍

滑动窗口是双指针问题的一种，通常用于解决**子数组**、**子串**、**字符串**等问题。滑动窗口的核心是窗口中的内容，而双指针的核心是两个指针。

通常情况下，我们在处理子数组/子串等问题时，会按照如下处理方式

```python
for left in range(len(nums)):
    for right in range(left, len(nums)):
# nums[left, right] 是一个子数组

```

这样处理的方式，时间复杂度是O(n^2)，显然，这种处理方式太慢了。

滑动窗口的核心思想是，我们用一个窗口来维护一个子数组/子串，窗口的左边界和右边界分别是i和j，窗口的右边界向右移动，当满足某种条件时，窗口的左边界向右
移动，直到窗口满足某种条件。代码如下:

```python
left, right = 0, 0
while right < len(nums):
    # 增大窗口
    window.add(nums[right])
    right += 1
    # 判断是否要收缩
    while window_needs_shrink:
        # 缩小窗口
        window.remove(nums[left])
        left += 1

```

在这段代码中，while循环中嵌套了while循环，但是，它的时间复杂度是O(n)，因为left和right没有进行回退，每个元素只访问一次(
上述的暴力求解代码中，每次外层循环开始时，right从left + 1开始，增长到len(nums)，会进行回退，所以时间复杂度是O(n^2))。

> 需要注意的是，滑动窗口并**不能枚举**所有的子数组/子串，但是，它却可以枚举**所有满足某种条件**的子数组/子串。