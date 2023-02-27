.. _modes:

Modes Overview
=====

.. contents::
   :local:
   :depth: 2
	
Common Info
------------

	.. note::
		To start creating objects, select the object in the inspector, select the desired spawn position, and press the `E` key to create the object (you can change the create :ref:`hotkey <hotKeys>` to whatever you want).
		
		Each edit mode has its own special features, which are described below.

.. _singleMode:

Single Mode
------------

``The single mode is used for the positioning of single objects.``

`Single mode tutorial <https://youtu.be/wHtF12qiRgI>`_

	.. image:: images/modes/SingleMode/SingleModeTab1.png
	
Object Mode
~~~~~~~~~~~~

Create new 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new object by using different tools.
	
Select
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select an existing object in the scene and modify it using the various single edit tools described below.
		
Edit Mode
~~~~~~~~~~~~
	
Simple
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Spawn objects without any additional adjustments.

Custom handles
^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
Create an object by modifying it with position, rotation and scale handles.
		
	.. image:: images/modes/SingleMode/SingleModeTab2.png
	
| **Show rotation handle** : show rotation handle of target object.

**Rotation handle type:**
	* **Sphere** : edit object rotation with sphere handle.
	* **Arc** : edit object rotation with arc handle.
	
| **Show movement handle** : show movement handle of target object.
| **Clamp cell movement** : object movement constraint within the grid cell.

	.. image:: images/modes/SingleMode/SelectEditExample.png
		
Cursor point rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^
		
Rotates the object in the direction of the cursor.
		
	.. image:: images/modes/SingleMode/CursorPointExample.png
		
Custom point rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rotates the object towards the target object.		
		
	.. image:: images/modes/SingleMode/SingleModeTab4.png
	
		* **Snap Y Axis** : snap target object to the Y axis.
		* **Target point position** : position of target point.
	
	.. image:: images/modes/SingleMode/CustomPointRotationExample.png		
	
	.. note::
		By default, you can change the scale of the object using the `left-ctrl` key and the `mouse wheel` keys.

Physics Placing
^^^^^^^^^^^^^^^^^^^^^^^^^^^		
		
Place objects using physics.
		
	.. image:: images/modes/SingleMode/SingleModeTab5.png
	
**Simulation settings:**
	* **Auto stop simulation** : physics simulation will automatically stop after the objects are frozen in position.
	* **Auto destroy falling object** :
		* **Y destroy position** : position below which physical objects are automatically destroyed.
	
**Temp rigidbody settings:**
	* **Mass** : mass of temporarily created physical object.
	* **Drag** : drag value of temporarily created physical object.
	* **Angular drag** : angular drag value of temporarily created physical object.
	
| **Target point position** : position of the target point.

	|
	.. image:: images/modes/SingleMode/PhysicsPlacingExample.png
	`Physics placing example.`	
	
	.. note::
		Rigidbody and collider components are automatically added temporarily if missing.
		
		
Attach Mode
~~~~~~~~~~~~

Default
^^^^^^^^^^^^^^^^^^^^^^^^^^^		
		
Default object placing.

Brush
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

Create an object on any collider or mesh surface of another object.
		
	.. image:: images/modes/SingleMode/SingleModeTab6.png
	
	.. image:: images/modes/SingleMode/SingleModeTab6-1.png
		:width: 500

**Hit surface type:**
	* **Mesh** : attach object to mesh.
	* **Collider** : attach object to collider.
	
| **Attach layer** : layer of the hit object.
| **Normal offset** : offset from normal hit.
| **Additive euler rotation** : additional rotation Euler offset of the object.

* **Normal rotation:**
	* **Disabled** : default object rotation.
		* **Look normal** : look normal method for the attached object.
		* **Revert normal rotation** : inverse normal direction of the surface hit.
	* **Along normal** : along the normal method for the attached object.
		* **Along normal base** : normal base value (default Vector3(0,1,0)).	
		
* **Snap to cell** : snap tile to cell grid (useful for attaching cube tiles).
	* **Add surface pivot offset** : 
			
	|
	.. image:: images/modes/SingleMode/SingleModeTab6-2.png
	`Snap cube to cell example.`
		
