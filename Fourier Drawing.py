#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#********************************** Sept 2021 **********************************
#*******************************************************************************
from vpython import *
import numpy as np
import cmath as cm

#---------------------- Scene Information -----------------------
scene = canvas()
scene.range = 1200
scene.height = 1080
scene.width = 1920
scene.fov = pi/6
scene.userspin = 0

#---------------------- Changable Info -----------------------
Num_of_Arrows = 500

#---------------------- Display Drawing -----------------------
Drawer = curve( color=color.cyan )
Drawing = curve()
Z = []

#Creates a list of points from a mathematical function
ThetaSet = np.linspace( 0 , 6*pi , 100 )
for Theta in ThetaSet:
    #Defines a Cardioid
    #x = 2 * ( 1 - cos(Theta) ) * cos(Theta)
    #y = 2 * ( 1 - cos(Theta) ) * sin(Theta)
    #Defines a Cyclocycloid
    r1 = -3
    r2 = 5
    d = 5
    x = ( r1 + r2 ) * cos(Theta) - d * cos( ( r1 + r2 ) / r1 * Theta )
    y = ( r1 + r2 ) * sin(Theta) - d * sin( ( r1 + r2 ) / r1 * Theta )
    #Adds point the shape we intend to draw
    Drawing.append( vector(x,y,0) )
    Z.append( complex(x,y) )

#Pulls image points from a file
"""
PointFile = open("ScienceAsylum.txt", "r")
for L in PointFile:
    v = L.split(",")
    x = float(v[0])
    y = -float(v[1])
    Drawing.append( vector(x,y,0) )
    Z.append( complex(x,y) )
PointFile.close()
"""

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
    ThisArrow = arrow()
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

#---------------------- Rotate Arrows -----------------------
dt = 0.0001
while 1:
    rate(500)
    ele = 0
    for ThisArrow in FourierArrows:
        ThisArrow.rotate( angle = 2*pi * ThisArrow.f * dt,
                          axis = vector(0,0,1),
                          origin = ThisArrow.pos)
        if ele == 0:
            ThisArrow.pos = vector(0,0,0)
        else:
            ThisArrow.pos = PreviousArrow.pos + PreviousArrow.axis
        PreviousArrow = ThisArrow
        ele += 1
    Drawer.append( ThisArrow.pos + ThisArrow.axis )

