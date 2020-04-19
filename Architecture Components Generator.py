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
cmds.frameLayout(collapsable=True, label="Straight Stairs", width=475)

cmds.columnLayout()
cmds.radioButtonGrp('straightStairsHeight', label="Staircase Height", labelArray3=["2 m", "2.4 m", "2.8 m"], numberOfRadioButtons=3, sl=2)
cmds.intSliderGrp('straightStairsWidth', l="Staircase Width", f=True, min=1, max=6, value=3)
cmds.radioButtonGrp('straightStairsHR', label="Add Handrails?", labelArray2=["yes", "no"], numberOfRadioButtons=2, sl=1)

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
cmds.radioButtonGrp('spiralStairsHeight', label="Staircase Height", labelArray3=["2 m", "2.4 m", "2.8 m"], numberOfRadioButtons=3, sl=2)
cmds.radioButtonGrp('spiralStaircaseDiameter', label="Staircase Diameter", labelArray3=["140 m", "160 m", "180 m"], numberOfRadioButtons=3, sl=1)
cmds.intSliderGrp('stepHeight', l="Step Thickness", f=True, min=1, max=6, value=3)
cmds.colorSliderGrp('spiralColour', label="Colour", hsv=(120, 1, 1))

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
cmds.radioButtonGrp('wallHeight', label="Wall Height", labelArray3=["2 m", "2.4 m", "2.8 m"], numberOfRadioButtons=3, sl=2)
cmds.radioButtonGrp('windowHeight', label="Window Height", labelArray3=["0.5 m", "1 m", "1.5 m"], numberOfRadioButtons=3, sl=2)
cmds.intSliderGrp('windows', l="Number of Window frames", f=True, min=0, max=2, value=2)
cmds.radioButtonGrp('addDoor', label="Add a Door frame?", labelArray2=["yes", "no"], numberOfRadioButtons=2, sl=1)
cmds.colorSliderGrp('wallColour', label="Colour", hsv=(63, 0.5, 1))

cmds.columnLayout()
cmds.button(label="Create Walls with window/door frames", command=('walls()'))

# Level Up in Hierarchy


# Show UI window
cmds.showWindow( myWin )

#################################################################
#                   STRAIGHT STAIRS FUNCTION                    #  
#################################################################
def straightStairs():
    # query user input values
    staircaseHeight = cmds.radioButtonGrp('straightStairsHeight', q=True, sl=True)
    staircaseWidth = cmds.intSliderGrp('straightStairsWidth', q=True, v=True)
    createHandrails = cmds.radioButtonGrp('straightStairsHR', q=True, sl=True)
    
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
    for i in range (24):
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
       
    # create handrails
    if(createHandrails == 1): 
   
        # handrail poles Left
        for i in range (8):
            # create Left side poles
            cmds.polyCylinder (r = 0.05, h = 6)
            # move it up
            cmds.move(3 + i*stairSizeY, moveY=True)
            # move it to the left
            cmds.move(-stairSizeX/2.0 + 0.4, moveX=True)
            # move it into depth
            cmds.move(-i *stairSizeZ, moveZ=True)
            
        # handrail poles Right
        for i in range (8):
            # create Left side poles
            cmds.polyCylinder (r = 0.05, h = 6)
            # move it up
            cmds.move(3 + i*stairSizeY, moveY=True)
            # move it to the Right
            cmds.move(stairSizeX/2.0 - 0.4, moveX=True)
            # move it into depth
            cmds.move(-i *stairSizeZ, moveZ=True)
        
            
        # handrail upper part 
        # length^2 = a^2 + b^2
        
        
        #LEFT
        cmds.polyCube( sx=1, sy=1, sz=1, h=.2, w=.5, d=17)
        
        cmds.rotate(27, 0, 0)
        
        cmds.move(-3.557, 9.576, -6.858)
        
        # RIGHT
        cmds.polyCube( sx=1, sy=1, sz=1, h=.2, w=.5, d=17)
        
        cmds.rotate(27, 0, 0)
        
        cmds.move(3.557, 9.576, -6.858)
    
