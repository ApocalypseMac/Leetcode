# lc weekly contest 222

18/18

------

- 1710 easy

    按照每个箱子权重降序排序，依次选取。

- 1711 medium

    类似 two sum 的解法，遍历的两数之和变成 $2^0 ~ 2^21$ 之间的幂次，为了避免重复可以先排序。

- 1712 medium

    遍历左数组的边界，用两个指针确定满足要求的中间数组右边界的左右可取范围，显然随着左边界递增，左右界均递增，因此可以双指针处理。对于计算连续子数组和，可以用前缀和优化。同样地，也可以用二分来计算每次边界可取范围。

- 1713 hard

    本质上是求解 `target` 和 `arr` 的最长公共子序列，但是由于数据范围 $O(n^2)$ 过不了。考虑 `target` 不包含重复元素，因此可以建立 `target` 数组值和下标的一一映射。这样就可以提取出 `arr` 中存在于 `target` 的元素并转化为下标，进而问题就变成了求新数组的最长递增子序列了，而后者有 `O(n\log(n))` 的算法。

------