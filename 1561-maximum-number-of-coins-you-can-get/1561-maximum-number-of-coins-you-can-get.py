class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = deque(sorted(piles))
        total = 0

        while piles:
            piles.pop()
            total += piles.pop()
            piles.popleft()

        return total