class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0


        for i in range(k+1):
            tmp = prices[:]

            for s,d,p in flights:

                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmp[d]:
                    tmp[d] = prices[s] + p
            prices = tmp

        return -1 if prices[dst] == float('inf') else prices[dst]