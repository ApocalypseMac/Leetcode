# lc weekly contest 205

13/19

------

- 5507 easy
    按字母顺序对每个问号逐个模拟即可，为了方便处理开头和结尾可以在字符开头结尾加上特殊字符。注意前面的问号更新后会对后继问号产生影响。

- 5508 middle
    对于平方数值建立一个 Counter, 然后遍历可能的乘积并计数即可。

- 5509 middle
    我一开始想的 dp, 但是未优化字符集情况下会超时。实际上考虑 `"aaaaaabaaaa"` 这样的字符串，无论如何都不需要删除中间的 `'b'`, 换言之就是具有贪心性质。对于任意一段重复子序列，只需要保留权值最大的元素即可。

- 5510 hard
    看到题目懵了，实际上就是生成树的性质+连通分量的事情。并不需要具体求出需要删除哪些边，只需要计数即可（具有贪心选择性质）。首先 bfs/dfs 确定 A/B 是否可以遍历全部边，然后对于公共边计算连通分量数，这样就有了公共边需要保留的个数。对于保证连通，实际上需要保留的边数就是 A 和 B 的生成树边数减去公共边的保留数量，最后用总边数减即可。

------

这场周赛还是暴露了很多问题，还是要精刷题多总结。
