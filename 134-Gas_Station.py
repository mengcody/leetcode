class Solution:
    """
    一个环形的路，给定两个数组gas, cost，gas表示在加油站数组，cost表示油费
    gas[i] 表示在这个加油站能加多少油
    cost[i] 表示从这个加油站到下一个加油站需要多少油

    solution: greedy algorithm
    从起点开始, 就是走，

    To solve this problem, we can use a greedy algorithm.

    We'll traverse the stations in a circular manner and keep track of the current gas in the tank.

    If at any point the gas in the tank becomes negative, we'll reset the start station to the current station and reset
    the gas tank.

    We'll also keep track of the total gas and total cost.
    At the end, if the total gas is greater than or equal to the total cost, we'll return the start station;
    otherwise, we'll return -1.
    """

    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = 0
        total_cost = 0
        start_station = 0
        current_gas = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_station = i + 1
                current_gas = 0

        return start_station if total_gas >= total_cost else -1


if __name__ == "__main__":
    solution = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert 3 == solution.can_complete_circuit(gas, cost)
