ExtAPI.DataModel.Project.Model.Analyses[0].MeshData
ExtAPI.DataModel.AnalysisList[0].MeshData


# md has Ansys.ACT.Common.Mesh.MeshWrapper, Ansys.ACT.Common.Mesh.ElementWrapper, Ansys.ACT.Common.Mesh.NodeWrapper
Elements
ElementCount
ElementById
ElementIds
ElementIdsFromNodeIds

Nodes
NodeCount
NodeIds
NodeIdsFromElementIds
NodeById

GetElementEdges
GetElementFaces



e1 = md.ElementById(49)
e1.Nodes.Count
e1.CornerNodes.Count
e1.NodeIds
e1.CornerNodesIds
# selinfo = sm.CreateSelectionInfo(SelectionTypeEnum.MeshNodes) 
selinfo.Ids = e1.NodeIds
sm.NewSelection(selinfo)
sm.NewSelection(selinfo)
e1.GetBody()


n1 = e1.Nodes[0]
n1.GetBody()

A = Assembly
B = MeshData


sm =ExtAPI.SelectionManager
selinfo = sm.CreateSelectionInfo(SelectionTypeEnum.MeshElements)
selinfo = sm.CreateSelectionInfo(SelectionTypeEnum.MeshNodes)
selinfo.Ids = [int of element id]
sm.NewSelection(selinfo)

