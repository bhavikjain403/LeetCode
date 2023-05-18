class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        all_nodes = set(range(n))
        destination_nodes = set(destination for _, destination in edges)
        source_nodes = all_nodes - destination_nodes
        return list(source_nodes)