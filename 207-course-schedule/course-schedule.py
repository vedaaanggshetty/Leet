class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        g = defaultdict(list)
        states = [0] * numCourses
        visiting = 1
        visited = 2

        for u,v in prerequisites:
            g[u].append(v)

        def dfs(node):

            if states[node] == visited:
                return True
            elif states[node] == visiting:
                return False

            states[node] = visiting
            for n in g[node]:
                if not dfs(n):
                    return False

            states[node] = visited
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True        
        
        