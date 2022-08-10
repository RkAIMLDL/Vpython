from vpython import*
myOrb=sphere(radius=1,color=color.white)
rChan=0
gChan=0
bChan=0
rInc=.001
gInc=.002
bInc=.0015
while True:
    rChan=rChan+rInc
    gChan=gChan+gInc
    bChan=bChan+bInc
    myOrb.color=vector(rChan,gChan,bChan)
    if rChan>=1 or rChan<=0:
        rChan=rChan*(-1)
    if gChan>=1 or gChan<=0:
        gChan=gChan*(-1)
    if bChan>=1 or bChan<=0:
        bChan=bChan*(-1)