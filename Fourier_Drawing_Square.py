#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#****************************** Started Sept 2021 ******************************
#**************************** Last Updated Aug 2022 ****************************
#*******************************************************************************
from vpython import *
import numpy as np
import cmath as cm

#---------------------- Scene Information -----------------------
scene = canvas()
scene.range = 400
scene.height = 900
scene.width = 1900
scene.fov = pi/6
scene.userspin = 0

#---------------------- Changable Info -----------------------
Num_of_Arrows = 100

#---------------------- Display Drawing -----------------------
Drawing = curve( color = color.gray(0.2) )
Z = []
PointFile = open("Square.txt", "r")
for L in PointFile:
    v = L.split(",")
    x = float(v[0])
    y = -float(v[1])
    Drawing.append( vector(x,y,0) )
    Z.append( complex(x,y) )

PointFile.close()
Drawer = curve( color = color.cyan , radius = 3 )

#-------------------- Fourier Transform -----------------------
Coefficients = []

N = Num_of_Arrows
if N % 2 == 0:
    FrequencyArray = np.arange( -N/2 , N/2 , 1 )
else:
    FrequencyArray = np.arange( -(N-1)/2 , (N-1)/2 + 1 , 1 )

PointArray = np.arange( 0 , Drawing.npoints , 1 )
for f in FrequencyArray:
    ZT = 0
    for ele in PointArray:
        ZT += Z[ele] * cm.exp( -1j * 2*pi * f * ele / N )
    Coefficients.append( [ abs(ZT)/N , f , cm.phase(ZT) ] )

Coefficients = sorted(Coefficients, key=lambda x: x[0], reverse=True)

#---------------------- Display Arrows -----------------------
FourierArrows = []
for ele in np.arange( 0 , N , 1 ):
    ThisArrow = arrow( visible = 1 )
    if ele == 0:
        ThisArrow.pos = vector(0,0,0)
    else:
        ThisArrow.pos = PreviousArrow.pos + PreviousArrow.axis
    ThisArrow.axis = rotate( Coefficients[ele][0] * vector(1,0,0) ,
                             angle = Coefficients[ele][2] ,
                             axis = vector(0,0,1) )
    ThisArrow.f = Coefficients[ele][1]
    FourierArrows.append( ThisArrow )
    PreviousArrow = ThisArrow

#---------------------- Display Orbits -----------------------
FourierOrbits = []
for ele in np.arange( 0 , N , 1 ):
    CirclePoints = []
    R = mag( FourierArrows[ele].axis )
    for Theta in np.linspace( 0 , 2*pi , 100 ):
        x = R * cos(Theta)
        y = R * sin(Theta)
        CirclePoints.append( vector(x,y,0) )
    ThisOrbit = curve( pos = CirclePoints , origin = FourierArrows[ele].pos ,
                       visible = 1 )
    FourierOrbits.append( ThisOrbit )

#---------------------- Rotate Arrows -----------------------
scene.waitfor('click')
dt = 0.0001
while 1:
    rate(500)
    #scene.capture("Square")
    ele = 0
    for ThisArrow in FourierArrows:
        ThisArrow.rotate( angle = 2*pi * ThisArrow.f * dt,
                          axis = vector(0,0,1),
                          origin = ThisArrow.pos)
        if ele == 0:
            ThisArrow.pos = vector(0,0,0)
        else:
            ThisArrow.pos = PreviousArrow.pos + PreviousArrow.axis
        FourierOrbits[ele].origin = ThisArrow.pos
        PreviousArrow = ThisArrow
        ele += 1
    DrawerPoint = FourierArrows[N-1].pos + FourierArrows[N-1].axis
    Drawer.append( DrawerPoint )
