class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def gain(p, t):
            return (p + 1) / (t + 1.0) - p / float(t)

   # build a max heap by negative gain (since heapq is min-heap)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        return sum(p * 1.0 / t for _, p, t in heap) / len(heap)