class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        if len(coins) == 1:
            if coins[0] > amount or amount % coins[0] > 0:
                return -1
            else:
                return amount // coins[0]

        coins.sort()

        # [0...amount]
        fewest_num_for_amount = [float('inf')] * (amount+1)
        fewest_num_for_amount[0] = 0
        if coins[0] > 1:
            return -1
        fewest_num_for_amount[1] = 1
        # fewest_num_for_amount[2] = fewest_num_for_amount[2-1]+1

        for i in range(2, len(fewest_num_for_amount)):

            for coin in coins:
                if coin > i:
                    break
                elif coin == i:
                    fewest_num_for_amount[i] = 1
                else:
                    fewest_num_for_amount[i] = min(fewest_num_for_amount[i], 
                                fewest_num_for_amount[(i - coin)] + 1)
                    if i % coin == 0:
                        fewest_num_for_amount[i] = min(fewest_num_for_amount[i], i//coin)

        return int(fewest_num_for_amount[-1])
            