Common Settings
~~~~~~~~~~~~

	**Draw forward arrow** : show forward rotation of target object.
	
	**Show edit info** : show rotation and local of position of target object.
	
Snapping Settings
~~~~~~~~~~~~
	
	.. image:: images/modes/SingleMode/SingleModeTab7.png
	
**Enable rotation snapping:**
	* **Snap angle value** : value of rotation snapping.		
	
**Enable position snapping:**
	* **Snap position value** : value of position snapping.
	
**Enable scale snapping:**
	* **Snap scale value** : value of scale snapping.
	* **Scale step** : value of the incrementing scale by key.

.. _brushMode:

Brush Mode
------------

``Brush mode is used to position multiple objects on any surface.``

`Brush mode tutorial <https://youtu.be/CrvR2lRYawo>`_

How To Use
~~~~~~~~~~~~
							
* Press `E` key to spawn objects under the brush.		

Attach Settings
~~~~~~~~~~~~

	.. image:: images/modes/BrushMode/BrushModeTab1.png

**Attach mode:**
	* **Default** : default object placement.
	* **Brush** : create an object on any collider surface or meshes another object.

**Hit surface type:**
	* **Mesh** : attach object to mesh.
	* **Collider** : attach object to collider.
	
| **Attach layer** : `layer <https://docs.unity3d.com/Manual/Layers.html>`_ of hit object.
| **Normal offset** : offset from normal hit.
| **Additive euler rotation** : additional rotation euler offset of the object.

**Normal rotation:**
	* **Disabled** : default object rotation.
	* **Look normal** : look normal method for the attached object.
		* **Revert normal rotation** : inverse normal direction of the surface hit.
	* **Along normal** : along normal method for the attached object.
		* **Along normal base** : normal base value (default Vector3(0,1,0)).	
		
| **Ignore previous created** : ignore previous created objects by brush.
| **Snap to cell** : snap tile to cell grid (available only for 1 object).
* **Has slope angle**
	* **Slope angle value** : angle to the surface allowed to create objects.
			
			
Brush Settings
~~~~~~~~~~~~

	.. image:: images/modes/BrushMode/BrushModeTab2.png
	
| **Brush radius** : radius of the brush.
| **Spacing length** : distance between the points that the objects are created.

**Randomize object count** : random count value of objects of the brush.
	* **Min object count** : minimum number of objects created at a time.
	* **Max object count** : maximum number of objects created at a time.
	
| **Object count** : fixed number of brush objects.

**Rotation along brush** : each object is rotated along the brush creation line..
	* **Additional rotation along brush** : additional rotation offset for objects along line.

	.. image:: images/modes/BrushMode/BrushExample1.png
	`Brush example 1.`
	
	
	.. image:: images/modes/BrushMode/BrushExample2.png
	`Brush example 2.`
	
	
	.. image:: images/modes/BrushMode/BrushExample3.png
	`Brush example 3 (slope angle 30 degrees enabled).`

.. _lineMode:

Line Mode
------------

``Line mode is designed for placing objects along a line.``

`Line mode tutorial <https://youtu.be/BPoSkfNI7FY>`_

How To Use
~~~~~~~~~~~~
							
* Press the `E` key to start the line, when the line is set, press the `E` key again to spawn a line of the objects.

Line Type
~~~~~~~~~~~~
		
Free		
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

Places objects on a grid in the direction of the cursor.

	.. image:: images/modes/LineMode/LineModeTab1.png

	|
	.. image:: images/modes/LineMode/LineModeTab2.png
	`Free line example (endless line enabled).`
		
Fixed		
^^^^^^^^^^^^^^^^^^^^^^^^^^^		
		
Create straight lines on a grid.

	.. image:: images/modes/LineMode/LineModeTab3.png
		
Free/Fixed line settings
""""""""""""""""""""""""""
		
| **Show info** : information about the number of objects on the line.
| **Spacing cell** : spacing cell between objects.
| **Endless line** : the line automatically continues after the created previous one. 
| **Show snap neighbors**

