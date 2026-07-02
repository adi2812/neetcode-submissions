class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for i,j in prerequisites:
            if i in preMap:
                preMap[i].append(j)
            else:
                preMap[i] = [j]
        
        visit = set()

        def dfs(var):
            if var in visit:
                return False
            if preMap[var] == []:
                return True
            visit.add(var)
            for j in list(preMap[var]):
                if not dfs(j):
                    return False
                preMap[var].remove(j)
            visit.remove(var)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True