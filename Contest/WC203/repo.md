# lc weekly contest 203

7/20

最后一题超时，倒数第二题没写完（菜)

------

- 5495 easy
    只需要看首尾，同时计算是否过了一圈

- 5496 medium
    贪心，每次取最大的两个和最小的两个，取中间即可。

- 5497 medium
    并查集或者哈希表，维护区间并判断长度。对于哈希表，映射每段区间的左右邻居，当**区间发生改动**时判断改动前区间长度是否符合要求，是的话那么在上一个时间点符合要求的区间存在。另外要注意如果区间长度等于总长度需要直接返回。

- 5498 hard
    区间dp，打表 $O(n^3)$ 会被卡常TLE，此时需要用记忆化搜索来优化时间（避免计算很多较长区间的dp值）。当然，由于结果的单调性，事实上可以通过维护左右最优解来在平方时间内打表。

------

没啥想说的，菜