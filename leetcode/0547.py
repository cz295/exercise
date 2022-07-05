class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import defaultdict
        n = len(isConnected)
        node_to_node = defaultdict(list)
        node_dict = {}
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    node_to_node[j].append(i)
                    node_to_node[i].append(j)

        def dfs(x):
            print(node_dict, x)
            for _x in node_to_node[x]:
                if _x not in node_dict:
                    node_dict[_x] = node_dict[x]
                    dfs(_x)

        for x in range(n):
            if x not in node_dict:
                node_dict[x] = x
                dfs(x)
        return len(Counter(node_dict.values()))
    
    
#         l = len(isConnected)
#         seen = set()
#         province = 0
        
#         def dfs(i):
#             for j in range(l):
#                 if j not in seen and isConnected[i][j]:
#                     seen.add(j)
#                     dfs(j)

#         for i in range(l):
#             if i not in seen:
#                 province += 1
#                 seen.add(i)
#                 dfs(i)
            
                
#         return province
