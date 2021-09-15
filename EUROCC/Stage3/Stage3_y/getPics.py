# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
import sys
ofoam = OpenFOAMReader(FileName=''+str(sys.argv[1])+'o.foam')
ofoam.SkipZeroTime = 1
ofoam.CaseType = 'Reconstructed Case'
ofoam.LabelSize = '32-bit'
ofoam.ScalarSize = '64-bit (DP)'
ofoam.Createcelltopointfiltereddata = 1
ofoam.Adddimensionalunitstoarraynames = 0
ofoam.MeshRegions = ['internalMesh']
ofoam.CellArrays = []
ofoam.PointArrays = []
ofoam.LagrangianArrays = []
ofoam.Cachemesh = 1
ofoam.Decomposepolyhedra = 1
ofoam.ListtimestepsaccordingtocontrolDict = 0
ofoam.Lagrangianpositionswithoutextradata = 1
ofoam.Readzones = 0
ofoam.Copydatatocellzones = 0
# get active source.
ofoam = GetActiveSource()

# Properties modified on ofoam
ofoam.MeshRegions = ['back', 'baffles', 'bf1_left', 'bf1_right', 'bf2_left', 'bf2_right', 'bf3_left', 'bf3_right', 'bottom', 'top']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1555, 568]

# show data in view
ofoamDisplay = Show(ofoam, renderView1)

