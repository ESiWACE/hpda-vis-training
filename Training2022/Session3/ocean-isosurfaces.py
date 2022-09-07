# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

LoadDistributedPlugin('CDIReader', ns=globals())


# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [3640, 2310]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.007415771484375, 3.145111083984375, -53.40749740600586]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.007415771484375, 3.145111083984375, 1007.7768969051635]
renderView1.CameraFocalPoint = [0.007415771484375, 3.145111083984375, -53.40749740600586]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 332.3322252521097
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(3640, 2310)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

if __name__ == '__main__':
  import sys
  filenames = sys.argv[1:]
else:
  filenames = [ '/tmp/hpda-vis-training/Training2022/Session3/oce_3d_r2b4.nc' ]

# create a new 'CDIReader'
ngc2013_oce_r2b6nc = CDIReader(registrationName='ngc2013_oce_r2b6.nc', FileNames=filenames)
ngc2013_oce_r2b6nc.Dimensions = '(clon, clat, depth)'
ngc2013_oce_r2b6nc.CellArrayStatus = ['to', 'so', 'u', 'v', 'heat_content_liquid_water']
ngc2013_oce_r2b6nc.Show3DSurface = 1
ngc2013_oce_r2b6nc.LayerThickness = 100
ngc2013_oce_r2b6nc.VerticalLevel = 63

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=ngc2013_oce_r2b6nc)
threshold1.Scalars = ['CELLS', 'so']
threshold1.LowerThreshold = 0.1
threshold1.UpperThreshold = 999.0

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'velmag'
calculator1.Function = 'mag(u*iHat+v*jHat)'

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=calculator1)
cellDatatoPointData1.CellDataArraytoprocess = ['Center Latitude (CLAT)', 'Center Longitude (CLON)', 'heat_content_liquid_water', 'so', 'to', 'u', 'v', 'velmag']

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'velmag']
contour1.Isosurfaces = [0.7412541514113079, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7, 0.8, 0.9000000000000001, 1.0]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'u'
uLUT = GetColorTransferFunction('u')
uLUT.AutomaticRescaleRangeMode = 'Never'
uLUT.RGBPoints = [-1.0, 0.231373, 0.298039, 0.752941, 0.0, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'u']
contour1Display.LookupTable = uLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'velmag'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 59.997473144531256
contour1Display.SelectScaleArray = 'velmag'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'velmag'
contour1Display.GaussianRadius = 2.9998736572265625
contour1Display.SetScaleArray = ['POINTS', 'velmag']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'velmag']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.2, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.2, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'u'
uLUTColorBar.ComponentTitle = ''

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'u'
uPWF = GetOpacityTransferFunction('u')
uPWF.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(contour1)
# ----------------------------------------------------------------



# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'TimeStep'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [3640, 2310]
pNG1.Writer.Format = 'PNG'

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
