class Solution:
    """
    solution1: 暴力破解
    """

    def h_index(self, citations: list[int]) -> int:
        h = len(citations)
        while h > 0:
            count = 0
            for i in citations:
                # check if have h element is bigger than h
                # if true then the h is the h-index
                if i >= h:
                    count += 1
            print(f"h={h}, count={count}")
            if count >= h:
                return h
            h -= 1
        return h

    """
    soulution2: 排序，然后直接遍历，取值
    """

    def h_index2(self, citations: list[int]) -> int:
        # 从小到大排序
        citations.sort(reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index += 1

            else:
                break

        return h_index


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    assert 3 == Solution().h_index(citations)
