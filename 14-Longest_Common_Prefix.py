class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        """
        solution1
        :param strs:
        :return:
        """
        ans = ""
        # 1. 先排序
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        # 2. 然后比较第一个和最后一个就好了
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        return ans

    def longest_common_prefix2(self, strs: list[str]) -> str:
        """
        solution2
        1. 以第一个为标准，因为如果是最长的公共子串，则一定也在这个里面
        2. 
        """
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for w in strs[1:]:
                # 到了这个单词的末尾，后者不等了就直接返回
                if i == len(w) or w[i] != base[i]:
                    return base[0:i]

        return base


if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    assert "fl" == solution.longest_common_prefix(strs)
    assert "fl" == solution.longest_common_prefix2(strs)
