"""
问题：深度克隆图
思路：BFS和建立neighbors联系
1. 生成新root，加入到Q，生成新map，将root加入到map
2. 当q还有东西时：curr = q.pop(0);
3. for每一个q中的node，查看是否已经克隆过(map)，如果没有，克隆并加入map
4. 将curr的neighbors clone加入curr的克隆的neighbors
完成
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        copied = {}
        copied[root.label] = root
        q = [node]
        while q:
            curr = q.pop(0)
            for n in curr.neighbors:
                if n.label not in copied:
                    q.append(n)
                    copied[n.label] = UndirectedGraphNode(n.label)
                copied[curr.label].neighbors.append(copied[n.label])
        return root