**Multifloor:** : enable multi-floor feature
	* **Auto reset floor** : auto reset of floor count to 1 after deselecting.
	* **Floor count** : number of object floors.
	* **Floor offset mode:**
		* **Custom** : user floor offset.		
		* **Mesh bounds** : Y-axis size of mesh renderer floor offset.			
		* **Collider bounds** : Y-axis size of collider floor offset.				
	* **Floor offset** : additional floor offset.
	
| **Rotation along line** : each object is rotated along the line..
			
	.. image:: images/modes/LineMode/LineModeTab4.png
	`Fixed line example (randomizer enabled).`		
	
	|
		
Free/Fixed edge settings
""""""""""""""""""""""""""

`Snap edge` movement type should be enabled in the `Overlay mapping` tab.

		.. image:: images/modes/LineMode/LineEdgeSettings.png

| **Snap every edge** : object is placed on each cell edge on the line.

**Add edge side offset** : adds an offset to the side of the line.
	* **Edge relative point** : point relative to which the offset will be applied to the side.
	* **Edge side offset** : offset value to the side.
			
		
	.. image:: images/modes/LineMode/LineEdgeExample.png
	`Fixed line example:`		
		* Randomizer with pattern (01) enabled.	
		* Snap edge enabled.
		* Edge side offset (0.5).		

|

	.. note::
		`Snap same floor` feature for :ref:`auto-snap <autoSnap>` available (`Snap Settings` tab).
		
Curved		
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

Place objects along a curved line.

	.. image:: images/modes/LineMode/LineModeTab5.png

Common settings
""""""""""""""""""""""""""

**Curve line type:**
	* **Bezier**
	* **Simple line**
	* **Circle**
	
**Snap type:**
	* **Disabled**
	* **Lock Y** : Y position is fixed.
	* **Auto Snap** : the object of the curve is automatically attached to the surface.
	
**Object normal type:**
	* **Up**
	* **Curve direction**
	* **Surface normal**
	* **Custom** : user normal.
				
Tabs
""""""""""""""""""""""""""

**Common**
	* **Loop line** : should the line be looped.
	* **Additive euler rotation** : additional rotation for each object.
	* **Flexible spacing** : position of objects on the curve according to their size.
	* **Spacing length** : user spacing.
	* **Clamp tangents** : tangents move together relative to the central node.
	
**Custom**
	* **Auto snap:**
		* **Attach to mesh** : should the object be attached to the mesh.
		* **Snap layer mask** : layer for attaching objects.
		* **Raycast direction** : direction of the raycast.
		* **Raycast distance** : raycast from offset point to raycast direction distance.
		* **Offset raycast distance** : offset from zero Y surface.
		
**Visual**
	* **Curve color** : color of the curve.
	* **Handles type** : handle type for tangents.
		* **Sphere**
		* **Position handle**
	* **Draw nodes** : display handles of the nodes.
	* **Draw buttons** : display add/remove buttons of the curve segments.
	* **Draw tangents** : display tangents of the nodes.
	* **Bezier segment line count** : number of Bezier segments between nodes (the more segments, the more accurate the curve).
					
			|
			
	.. image:: images/modes/LineMode/AdditionalCurveSettings.png
	* **Additional curve settings (:ref:`randomizer <randomizer>` window):**
		* **Flexible spacing [enabled]:**
			* **Ignore size** : object size in the line is ignored.
				* **Edge** : object takes the rotation of the previous object, also the line is finished by this object.
			
	
	|
	.. image:: images/modes/LineMode/LineModeTab6.png
	`Simple line example:`
		* Random pattern enabled.		
		* Flexible spacing enabled (additional `ignore size` & `edge` enabled at the pillar in the :ref:`randomizer <randomizer>` window).		
	
	|
	.. image:: images/modes/LineMode/LineModeTab7.png
	`Bezier line example:`
		* Auto-snap enabled.	
		* Random rotation enabled.	
	
	|
	.. image:: images/modes/LineMode/LineModeTab8.png
	`Circle line example (object random enabled).`

	.. note::
		For simple line segment can be added by `Ctrl` and `left-mouse click` :ref:`hotkeys <autoSnap>`.
		
