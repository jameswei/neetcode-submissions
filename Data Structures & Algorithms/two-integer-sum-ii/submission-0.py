class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            if numbers[0]+numbers[1] == target:
                return [1,2]

        # numbers is already sorted, 
        # two pointers from head and tail
        i, j = 0, len(numbers)-1

        # i == j is not allowed
        while i < j:
            a, b = numbers[i], numbers[j]
            print(f"i: {i}, j: {j}, [i]: {a}, [j]: {b}, sum: {a+b}")
            if a+b == target:
                break

            # move i to right
            elif a+b < target:
                i += 1

            # a+b > target
            # move j to left
            else:
                j -= 1

        # either i == j without answer or found answer
        # it's said that there will always be exactly one valid answer

        return [i+1, j+1]