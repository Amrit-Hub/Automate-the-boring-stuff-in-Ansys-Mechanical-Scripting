SM = ExtAPI.SelectionManager
selinfo = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selinfo.Ids = [ids of GeometryEntities]
SM.NewSelection(selinfo)