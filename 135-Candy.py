class Solution:
    """
   It first initializes an array candies with each child having one candy.

   Then, it makes two passes over the ratings array: first from left to right and then from right to left.

   In each pass, it adjusts the number of candies for each child based on their ratings and neighboring ratings.
    """

    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        # start to end
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # end to start
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    solution = Solution()
    r = [1, 0, 2]
    assert 5 == solution.candy(r)