.. _areaMode:
		
Area Mode
------------

``Area mode is designed for positioning objects by area.``

`Area mode tutorial <https://youtu.be/QqRKa3xVoyI>`_


How To Use
~~~~~~~~~~~~
							
* Press `E` key to start the area, 

	.. image:: images/modes/AreaMode/AreaModeTab1.png
		
* Once the area is set, press `E` key again to spawn the objects.

	.. image:: images/modes/AreaMode/AreaModeTab2.png
		
Settings
~~~~~~~~~~~~

	.. image:: images/modes/AreaMode/AreaModeTab3.png

| **Show info** : show information about object count of the area.

**Area mode type:**
	* **Default** : placing the object set on the area.
	* **Scale**	: scaling of a single object on an area.
	
| **Random spacing cell** : spacing cell between objects.
| **Spacing cell** : spacing cell between objects.

**Multifloor** : enable multi floor feature
	* **Auto reset floor** : auto reset floor count to 1 after unselect.
	* **Floor count** : count of object floors.
	* **Floor offset mode:**
		* **Custom** : user floor offset.		
		* **Mesh bounds** : Y axis size mesh renderer floor offset.			
		* **Collider bounds** : Y axis size collider floor offset.			
	* **Floor offset** : additional floor offset.

	.. note::
		`Snap same floor` feature for :ref:`auto-snap <autoSnap>` available (`Snap Settings` tab).

.. _destroyMode:

Destroy Mode
------------

``Destroy mode is designed for conveniently destroying objects in the scene.``

`Destroy mode tutorial <https://youtu.be/aZUhq0YlEk8>`_

How To Use
~~~~~~~~~~~~
								
* Press `E` key to start the destroy area, after the area is set, press the `E` key again to destroy the selected area.
			
	.. image:: images/modes/DestroyMode/DestroyModeTab1.png
	
Delete Mode
~~~~~~~~~~~~

MapTile grid delete		
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

* **Delete floor method:**
	* **Disabled**
		
	.. image:: images/modes/DestroyMode/DestroyModeTab2.png
	* **Selected** : selected floors are deleted.
		* **Floor height** : floor height in unity units.
		* **Floor precision** : offset on the edges between floors.
		* **Min floor number** : min floor number for delete. 
		* **Max floor number** : max floor number for delete. 
		
	|
	.. image:: images/modes/DestroyMode/DestroyModeTab3.png
	* **Last count** : selected top floors are deleted.
		* **Floor count** : number of floors to remove.
			
	|
	.. image:: images/modes/DestroyMode/DestroyModeTab4.png
	* **Max index count** : only floors with a maximum index will be deleted.
		* **Floor count** : number of floors to remove.	
			
	|
	.. image:: images/modes/DestroyMode/DestroyModeTab5.png
	`Last count remove example.`			
	
	|
	.. image:: images/modes/DestroyMode/DestroyModeTab6.png
	`Selected 0 - 2 floors remove example.`
					
					
	.. note::
		* The floor delete method only works on GameObjects with :ref:`MapTile <maptile>` component.
		* Enable auto-snap to snap the cursor to any surface.
			
Raycast deletion		
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

Common settings
""""""""""""""""""""""""""

| **Allow delete not prefab** : gameobjects (not prefabs) can be deleted.

**Object type:**
	* **Any** : any object can be deleted.
	* **MapTile** : only :ref:`MapTile <maptile>` objects can be deleted.
	* **Default gameobject** : only default gameobject (without :ref:`MapTile <maptile>` component) objects can be deleted.
	
| **Target layer** : `layers <https://docs.unity3d.com/Manual/Layers.html>`_ that will be deleted.
**Draw debug** : show the bounds of the deletion process.
	* **Debug color** : debug colour.
	
Unique settings
""""""""""""""""""""""""""	

* **Box raycast**			
	* **Y box offset** : offset from surface.
	* **Max box raycast distance** : raycast distance from offset point.
