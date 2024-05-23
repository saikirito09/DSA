class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        for i in candies:
            if i + extraCandies >= max(candies):
                a.append(True)
            else:
                a.append(False)
        return a
        
