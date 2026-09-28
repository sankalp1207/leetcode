class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        d={}
        for edge in edges:
            if edge[0] in d:
                d[edge[0]].append(edge[1])
            else:
                d[edge[0]]=[edge[1]]
            if edge[1] in d:
                d[edge[1]].append(edge[0])
            else:
                d[edge[1]]=[edge[0]]
        print(d)
        print(len(d))
        maxE=1
        for i in range(2,len(d)+1):
            if(len(d[i]) > len(d[maxE])):
                maxE=i
        return maxE