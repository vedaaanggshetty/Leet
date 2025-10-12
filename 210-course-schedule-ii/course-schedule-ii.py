class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        res = []
        visited = [0] * numCourses
        cycle = [False]
        
        graph = defaultdict(list)
        p = prerequisites
        for u,v in p:
            graph[v].append(u)


        def dfs(n):

            if visited[n] == 1:
                cycle[0] = True
                return
            
            if visited[n] == 2:
                return 

            visited[n] = 1
            for nei in graph[n]:
                dfs(nei)
            visited[n] = 2
            res.append(n)


        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)

            if cycle[0]:
                return []

        return res[::-1]
            

    