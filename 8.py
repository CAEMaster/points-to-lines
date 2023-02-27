from abaqus import *
from abaqusConstants import *

session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.unsetPrimaryObject()
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(5.0, 5.0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s, depth=2.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-1']
del p.features['Solid extrude-1']


f1 = open('D:/work/2/0227/9/cord.txt')
b1=f1.readlines()
end1=len(b1)
p = mdb.models['Model-1'].parts['Part-1']
for x in range(end1):
       p.DatumPointByCoordinate(coords=(float(b1[x].split('\t')[0].split(',')[0]), float(b1[x].split('\t')[1].split(',')[0]), float(b1[x].split('\t')[2].split(',')[0])))


d1 = p.datums
p.WireSpline(points=(d1.values()), mergeType=IMPRINT, meshable=ON, 
    smoothClosedSpline=ON)


