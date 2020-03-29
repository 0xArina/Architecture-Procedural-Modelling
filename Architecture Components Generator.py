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
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475, height=40)

cmds.columnLayout()
cmds.button(label="Create Straight Stairs", command=('straightStairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#              UI: adjust and create Spiral Stairs              #
#################################################################
cmds.frameLayout(collapsable=True, label="Spiral Stairs")

cmds.columnLayout()
cmds.radioButtonGrp('spiralStairsHeight', label="Staircase Height", labelArray3=["2.4 m", "2.8 m", "3.2 m"], numberOfRadioButtons=3, sl=1)

cmds.columnLayout()
cmds.button(label="Create Spiral Stairs", command=('spiralStairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#            UI: adjust and create L-shaped Stairs              #
#################################################################
cmds.frameLayout(collapsable=True, label="L-shaped Stairs")

cmds.columnLayout()
cmds.button(label="Create L-shaped Stairs", command=('Lstairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#            UI: adjust and create U-shaped Stairs              #
#################################################################
cmds.frameLayout(collapsable=True, label="U-shaped Stairs")

cmds.columnLayout()
cmds.button(label="Create U-shaped Stairs", command=('Ustairs()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#         UI: adjust and create Roman Tuscan column             #
#################################################################
cmds.frameLayout(collapsable=True, label="Roman Tuscan column")

cmds.columnLayout()
cmds.button(label="Create Roman Tuscan column", command=('RTcolumn()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#          UI: adjust and create Greek Doric column             #
#################################################################
cmds.frameLayout(collapsable=True, label="Greek Doric column")

cmds.columnLayout()
cmds.button(label="Create Greek Doric column", command=('GDcolumn()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#          UI: adjust and create Greek Ionic column             #
#################################################################
cmds.frameLayout(collapsable=True, label="Greek Ionic column")

cmds.columnLayout()
cmds.button(label="Create Greek Ionic column", command=('GIcolumn()'))

# Level Up in Hierarchy
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

#     UI: adjust and create walls with window/door frames       #
#################################################################
cmds.frameLayout(collapsable=True, label="Walls with window/door frames")

cmds.columnLayout()
cmds.button(label="Create Walls with window/door frames", command=('walls()'))

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
    
    # step count
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
        cmds.polyCylinder (r = 0.05, h = 6)
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
    # query user input values
    stairsHeight = cmds.radioButtonGrp('spiralStairsHeight', q=True, sl=True)
     
    # define needed variables   "2.4 m", "2.8 m", "3.2 m"
    if(stairsHeight == 1):
        cylindHeight = 20
    if(stairsHeight == 2):
        cylindHeight = 28
    if(stairsHeight == 3):
        cylindHeight = 32
    # staircaseHeight 
    # staircaseDiameter 
   # lengthBtwSteps
   # stepThickness
    
    # base
    cmds.polyCylinder(r = 2, h = cylindHeight)
    # move it up
    cmds.move(10, moveY=True)
    # step count 
    for i in range(10):
        # stair
        cmds.polyCube(w = 5, d = 2, h = 0.5)
        # move it on X axis 
        cmds.move(3, moveX=True)
        # move it on Y axis 
        cmds.move(i*2, moveY=True)
        # move rotation pivot and set world-space transformation
        cmds.xform( ws = True, rotatePivot = (0, 0, 0))
        # rotate on Y axis
        cmds.rotate(i * 15, rotateY=True)

#################################################################
#                   L-SHAPED STAIRS FUNCTION                    #  
#################################################################


#################################################################
#                   U-SHAPED STAIRS FUNCTION                    #  
#################################################################


#################################################################
#                  ROMAN TUSCAN COLUMN FUNCTION                 #  
#################################################################


#################################################################
#                   GREEK DORIC COLUMN FUNCTION                 #  
#################################################################


#################################################################
#                  GREEK IONIC COLUMN FUNCTION                  #  
#################################################################


#################################################################
#                     WALLS/WINDOWS FUNCTION                    #  
#################################################################
def walls():
    # base
    cmds.polyCube(w = 40, d = 1.5, h = 20)
    # move it up
    cmds.move(10, moveY=True)