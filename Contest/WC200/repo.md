# lc weekly contest 200
18/18
0:46:41 + error 3 = 1:01:41

简要写个repo

脑子的确不好使，而且又犯了不仔细看题目的老毛病，甚至还写错两个变量爆了两个error

------

下面说题目

- 5475 easy

    Bruteforce，这里注意是下标递增所以不要学我一开始写愣住了还排序了一下

- 5476 medium

    可以理解为某个排序过程的变种，注意这里k是连胜次数不是第k次获胜（只有我这样的傻逼会看错题目吧）

    分析一下会发现，数组可以拆分成 A max B 的形式，当A全部处理完之后便会停在最大值上，因此可以算出结果一定是max的lowerbound，那对于A部分，直接按照要求做就行了，遍历一遍，符合结果就返回，不符合就是max

- 5477 medium

    排序 + 贪心

    首先判断能否符合条件，遍历每行末尾0的数量，排序后和要求逐项比较；其次从高到低贪心的选取最靠前的符合要求的行（因为只要满足这一行一定能满足更低的），具体处理略，我是list pop元素做的

- 5478 hard

    贪心

    我一开始以为是dp，后来发现没法写，而且平方空间肯定会炸，仔细想了下就是O(m+n)贪心。

    其实就是两个严格升序数组，遇到相同的值就可以swap，那么把所有swap和开头结尾点加起来就可以把每个数组截成k+1段，贪心取每段最大值求和即可（这也配hard？）

------

说到底还是要静下心认真看题目，不要心浮气躁看一半就去兴冲冲写code（刷题几个月的老毛病了）

还有就是一些编程规范问题，包括变量命名之类的东西（x