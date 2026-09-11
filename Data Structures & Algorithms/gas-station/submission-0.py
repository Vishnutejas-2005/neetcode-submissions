class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gas = 0
        total_gas = 0
        idx = 0

        n = len(gas)

        for i in range(n):
            curr_gas += gas[i]-cost[i]
            total_gas += gas[i]-cost[i]

            if curr_gas < 0:
                curr_gas = 0
                idx = i+1

        if total_gas <0:
            return -1

        return idx
        