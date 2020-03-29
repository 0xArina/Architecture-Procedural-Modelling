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

#              UI: adjust and create Spiral Stairs              #
#################################################################
cmds.frameLayout(collapsable=True, label="Spiral Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Spiral Stairs", command=('spiralStairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#            UI: adjust and create L-shaped Stairs              #
#################################################################
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('Lstairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#            UI: adjust and create U-shaped Stairs              #
#################################################################
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('Ustairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#         UI: adjust and create Roman Tuscan column             #
#################################################################
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('RTcolumn()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#          UI: adjust and create Greek Doric column             #
#################################################################
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('GDcolumn()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#          UI: adjust and create Greek Ionic column             #
#################################################################
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('GIcolumn()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#     UI: adjust and create walls with window/door frames       #
#################################################################
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=140)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('straightStairs()'))

# Level Up in Hierarchy


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
    
    # staircase
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
       
        
    # handrail poles
    for i in range (8):
        # create Left side poles
        cmds.polyCylinder (r = .05, h = 6)
        # move it up
        cmds.move(3 + i*stairSizeY, moveY=True)
        # move it to the left
        cmds.move(-stairSizeX/2.0 + 0.4, moveX=True)
        # move it into depth
        cmds.move(-i *stairSizeZ, moveZ=True)
        
    # handrail upper part
    # length^2 = a^2 + b^2
    
    cmds.polyCube( sx=1, sy=1, sz=1, h=.2, w=.5, d=17)
    
    cmds.rotate(27, 0, 0)
    
#################################################################
#                     SPIRAL STAIRS FUNCTION                    #  
#################################################################
def spiralStairs():
    
    # base
    cmds.polyCylinder(r =2, h= 20)
    for i in range(7):
        # steps
        cmds.polyCube(w = 5, d = 2, h = 0.5)
        cmds.move(3 * i, moveY=True)

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################