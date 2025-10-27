import maya.cmds as cmds

def cleanup_selected_asset():
    """Resets transformations and centers the Pivot for the SELECTED object."""
    
    # 1. We receive a list of selected objects

    selection = cmds.ls(selection=True)
    
    if not selection:
        # We check that there is at least something, otherwise we display an error message.
        print("❌ TA error: No objects are selected. Select an asset to clean.")
        return

    # Take the first highlighted item from the list
    object_name = selection[0] 
    
    # 2. Cleaning
    cmds.makeIdentity(object_name, apply=True, t=1, r=1, s=1)
    cmds.xform(object_name, centerPivots=True)
    
    print(f"🎉 QA PASS: Объект {object_name} Ready for export!")

cleanup_selected_asset()
