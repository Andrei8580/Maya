
                                 !!!Only for the first selected object!!!


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






                                    !!!For all selected!!!


import maya.cmds as cmds

def cleanup_selected_asset():
    """Resets transformations and centers the Pivot for ALL selected objects."""
    
    selection = cmds.ls(selection=True, type='transform') # Let's make sure that the transform nodes are selected.
    
    if not selection:
        print("❌ TA error: No objects are selected. Select assets to clean.")
        return

    # We make Python go through EVERY object in the 'selection' list.
    for object_name in selection: 
    # Instead of taking only selection[0], we take object_name from each element of the list.

        # 2. Cleaning
        cmds.makeIdentity(object_name, apply=True, t=1, r=1, s=1)
        cmds.xform(object_name, centerPivots=True)
        
        print(f"🎉 QA PASS: Объект {object_name} Ready for export!")
    
    print("✅ All selected assets have successfully passed QA cleaning.")

cleanup_selected_asset()


             !!!For export to Unreal Engine, so that it stands on the ground !!!

import maya.cmds as cmds

def prepare_assets_for_ue():
    """
    Prepares selected objects for export to UE5:
    1. Resets transformations
    2. Centers pivot
    3. Places object on the ground (Y=0)
    """
    selection = cmds.ls(selection=True, type='transform')
    
    if not selection:
        print("❌ Error: No objects selected")
        return

    for obj in selection:
        bbox = cmds.exactWorldBoundingBox(obj)
        bottom_y = bbox[1]  # Bottom point on the Y axis

        # Move the object so that the bottom edge is at Y=0.
        cmds.move(0, -bottom_y, 0, obj, relative=True)

        # Reset transformations after displacement
        cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1)

        # Center the pivot
        cmds.xform(obj, centerPivots=True)

        print(f"✅ {obj} prepared for UE5 (on the ground, pivot center, transformations reset)")

    print("✅ All selected objects are ready for export to UE5.")

# Call function for selected objects
prepare_assets_for_ue()