* **Brush raycast**
	* **Brush radius** : radius of the delete brush.
	* **Attach to surface:**
		* **Attach layer** : `layer <https://docs.unity3d.com/Manual/Layers.html>`_  to which the brush is attached.
	* **Y brush raycast normal offset** : offset from brush hit surface.
	* **Max brush raycast distance** : raycast distance from offset point.
				
		.. note::
			**How to use:**
				
			Press `E` key to destroy objects under the brush.
				
	.. image:: images/modes/DestroyMode/DestroyModeTab7.png
	`Box raycast remove example.`		
		
	.. image:: images/modes/DestroyMode/DestroyModeTab8.png
	`Brush raycast remove example.`		
				
	.. note::
		The raycast method only works on any GameObject with collider.
			
Screen selection	
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

How To Use
""""""""""""""""""""""""""

* Press the `E` key to start the selection box, after selecting the objects, press the `Spacebar` key to destroy them.
					
	.. image:: images/modes/DestroyMode/DestroyModeTab9.png
	`Screen selection remove example.`	

Settings
""""""""""""""""""""""""""

* **Selection object method:**
		* **Multiple** : all objects under the selection box are selected.
		* **Single** : only 1 object under the cursor is selected.
	* **Auto destroy on select** : object is automatically be deleted after selection.
	* **Selection color** : colour of the selection box.

.. _tilesetMode:

Tileset Mode
------------

``Tileset area is used to create areas of linked tiles.``

`Tileset area mode tutorial <https://youtu.be/LaKgNFQdPNI>`_

How To Use
~~~~~~~~~~~~

* Press `E` key to start the tileset area, after the area is set, press the `E` key again to spawn tileset area.


How To Create Tileset
~~~~~~~~~~~~

* Toggle `Create new tileset settings`.
* Enter `Tileset name`.
* Press `Create` button.

	.. image:: images/modes/TilesetArea/TilesetAreaTab1.png

|
* Drag and drop the desired prefabs into the box (the default prefab should drop first).

	.. image:: images/modes/TilesetArea/TileSetAreaExample1.png
	.. image:: images/modes/TilesetArea/TileSetAreaExample2.png

|
* Press `Open tile edit mode prefab` to configure the tile set.
* Select the cells where the connection of the tiles will be.

	.. image:: images/modes/TilesetArea/TilesetConnectionExample1.png
	|
	.. image:: images/modes/TilesetArea/TilesetConnectionExample2.png
	|
	.. image:: images/modes/TilesetArea/TilesetConnectionExample3.png
	|
	.. image:: images/modes/TilesetArea/TilesetConnectionExample4.png
		
	`Tile connection setup example examples.`						
		
	|
	.. image:: images/modes/TilesetArea/CreateTilesetExample1.png
	`Create tileset area example.`		
	
	.. note::
		At the moment, the tilesets only work for flat tiles.

Settings
~~~~~~~~~~~~

| **Selected MapTile prefab** : what :ref:`MapTile <maptile>` prefab is selected.
| **Selected tileset** : what tileset prefab is selected.
	
.. _translateMode:
	
Translate Mode
------------

``Translate mode is used to move the set of objects.``

`Translate mode tutorial <https://youtu.be/mlIa1BwmDiE>`_

How To Use
~~~~~~~~~~~~

* Press `E` key to start the selection area.
* Move the scene handle to the desired position.
* Press the `E` key again to translate selected objects.

Settings
~~~~~~~~~~~~

	.. image:: images/modes/TranslateMode/TranslateModeTab1.png
	
Scene settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^		
	
**Movement type:**
	* **World cursor** : objects move along the world cursor.
	* **Scene handle** : objects move along the scene handle.
**Translate mode:**
	* **Full translate** : objects can only be moved only if all selected objects can be moved.
	* **Partial translate** : will be moved those objects that do not intersect other objects.
	* **Can replace** : intersected objects can be replaced when the selected objects are moved.
**Selection method:**
	* **Map** : selecting objects on the grid.
	* **Screen selection** : selecting objects under the selection box.
		
Translate settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

