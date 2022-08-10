from vpython import*
myCylOrange=cylinder(radius=1,color=color.red,length=6)
myCylCyan=cylinder(radius=1,legth=6,color=color.cyan,pos=vector(0,3,0))
myCylOrangeLength=1
myCylCyanLength=1
myCylOrangeDelta=.01
myCylCyanDelta=.02
while True:
    rate(5)
    myCylOrangeLength=myCylOrangeLength+myCylOrangeDelta
    myCylCyanLength=myCylCyanLength+myCylCyanDelta
    myCylOrange.length=myCylOrangeLength
    myCylOrange.length=myCylCyanLength
    if myCylOrangeLength>=6 or myCylOrangeLength<=.1:
        myCylOrangeDelta=myCylOrangeDelta*(-1)
        myCylCyanDelta=myCylCyanDelta*(-1)
    