# trace defaults for the display properties.
ofoamDisplay.Representation = 'Surface'
ofoamDisplay.AmbientColor = [1.0, 1.0, 1.0]
ofoamDisplay.ColorArrayName = [None, '']
ofoamDisplay.DiffuseColor = [1.0, 1.0, 1.0]
ofoamDisplay.LookupTable = None
ofoamDisplay.MapScalars = 1
ofoamDisplay.MultiComponentsMapping = 0
ofoamDisplay.InterpolateScalarsBeforeMapping = 1
ofoamDisplay.Opacity = 1.0
ofoamDisplay.PointSize = 2.0
ofoamDisplay.LineWidth = 1.0
ofoamDisplay.RenderLinesAsTubes = 0
ofoamDisplay.RenderPointsAsSpheres = 0
ofoamDisplay.Interpolation = 'Gouraud'
ofoamDisplay.Specular = 0.0
ofoamDisplay.SpecularColor = [1.0, 1.0, 1.0]
ofoamDisplay.SpecularPower = 100.0
ofoamDisplay.Luminosity = 0.0
ofoamDisplay.Ambient = 0.0
ofoamDisplay.Diffuse = 1.0
ofoamDisplay.EdgeColor = [0.0, 0.0, 0.5]
ofoamDisplay.BackfaceRepresentation = 'Follow Frontface'
ofoamDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
ofoamDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
ofoamDisplay.BackfaceOpacity = 1.0
ofoamDisplay.Position = [0.0, 0.0, 0.0]
ofoamDisplay.Scale = [1.0, 1.0, 1.0]
ofoamDisplay.Orientation = [0.0, 0.0, 0.0]
ofoamDisplay.Origin = [0.0, 0.0, 0.0]
ofoamDisplay.Pickable = 1
ofoamDisplay.Texture = None
ofoamDisplay.Triangulate = 0
ofoamDisplay.UseShaderReplacements = 0
ofoamDisplay.ShaderReplacements = ''
ofoamDisplay.NonlinearSubdivisionLevel = 1
ofoamDisplay.UseDataPartitions = 0
ofoamDisplay.OSPRayUseScaleArray = 0
ofoamDisplay.OSPRayScaleArray = ''
ofoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ofoamDisplay.OSPRayMaterial = 'None'
ofoamDisplay.Orient = 0
ofoamDisplay.OrientationMode = 'Direction'
ofoamDisplay.SelectOrientationVectors = 'None'
ofoamDisplay.Scaling = 0
ofoamDisplay.ScaleMode = 'No Data Scaling Off'
ofoamDisplay.ScaleFactor = 0.04869999885559082
ofoamDisplay.SelectScaleArray = 'None'
ofoamDisplay.GlyphType = 'Arrow'
ofoamDisplay.UseGlyphTable = 0
ofoamDisplay.GlyphTableIndexArray = 'None'
ofoamDisplay.UseCompositeGlyphTable = 0
ofoamDisplay.UseGlyphCullingAndLOD = 0
ofoamDisplay.LODValues = []
ofoamDisplay.ColorByLODIndex = 0
ofoamDisplay.GaussianRadius = 0.0024349999427795413
ofoamDisplay.ShaderPreset = 'Sphere'
ofoamDisplay.CustomTriangleScale = 3
ofoamDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
ofoamDisplay.Emissive = 0
ofoamDisplay.ScaleByArray = 0
ofoamDisplay.SetScaleArray = [None, '']
ofoamDisplay.ScaleArrayComponent = 0
ofoamDisplay.UseScaleFunction = 1
ofoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ofoamDisplay.OpacityByArray = 0
ofoamDisplay.OpacityArray = [None, '']
ofoamDisplay.OpacityArrayComponent = 0
ofoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ofoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
ofoamDisplay.SelectionCellLabelBold = 0
ofoamDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
ofoamDisplay.SelectionCellLabelFontFamily = 'Arial'
ofoamDisplay.SelectionCellLabelFontFile = ''
ofoamDisplay.SelectionCellLabelFontSize = 18
ofoamDisplay.SelectionCellLabelItalic = 0
ofoamDisplay.SelectionCellLabelJustification = 'Left'
ofoamDisplay.SelectionCellLabelOpacity = 1.0
ofoamDisplay.SelectionCellLabelShadow = 0
ofoamDisplay.SelectionPointLabelBold = 0
ofoamDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
ofoamDisplay.SelectionPointLabelFontFamily = 'Arial'
ofoamDisplay.SelectionPointLabelFontFile = ''
ofoamDisplay.SelectionPointLabelFontSize = 18
ofoamDisplay.SelectionPointLabelItalic = 0
ofoamDisplay.SelectionPointLabelJustification = 'Left'
ofoamDisplay.SelectionPointLabelOpacity = 1.0
ofoamDisplay.SelectionPointLabelShadow = 0
ofoamDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
ofoamDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
ofoamDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
ofoamDisplay.GlyphType.TipResolution = 6
ofoamDisplay.GlyphType.TipRadius = 0.1
ofoamDisplay.GlyphType.TipLength = 0.35
ofoamDisplay.GlyphType.ShaftResolution = 6
ofoamDisplay.GlyphType.ShaftRadius = 0.03
ofoamDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
ofoamDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
ofoamDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
ofoamDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
ofoamDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
ofoamDisplay.DataAxesGrid.XTitle = 'X Axis'
ofoamDisplay.DataAxesGrid.YTitle = 'Y Axis'
ofoamDisplay.DataAxesGrid.ZTitle = 'Z Axis'
ofoamDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
ofoamDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
ofoamDisplay.DataAxesGrid.XTitleFontFile = ''
ofoamDisplay.DataAxesGrid.XTitleBold = 0
ofoamDisplay.DataAxesGrid.XTitleItalic = 0
ofoamDisplay.DataAxesGrid.XTitleFontSize = 12
ofoamDisplay.DataAxesGrid.XTitleShadow = 0
ofoamDisplay.DataAxesGrid.XTitleOpacity = 1.0
ofoamDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
ofoamDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
ofoamDisplay.DataAxesGrid.YTitleFontFile = ''
ofoamDisplay.DataAxesGrid.YTitleBold = 0
ofoamDisplay.DataAxesGrid.YTitleItalic = 0
ofoamDisplay.DataAxesGrid.YTitleFontSize = 12
ofoamDisplay.DataAxesGrid.YTitleShadow = 0
ofoamDisplay.DataAxesGrid.YTitleOpacity = 1.0
ofoamDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
ofoamDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
ofoamDisplay.DataAxesGrid.ZTitleFontFile = ''
ofoamDisplay.DataAxesGrid.ZTitleBold = 0
ofoamDisplay.DataAxesGrid.ZTitleItalic = 0
ofoamDisplay.DataAxesGrid.ZTitleFontSize = 12
ofoamDisplay.DataAxesGrid.ZTitleShadow = 0
ofoamDisplay.DataAxesGrid.ZTitleOpacity = 1.0
ofoamDisplay.DataAxesGrid.FacesToRender = 63
ofoamDisplay.DataAxesGrid.CullBackface = 0
ofoamDisplay.DataAxesGrid.CullFrontface = 1
ofoamDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
ofoamDisplay.DataAxesGrid.ShowGrid = 0
ofoamDisplay.DataAxesGrid.ShowEdges = 1
ofoamDisplay.DataAxesGrid.ShowTicks = 1
ofoamDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
ofoamDisplay.DataAxesGrid.AxesToLabel = 63
ofoamDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
ofoamDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
ofoamDisplay.DataAxesGrid.XLabelFontFile = ''
ofoamDisplay.DataAxesGrid.XLabelBold = 0
ofoamDisplay.DataAxesGrid.XLabelItalic = 0
ofoamDisplay.DataAxesGrid.XLabelFontSize = 12
ofoamDisplay.DataAxesGrid.XLabelShadow = 0
ofoamDisplay.DataAxesGrid.XLabelOpacity = 1.0
ofoamDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
ofoamDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
ofoamDisplay.DataAxesGrid.YLabelFontFile = ''
ofoamDisplay.DataAxesGrid.YLabelBold = 0
ofoamDisplay.DataAxesGrid.YLabelItalic = 0
ofoamDisplay.DataAxesGrid.YLabelFontSize = 12
ofoamDisplay.DataAxesGrid.YLabelShadow = 0
ofoamDisplay.DataAxesGrid.YLabelOpacity = 1.0
ofoamDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
ofoamDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
ofoamDisplay.DataAxesGrid.ZLabelFontFile = ''
ofoamDisplay.DataAxesGrid.ZLabelBold = 0
ofoamDisplay.DataAxesGrid.ZLabelItalic = 0
ofoamDisplay.DataAxesGrid.ZLabelFontSize = 12
ofoamDisplay.DataAxesGrid.ZLabelShadow = 0
ofoamDisplay.DataAxesGrid.ZLabelOpacity = 1.0
ofoamDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
ofoamDisplay.DataAxesGrid.XAxisPrecision = 2
ofoamDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
ofoamDisplay.DataAxesGrid.XAxisLabels = []
ofoamDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
ofoamDisplay.DataAxesGrid.YAxisPrecision = 2
ofoamDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
ofoamDisplay.DataAxesGrid.YAxisLabels = []
ofoamDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
ofoamDisplay.DataAxesGrid.ZAxisPrecision = 2
ofoamDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
ofoamDisplay.DataAxesGrid.ZAxisLabels = []
ofoamDisplay.DataAxesGrid.UseCustomBounds = 0
ofoamDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
ofoamDisplay.PolarAxes.Visibility = 0
ofoamDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
ofoamDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
ofoamDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
ofoamDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
ofoamDisplay.PolarAxes.EnableCustomRange = 0
ofoamDisplay.PolarAxes.CustomRange = [0.0, 1.0]
ofoamDisplay.PolarAxes.PolarAxisVisibility = 1
ofoamDisplay.PolarAxes.RadialAxesVisibility = 1
ofoamDisplay.PolarAxes.DrawRadialGridlines = 1
ofoamDisplay.PolarAxes.PolarArcsVisibility = 1
ofoamDisplay.PolarAxes.DrawPolarArcsGridlines = 1
ofoamDisplay.PolarAxes.NumberOfRadialAxes = 0
ofoamDisplay.PolarAxes.AutoSubdividePolarAxis = 1
ofoamDisplay.PolarAxes.NumberOfPolarAxis = 0
ofoamDisplay.PolarAxes.MinimumRadius = 0.0
ofoamDisplay.PolarAxes.MinimumAngle = 0.0
ofoamDisplay.PolarAxes.MaximumAngle = 90.0
ofoamDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
ofoamDisplay.PolarAxes.Ratio = 1.0
ofoamDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.PolarAxisTitleVisibility = 1
ofoamDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
ofoamDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
ofoamDisplay.PolarAxes.PolarLabelVisibility = 1
ofoamDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
ofoamDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
ofoamDisplay.PolarAxes.RadialLabelVisibility = 1
ofoamDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
ofoamDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
ofoamDisplay.PolarAxes.RadialUnitsVisibility = 1
ofoamDisplay.PolarAxes.ScreenSize = 10.0
ofoamDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
ofoamDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
ofoamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
ofoamDisplay.PolarAxes.PolarAxisTitleBold = 0
ofoamDisplay.PolarAxes.PolarAxisTitleItalic = 0
ofoamDisplay.PolarAxes.PolarAxisTitleShadow = 0
ofoamDisplay.PolarAxes.PolarAxisTitleFontSize = 12
ofoamDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
ofoamDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
ofoamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
ofoamDisplay.PolarAxes.PolarAxisLabelBold = 0
ofoamDisplay.PolarAxes.PolarAxisLabelItalic = 0
ofoamDisplay.PolarAxes.PolarAxisLabelShadow = 0
ofoamDisplay.PolarAxes.PolarAxisLabelFontSize = 12
ofoamDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
ofoamDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
ofoamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
ofoamDisplay.PolarAxes.LastRadialAxisTextBold = 0
ofoamDisplay.PolarAxes.LastRadialAxisTextItalic = 0
ofoamDisplay.PolarAxes.LastRadialAxisTextShadow = 0
ofoamDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
ofoamDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
ofoamDisplay.PolarAxes.EnableDistanceLOD = 1
ofoamDisplay.PolarAxes.DistanceLODThreshold = 0.7
ofoamDisplay.PolarAxes.EnableViewAngleLOD = 1
ofoamDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
ofoamDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
ofoamDisplay.PolarAxes.PolarTicksVisibility = 1
ofoamDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
ofoamDisplay.PolarAxes.TickLocation = 'Both'
ofoamDisplay.PolarAxes.AxisTickVisibility = 1
ofoamDisplay.PolarAxes.AxisMinorTickVisibility = 0
ofoamDisplay.PolarAxes.ArcTickVisibility = 1
ofoamDisplay.PolarAxes.ArcMinorTickVisibility = 0
ofoamDisplay.PolarAxes.DeltaAngleMajor = 10.0
ofoamDisplay.PolarAxes.DeltaAngleMinor = 5.0
ofoamDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
ofoamDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
ofoamDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
ofoamDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
ofoamDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
ofoamDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
ofoamDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
ofoamDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
ofoamDisplay.PolarAxes.ArcMajorTickSize = 0.0
ofoamDisplay.PolarAxes.ArcTickRatioSize = 0.3
ofoamDisplay.PolarAxes.ArcMajorTickThickness = 1.0
ofoamDisplay.PolarAxes.ArcTickRatioThickness = 0.5
ofoamDisplay.PolarAxes.Use2DMode = 0
ofoamDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(ofoamDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
ofoamDisplay.SetScalarBarVisibility(renderView1, False)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.ShowCategoricalColorsinDataRangeOnly = 0
vtkBlockColorsLUT.RescaleOnVisibilityChange = 0
vtkBlockColorsLUT.EnableOpacityMapping = 0
vtkBlockColorsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
vtkBlockColorsLUT.UseLogScale = 0
vtkBlockColorsLUT.ColorSpace = 'Diverging'
vtkBlockColorsLUT.UseBelowRangeColor = 0
vtkBlockColorsLUT.BelowRangeColor = [0.0, 0.0, 0.0]
vtkBlockColorsLUT.UseAboveRangeColor = 0
vtkBlockColorsLUT.AboveRangeColor = [0.5, 0.5, 0.5]
vtkBlockColorsLUT.NanColor = [1.0, 1.0, 0.0]
vtkBlockColorsLUT.NanOpacity = 1.0
vtkBlockColorsLUT.Discretize = 1
vtkBlockColorsLUT.NumberOfTableValues = 256
vtkBlockColorsLUT.ScalarRangeInitialized = 0.0
vtkBlockColorsLUT.HSVWrap = 0
vtkBlockColorsLUT.VectorComponent = 0
vtkBlockColorsLUT.VectorMode = 'Magnitude'
vtkBlockColorsLUT.AllowDuplicateScalars = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]
vtkBlockColorsLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')
vtkBlockColorsPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
vtkBlockColorsPWF.AllowDuplicateScalars = 1
vtkBlockColorsPWF.UseLogScale = 0
vtkBlockColorsPWF.ScalarRangeInitialized = 0

# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.ShowCategoricalColorsinDataRangeOnly = 0
vtkBlockColorsLUT.RescaleOnVisibilityChange = 0
vtkBlockColorsLUT.EnableOpacityMapping = 0
vtkBlockColorsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
vtkBlockColorsLUT.UseLogScale = 0
vtkBlockColorsLUT.ColorSpace = 'Diverging'
vtkBlockColorsLUT.UseBelowRangeColor = 0
vtkBlockColorsLUT.BelowRangeColor = [0.0, 0.0, 0.0]
vtkBlockColorsLUT.UseAboveRangeColor = 0
vtkBlockColorsLUT.AboveRangeColor = [0.5, 0.5, 0.5]
vtkBlockColorsLUT.NanColor = [1.0, 1.0, 0.0]
vtkBlockColorsLUT.NanOpacity = 1.0
vtkBlockColorsLUT.Discretize = 1
vtkBlockColorsLUT.NumberOfTableValues = 256
vtkBlockColorsLUT.ScalarRangeInitialized = 0.0
vtkBlockColorsLUT.HSVWrap = 0
vtkBlockColorsLUT.VectorComponent = 0
vtkBlockColorsLUT.VectorMode = 'Magnitude'
vtkBlockColorsLUT.AllowDuplicateScalars = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '11']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.6666666666666666, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5019607843137255, 0.7490196078431373, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]
vtkBlockColorsLUT.IndexedOpacities = [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.5019607843137255, 0.7490196078431373, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5019607843137255, 0.7490196078431373, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')
vtkBlockColorsPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
vtkBlockColorsPWF.AllowDuplicateScalars = 1
vtkBlockColorsPWF.UseLogScale = 0
vtkBlockColorsPWF.ScalarRangeInitialized = 0

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5019607843137255, 0.7490196078431373, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5019607843137255, 0.7490196078431373, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 0.0, 1.0, 1.0, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5019607843137255, 0.7490196078431373, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 0.6299992370489051, 0.6299992370489051, 1.0, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5019607843137255, 0.7490196078431373, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]

# Properties modified on vtkBlockColorsLUT
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 1.0, 0.5019607843137255, 0.7490196078431373, 0.6699931334401464, 0.5000076295109483, 0.3300068665598535, 1.0, 0.5019607843137255, 0.7490196078431373, 0.5300068665598535, 0.3499961852445258, 0.7000076295109483, 1.0, 0.7499961852445258, 0.5000076295109483]

# get active source.
ofoam = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1555, 831]

# get display properties
ofoamDisplay = GetDisplayProperties(ofoam, view=renderView1)

# hide color bar/color legend
ofoamDisplay.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.18712266413592632, 0.23966517350258076, 0.5543861540096434]
renderView1.CameraFocalPoint = [0.7873017993077217, -0.09013925022119454, -0.32177439064104096]
renderView1.CameraViewUp = [0.17467469052540907, 0.9697073687855915, -0.17075236868862878]
renderView1.CameraParallelScale = 0.28903675718625726

# save screenshot
SaveScreenshot(''+str(sys.argv[2])+'', renderView1, ImageResolution=[3110, 1136],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=1, 
    # TIFF options
    Compression='PackBits')