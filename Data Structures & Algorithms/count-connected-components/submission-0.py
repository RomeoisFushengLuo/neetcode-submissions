class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [0] * n

        def find(s: int) -> int:

            if parents[s] == s:
                return s 
            
            parents[s] = find(parents[s])
            return parents[s] 
        
        def union(i: int, j: int):

            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if rank[root_i] > rank[root_j]:
                    parents[root_j] = root_i
                elif rank[root_i] < rank[root_j]:
                    parents[root_i] = root_j
                else:
                    parents[root_i] = root_j
                    rank[root_j] += 1
                
                return True
            return False

        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1

        return res


        