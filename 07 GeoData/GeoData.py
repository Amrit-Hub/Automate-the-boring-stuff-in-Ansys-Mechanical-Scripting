# Geometry object, selection manager, geodata(geomtery wrapper)

# access geodata:
ExtAPI.DataModel.Project.Model.Analyses[0].GeoData
ExtAPI.DataModel.GeoData
ExtAPI.DataModel.AnalysisList[0].GeoData

# methods/prop with geodata gd
Assemblies
GeoEntityById
GetType
ToString

# A = body
# B = Selection info
# C = geo data

# A to B
Model.Geometry.Bodies[0].getgeobody()

# B to C
selinfo.Ids = bodygeodata.Id

# C to B
gd.geoentitybyid(int from selinfo)

# B to A
geomtery.getbody(body geo data)
geometry.getbody(part geo data)

GeoBodyTypeEnum -  		GeoBodySheet Sheet.
						GeoBodySolid Solid.
						Unknown type.
						GeoBodyUnknown
						GeoBodyWire
GeoCurveTypeEnum - 		GeoCurveBSpline BSpline.
						GeoCurveCircle Circle.
						GeoCurveCircularArc Circular Arc.
						GeoCurveEllipseFull Full Ellipse.
						GeoCurveEllipticalArc Elliptical Arc
						GeoCurveFaceted Faceted Curve.
						GeoCurveLine Line.
						GeoCurveLineSegment Line Segment.
						GeoCurveNoGeometry No Geometry.
						GeoCurveUnknown Unknown type.
GeoSurfaceTypeEnum - 	GeoSurfaceBSpline BSpline.
						GeoSurfaceCone Cone.
						GeoSurfaceCylinder Cylinder.
						GeoSurfaceEllipticalCone Elliptical Cone.
						GeoSurfaceEllipticalCylinder Elliptical Cylinder.
						GeoSurfaceFaceted Faceted.
						GeoSurfaceNoGeometry No Geometry.
						GeoSurfacePlane Plane.
						GeoSurfaceSphere Sphere.
						GeoSurfaceTorus Torus.
						GeoSurfaceUnknown Unknown type.




