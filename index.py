import maya.cmds as cmds

# Function for automatic creation and renaming
def create_and_rename_assets():
    
    # This is a scene reset. Remove if you need to keep other objects.
    cmds.select(all=True)
    cmds.delete()
    
    for i in range(1, 11): 
        # Format the name: SM_Cube_01, SM_Cube_02...
        asset_name = f"SM_Cube_{i:02d}" 
        
        # Create a cube with a new name, [0] takes the name of the object, ignoring the shape node
        new_cube = cmds.polyCube(name=asset_name)[0]
        
        # To see all the cubes, move them to the side.
        cmds.move(i * 2, 0, 0, new_cube) 
        
        print(f"Asset created: {new_cube}")

# Call the function
create_and_rename_assets()
