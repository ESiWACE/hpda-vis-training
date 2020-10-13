# state file generated using paraview version 5.8.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import sys

try:
  LoadPlugin('/opt/paraview/lib/paraview-5.8/plugins/CDIReader/CDIReader.so', remote=False, ns=globals())
except:
  print ("WARNING: Could not explicitly load CDI NetCDF reader plugin.\nIf things run fine, it might already be loaded.\n", file=sys.stderr)

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1920, 1080]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, 0.0, -1.0]
renderView1.UseLight = 0
renderView1.FillLightKFRatio = 1.0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [12.316810668886477, -2.9025359883208424, 1294.9254852830063]
renderView1.CameraFocalPoint = [12.316810668886477, -2.9025359883208424, -1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 189.04418487039632
renderView1.CameraParallelProjection = 1
renderView1.Background = [1.0, 0.0, 0.4980392156862745]


SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Plane'
plane1 = Plane()
plane1.Origin = [-300.0, -150.0, -1000.0]
plane1.Point1 = [300.0, -150.0, -1000.0]
plane1.Point2 = [-300.0, 150.0, -1000.0]

# create a new 'CDIReader'
uvnc = CDIReader(FileNames=['uv.nc'])
uvnc.Dimensions = '(clon, clat, depth)'
uvnc.CellArrayStatus = ['u', 'v']
uvnc.LayerThickness = 50

# create a new 'Plane'
plane2 = Plane()

# create a new 'Texture Map to Plane'
textureMaptoPlane2 = TextureMaptoPlane(Input=plane2)

# create a new 'Calculator'
calculator1 = Calculator(Input=uvnc)
calculator1.AttributeType = 'Cell Data'
calculator1.ResultArrayName = 'speed'
calculator1.Function = 'sqrt(u*u+v*v)'

# create a new 'Texture Map to Plane'
textureMaptoPlane1 = TextureMaptoPlane(Input=plane1)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'speed'
speedLUT = GetColorTransferFunction('speed')
speedLUT.AutomaticRescaleRangeMode = 'Never'
speedLUT.RGBPoints = [0.0, 0.031373, 0.25098, 0.505882, 0.062745, 0.031373, 0.329719, 0.590527, 0.12549, 0.031911, 0.408397, 0.674787, 0.1882355, 0.100807, 0.479262, 0.710219, 0.2509805, 0.169704, 0.550219, 0.745744, 0.31372550000000005, 0.238601, 0.62699, 0.787082, 0.3764705, 0.307958, 0.703114, 0.826759, 0.4392155, 0.39654, 0.752326, 0.797232, 0.501960785, 0.485121, 0.801046, 0.767705, 0.564706, 0.573702, 0.83451, 0.738178, 0.6274510000000001, 0.661592, 0.867743, 0.711034, 0.690196, 0.732457, 0.895302, 0.74253, 0.7529410000000001, 0.801845, 0.922307, 0.774579, 0.8156865, 0.841215, 0.938055, 0.817885, 0.8784315, 0.880907, 0.95391, 0.861084, 0.9411765000000001, 0.926182, 0.971626, 0.902422, 1.0, 0.968627, 0.988235, 0.941176]
speedLUT.ColorSpace = 'Lab'
speedLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'speed'
speedPWF = GetOpacityTransferFunction('speed')
speedPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['CELLS', 'speed']
calculator1Display.LookupTable = speedLUT
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 59.997473144531256
calculator1Display.SelectScaleArray = 'speed'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'speed'
calculator1Display.GaussianRadius = 2.9998736572265625
calculator1Display.SetScaleArray = [None, '']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = [None, '']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = speedPWF
calculator1Display.ScalarOpacityUnitDistance = 10.74003524973295

# show data from textureMaptoPlane1
textureMaptoPlane1Display = Show(textureMaptoPlane1, renderView1, 'GeometryRepresentation')

# a texture
world2 = CreateTexture("world.topo.200402.3x1920.png")

# trace defaults for the display properties.
textureMaptoPlane1Display.Representation = 'Surface'
textureMaptoPlane1Display.ColorArrayName = [None, '']
textureMaptoPlane1Display.Texture = world2
textureMaptoPlane1Display.SelectOrientationVectors = 'None'
textureMaptoPlane1Display.ScaleFactor = 60.0
textureMaptoPlane1Display.SelectScaleArray = 'None'
textureMaptoPlane1Display.GlyphType = 'Arrow'
textureMaptoPlane1Display.GlyphTableIndexArray = 'None'
textureMaptoPlane1Display.GaussianRadius = 3.0
textureMaptoPlane1Display.SetScaleArray = ['POINTS', 'Normals']
textureMaptoPlane1Display.ScaleTransferFunction = 'PiecewiseFunction'
textureMaptoPlane1Display.OpacityArray = ['POINTS', 'Normals']
textureMaptoPlane1Display.OpacityTransferFunction = 'PiecewiseFunction'
textureMaptoPlane1Display.DataAxesGrid = 'GridAxesRepresentation'
textureMaptoPlane1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
textureMaptoPlane1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
textureMaptoPlane1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for speedLUT in view renderView1
speedLUTColorBar = GetScalarBar(speedLUT, renderView1)
speedLUTColorBar.WindowLocation = 'AnyLocation'
speedLUTColorBar.Position = [0.9376054318488528, 0.36798941798941803]
speedLUTColorBar.Title = 'speed'
speedLUTColorBar.ComponentTitle = ''
speedLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
speedLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
speedLUTColorBar.ScalarBarLength = 0.3299999999999998

# set color bar visibility
speedLUTColorBar.Visibility = 1

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(uvnc)
# ----------------------------------------------------------------
view = GetActiveView()

reader=GetActiveSource()
tsteps=reader.TimestepValues
print ("Timesteps: ", ", ".join((str (x) for x in tsteps)))
for n,t in enumerate (tsteps):
    print ("rendering for time %f"%t)
    view.ViewTime = t
    SaveScreenshot('pink_background_%04d.png'%n, layout1, ImageResolution=[1920, 1080])