#################################################################
#                     SPIRAL STAIRS FUNCTION                    #  
#################################################################
def spiralStairs():
    # query user input values
    staircaseHeight = cmds.radioButtonGrp('spiralStairsHeight', q=True, sl=True)
    staircaseDiameter = cmds.radioButtonGrp('spiralStaircaseDiameter', q=True, sl=True)
    stepThickness = cmds.intSliderGrp('stepHeight', q=True, v=True)
    rgb = cmds.colorSliderGrp('spiralColour', q=True, rgbValue=True)
     
    # define variables   
    stepHeight = stepThickness * 0.3
    
    if(staircaseHeight == 1):
        cylindHeight = 16 # 2 m 
        stepCount = 8
    if(staircaseHeight == 2):
        cylindHeight = 20 # 2.4 m
        stepCount = 10
    if(staircaseHeight == 3):
        cylindHeight = 24 # 2.8 m
        stepCount = 12
    
    if(staircaseDiameter == 1):
        stairWidth = 5    # 140 m
    if(staircaseDiameter == 2):
        stairWidth = 7.2    # 160 m
    if(staircaseDiameter == 3):
        stairWidth = 9.4    # 180m
    
    # create base
    cmds.polyCylinder(r = 2, h = cylindHeight)
    
    # move it up
    cmds.move(cylindHeight/2, moveY=True)
    
    # add colour      
    

    # step count 
    for i in range(stepCount):
        # stair
        cmds.polyCube(w = stairWidth, d = 2, h = stepHeight)
        # move it on X axis 
        cmds.move(3, moveX=True)
        # move it on Y axis 
        cmds.move(i*2 + stepHeight/2, moveY=True)
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
    # query user input values
    wallHeight = cmds.radioButtonGrp('wallHeight', q=True, sl=True)
    windowHeight = cmds.radioButtonGrp('windowHeight', q=True, sl=True)
    doorFrame = cmds.radioButtonGrp('addDoor', q=True, sl=True)
    windowFrame = cmds.intSliderGrp('windows', q=True, v=True)
    rgb = cmds.colorSliderGrp('wallColour', q=True, rgbValue=True)
    
    # name
    nsTmp = "Wall" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    # define variables
    if(wallHeight  == 1):
        wallSizeY = 16
        doorSizeY = 11
        moveY = 8
        moveDoorY = 5.5
        move2obj = 12
    if(wallHeight  == 2):
        wallSizeY = 20
        doorSizeY = 15
        moveY = 10
        moveDoorY = 7.5
        move2obj = 16
    if(wallHeight  == 3):
        wallSizeY = 24
        doorSizeY = 19
        moveY = 12
        moveDoorY = 9.5
        move2obj = 20
    
    if(windowHeight == 1):
        windowSizeY = 3
        moveWindowY = windowSizeY/2 + wallSizeY/2 + 3
    if(windowHeight == 2):
        windowSizeY = 8
        moveWindowY = windowSizeY/2 + wallSizeY/2 - 3
    if(windowHeight == 3):
        windowSizeY = 12
        moveWindowY = windowSizeY/2 + wallSizeY/2  - 6
    
    # base
    wall = cmds.polyCube(w = 40, d = 1.5, h = wallSizeY)
    # move it up
    cmds.move(moveY, moveY=True)
   
    # add door frame
    if(doorFrame == 1):
        door = cmds.polyCube(w = 10, d = 1.5, h = doorSizeY)
        # move it up
        cmds.move(moveDoorY, moveY=True)
        # remove door frame from the wall
        wall = cmds.polyCBoolOp(wall, door, op=2)
    
    # add window frames 
    if(windowFrame == 1):
        window1 = cmds.polyCube(w = 7, d = 1.5, h = windowSizeY)
        # move it up
        cmds.move(moveWindowY , moveY=True)
        # move it left
        cmds.move(-12, moveX=True)
        # remove door frame from the wall
        wall = cmds.polyCBoolOp(wall, window1, op=2)
    if(windowFrame == 2):
        window1 = cmds.polyCube(w = 7, d = 1.5, h = windowSizeY)
        # move it up
        cmds.move(moveWindowY , moveY=True)
        # move it left
        cmds.move(-12, moveX=True)
        # remove door frame from the wall
        wall = cmds.polyCBoolOp(wall, window1, op=2)
        
        window2 = cmds.polyCube(w = 7, d = 1.5, h = windowSizeY)
        # move it up
        cmds.move(moveWindowY , moveY=True)
        # move it right
        cmds.move(12, moveX=True)
        # remove door frame from the wall
        wall = cmds.polyCBoolOp(wall, window2, op=2)
        
    # add material        
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], type='double3')
    
    add2Obj = cmds.polyCube(w = 1, d = 1.5, h = 1)
    cmds.move(move2obj, moveY=True)
    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(nsTmp+":blckMat"))  
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)