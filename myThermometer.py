from vpython import*
import numpy as np
glassBulb=sphere(radius=1.25,color=color.white,opacity=.5)
glassCy1=cylinder(radius=.65,length=6,color=color.white,opacity=.3)
mercSphere=sphere(radius=1,color=color.red)
merColumn=cylinder(radius=.45,length=6,color=color.red)
for tick in np.linspace(1,6,25):
    box(size=vector(.05,.5,.25),color=color.white,pos=vector(tick,0,.5))
while True:
    for myTemp in np.linspce(1,6,100):
        rate(25)
        merColumn.length=myTemp
    for myTemp in np.linspce(6,1,100):
        rate(25)
        merColumn.length=myTemp

