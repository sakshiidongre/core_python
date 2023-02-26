graph = {
 'A' : ['B','C'],
 'B' : ['D'],
 'C' : ['G', 'H'],
 'D' : ['E', 'F',],
 'E' : [],
 'F' : [],
 'G' : ['I'],
 'H' : []
}
path = list()
def DFS(SNode,ENode,graph,maxDepth,curList):
    curList.append(SNode)
    if SNode==ENode:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[SNode]:
        if DFS(node,ENode,graph,maxDepth-1,curList):
            return True
        else:
            curList
    return False
def iterativeDDFS(SNode,ENode,graph,maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(SNode,ENode,graph,i,curList):
            return True
    return False
Gnode= input("Goal Node: ")
MDepth= int(input("Maximum Depth: "))
if not iterativeDDFS('A',Gnode,graph,MDepth):
    print("Path does not exist")
else:
    print("Path exists: ")
    print(path.pop())