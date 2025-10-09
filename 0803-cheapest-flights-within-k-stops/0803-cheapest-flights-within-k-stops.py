class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10**9
        dist = [INF] * n
        dist[src] = 0
        
        for _ in range(k + 1):
            backup = dist.copy()

            for from_city, to_city, price in flights:
                if backup[from_city] != INF:
                    dist[to_city] = min(dist[to_city], backup[from_city] + price)
            
        return -1 if dist[dst] == INF else dist[dst]