class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total = sum(map(sum, grid))

        def canPartition(g):
            topSum = 0
            seen = set()  # cells seen in top section so far
            for i, row in enumerate(g):
                topSum += sum(row)
                botSum = total - topSum
                seen |= set(row)
                diff = topSum - botSum
                if diff in (0, g[0][0], g[0][-1], row[0]):
                    return True

                if len(g[0]) > 1 and i > 0 and diff in seen:
                    return True

            return False

        return (
            canPartition(grid) or              
            canPartition(grid[::-1]) or        
            canPartition(list(zip(*grid))) or  
            canPartition(list(zip(*grid))[::-1]) 
        )