* **Show intersected objects** : intersected objects will be highlighted.
	* **Intersected objects color** : the colour of the intersected objects highlighting.
	
| **Check intesection for Overlay** : intersections for overlay objects are detected by the raycast.
		
Other settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

| **Report translate result** : on/off moving result report in the console.
| **Hide source selected objects** : source objects will be hidden for the duration of the moving process.
| **Move intersected to source position** : objects will be moved to the start position if they have an intersection.

* **Delayed heavy calculation** : calculation of intersections will be delayed with a large number of objects.
		* **Heavy calculation object count** : count of objects to start a delay.
		* **Calculation delay duration** : duration of the delay after a position change.
		
Snap settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^		

* **Snap to grid**	
	* **Snap grid enabled** : snap to the grid.
		* **Cell offset** : value of offset in grid cells.
		* **Custom Y Snap** : custom snapping value for Y axis.
		
	* **Snap grid disabled:**	
		* **Translate snap type** : custom snapping.
			* **Snap translate** : translation offset will be snapped.
			* **Snap position** : position of translated objects will be snapped.
		* **Snap value**
		
| **Lock Y Axis** : when moving objects, the Y axis is locked.
	
	.. note::
		Moving a large number of objects can take a very long time.		
		
		To quickly move a large number of objects, turn on `Can replace` mode and turn off `Show intersected objects`.
	|
	.. image:: images/modes/TranslateMode/TranslateModeExample1.png
	`Translate mode example 1.`	
	
	|
	.. image:: images/modes/TranslateMode/TranslateModeExample2.png
	`Translate mode example 2 (Red object is a source, blue object is the intersected object).`

.. _templateMode:

Create Template Mode
------------

``Template mode is designed to create template prefabs from existing prefabs.``

`Template mode tutorial <https://youtu.be/c67ExYwabG0>`_

How To Use
~~~~~~~~~~~~

* Press `E` key to start the selection area, after the desired objects are selected, configure the template parameters and click the `Create` button.

	.. image:: images/modes/TemplateMode/TemplateMode1.png

* After the desired objects are selected, configure the template parameters.
* Click the `Create` button.

Settings
~~~~~~~~~~~~

	.. image:: images/modes/TemplateMode/TemplateMode2.png
	
**Selection method:**
	* **Map:** selecting objects on the grid.
	* **Screen selection:** selecting objects under the selection box.
		* **Object type:**
			* **Any** : any object can be selected.
			* **MapTile** : only :ref:`MapTile <maptile>` objects can be selected.
			* **Default gameobject** : only default gameobject (without :ref:`MapTile <maptile>` component) objects can be selected.
		* **Target layer** : `layer <https://docs.unity3d.com/Manual/Layers.html>`_ of objects to be selected.
		* **Selection object method:**
			* **Multiple** : all objects under selection box will be selected.
			* **Single** : only 1 object under the cursor will be selected.
		* **Selection color** : color of the selection box.
		
| **Template prefab name** : template name.
| **Template create path** : template creation path.

**Template object type:**
	* **MapTile** : template will be created with the :ref:`MapTile <maptile>` component.
	* **Default gameobject** : template will be created without the :ref:`MapTile <maptile>` component.
	
**Child prefab type:**
	* **Linked prefab** : child objects of the template are linked prefabs.
	* **Prefab clone**: child objects of the template are prefab clones.
	
**Category type:**
	* **Template**: template prefab is added to the template category.
	* **Custom**: template prefab is added to the custom category.
		* **Category**: name of the custom category.
		
**Delete child components**: delete all unity-components of the object.
	* **Delete only MapTile**: or only :ref:`MapTile <maptile>` component
	
| **Delete child colliders**: delete colliders of created object
| **Selected object count**: the number of selected objects for the template.
| **Template pivot**: local pivot position of the template.
| **Current template tile size**: the current grid size of the template.

**Draw bounds**: draw bounds of the template.
	* **Y bounds size**: Y bounds size of the template.
	* **Bounds color**: colour of the bounds.
		
	|
	.. image:: images/modes/TemplateMode/TemplateMode3.png
	`Template mode example.`

