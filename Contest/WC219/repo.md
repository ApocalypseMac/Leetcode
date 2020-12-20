# lc weekly contest 219

18/18

------

- 1688 easy

    `n` 个队伍，淘汰赛，决出冠军需要的比赛场数就是淘汰的对数 `n - 1`.

- 1689 medium

    贪心。每次取尽可能多的 `1`, 最终需要的数量就是数值最大的位。

- 1690 medium

    区间 `dp`. 和 Atcoder 的 L 题几乎一样。最优选择目标是使得两人分差（相减，并非绝对值）最小。由于每次得分和区间和有关，因此需要前缀和。每次转移就是取左和取右，因为**更换先后手**所以应当**减去**子区间的结果。

- 1691 hard

    首先数据范围肯定不能暴力搜索。因此需要对于不同的方块建立一个有序的关系，使得在前面的方块必定在下面。显然可知，如果一个方块的最短边长比另一个长，那么它一定不可能在另一块上面。因此就确定了一个偏序关系。将每个方块边升序排序然后按照最短边降序排序。

    继续观察可知，无论怎么摆放，使得长大于等于宽一定是更优的，因此对于每个方块有三种摆放方式，`dp[i][j]` 定义为第 `i` 个方块为顶部，高为 `j` 边时的最大高度，然后按要求转移即可。

    上述的复杂度已经足够解决此问题的，不过还可以进一步优化，事实上通过遍历不同的摆放方式，我们可以发现，原有的任何可行堆叠方法中将最长边作为高度依旧可行。这样每个方块的摆放方式就确定了。

------

还是脑子不清醒手不熟，做 `dp` 尤其应该思路清晰。