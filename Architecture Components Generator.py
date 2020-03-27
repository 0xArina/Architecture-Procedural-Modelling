import maya.cmds as cmds
import random as rnd

if 'myWin' in globals():
    if cmds.window(myWin, exists=True):
        cmds.deleteUI(myWin, window=True)

# Window Title       
myWin = cmds.window(title="Architecture Components", menuBar=True)

# Collapsible Menu with options to create New Scene and Delete Selected
cmds.menu(label="Basic Options")
cmds.menuItem(label="New Scene", command=('cmds.file(new=True, force=True)'))
cmds.menuItem(label="Delete Selected", command=('cmds.delete()'))

#            UI: adjust and create Straight Stairs              #
#################################################################
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('straightStairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

# Show UI window
cmds.showWindow( myWin )

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################
def straightStairs():
    # query values from UI sliders
    
    # define stairs size
    stairSizeX = 8.0
    stairSizeY = 1.0
    stairSizeZ = 2.0
    
    # name
    nsTmp = "StraightStairs" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    # quantity of stairs
    for i in range (8):
        # create a stair
        cmds.polyCube(d = stairSizeZ, h = stairSizeY, w = stairSizeX)
        # move it on Z axis
        cmds.move(-i*stairSizeZ, moveZ=True)
        # move it on Y axis
        cmds.move(i*stairSizeY, moveY=True)
    
    # unite stairs
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False) 
    # move them up
    cmds.move(stairSizeY/2.0, moveY=True)    
       
        
    # create Left side poles
    for i in range (8):
        cmds.polyCylinder (r = .05, h = 6)
        # move it up
        cmds.move(3 + i*stairSizeY, moveY=True)
        # move it to the left
        cmds.move(-stairSizeX/2.0 + 0.4, moveX=True)
        # move it into depth
        cmds.move(-i *stairSizeZ, moveZ=True)