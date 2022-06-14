Modes overview
=====

.. _modes:
	
Common info
------------

	.. note::
		To start creating objects, select the object in the inspector, select the desired position to spawn and press the E button to create the object (you can change create hotkey to whatever you want).
		
		Each edit mode has its own features, which are detailed below.

Single mode
------------

``Single mode is used to position single objects.``

`YouTube tutorial <https://youtu.be/wHtF12qiRgI>`_

	.. image:: images/modes/SingleMode/SingleModeTab1.png
	
	**Object mode:**
		* **Create new** : create a new object by using different tools.
		* **Select** : select an existing object in the scene and modify it with various single edit tools described bellow.
		
	**Single edit mode:**
		* **Simple** : spawn objects without any additional adjustments.
		
		* **Custom handles** : create object by modifying it with position, rotation, scale handles.
		
			.. image:: images/modes/SingleMode/SingleModeTab2.png
				
			* **Show rotation handle** : show rotation handle of target object.
			* **Rotation handle type:**
				* **Sphere** : edit object rotation with sphere handle.
				* **Arc** : edit object rotation with arc handle.
			* **Show movement handle** : show movement handle of target object.
			* **Clamp cell movement** : clamp the object movement within grid cell.

		.. image:: images/modes/SingleMode/SelectEditAnim.gif
	


		* **Cursor point rotation** : rotates the object in the direction of the cursor.
		
		.. image:: images/modes/SingleMode/CursorPointAnim.gif
		


		* **Custom point rotation** : rotates the object in the direction of the target object.
		
		.. image:: images/modes/SingleMode/SingleModeTab4.png
		
			* **Snap Y Axis** : snap target object to the Y axis.
			* **Target point position** : position of target point.
		
		.. image:: images/modes/SingleMode/CustomPointRotationAnim.gif
		
		
		
		* **Physics placing** : place objects using physics.
		
		.. image:: images/modes/SingleMode/SingleModeTab5.png
		
			* **Simulation settings:**
				* **Auto stop simulation**
				* **Auto destroy falling object** :
					* **Y destroy position** : position below which physical objects are automatically destroyed.
				
			* **Temp rigidbody settings:**
				* **Mass** : mass of temp created physics object.
				* **Drag** : drag value of temp created physics object.
				* **Angular drag** : angular drag value of temp created physics object.
				
			* **Target point position** : position of target point.
			
			.. image:: images/modes/SingleMode/PhysicsPlacingAnim.gif
		
		
	**Attach mode:**
		* **Default** : default object placing.
		* **Brush** : create an object on any collider surface or meshes another object.
		
		.. image:: images/modes/SingleMode/SingleModeTab6.png
		
		.. image:: images/modes/SingleMode/SingleModeTab6-1.png
			:width: 500

		**Hit surface type:**
			* **Mesh** : attach object to mesh.
			* **Collider** : attach object to collider.
		**Attach layer** : layer of hit object.
		**Normal offset** : offset from normal hit.
		**Additive euler rotation** : additional rotation euler offset of the object.
		**Normal rotation:**
			* **Disabled** : default object rotation.
			* **Look normal** : look normal method for the attached object.
				* **Revert normal rotation** : inverse normal direction of the surface hit.
			* **Along normal** : along normal method for the attached object.
				* **Along normal base** : normal base value (default Vector3(0,1,0)).	
		**Snap to cell** : snap tile to cell grid (useful for attaching cube tiles).
			* **Add surface pivot offset** : 
			
		.. image:: images/modes/SingleMode/SingleModeTab6-2.png
		Snap cube to cell example.
		
		
	**Draw forward arrow** : show forward rotation of target object.
	
	**Show edit info** : show rotation and local of position of target object.
	
	
	**Snapping settings:**
	
	
	.. image:: images/modes/SingleMode/SingleModeTab7.png
	
		**Enable rotation snapping**
			**Snap angle value** : value of rotation snapping.					
		**Enable position snapping**
			**Snap position value** : value of position snapping.
		**Enable scale snapping**
			**Snap scale value** : value of scale snapping.
			**Scale step** : value of increasing scale by button.

Brush mode
------------

``Brush mode is used to position multiple objects on any surface``

	.. image:: images/modes/BrushMode/BrushModeTab1.png

	* **Attach settings:**
		* **Attach mode:**
			* **Default** : default object placing.
			* **Brush** : create an object on any collider surface or meshes another object.
		
		* **Hit surface type:**
			* **Mesh** : attach object to mesh.
			* **Collider** : attach object to collider.
		* **Attach layer** : layer of hit object.
		* **Normal offset** : offset from normal hit.
		* **Additive euler rotation** : additional rotation euler offset of the object.
		* **Normal rotation:**
			* **Disabled** : default object rotation.
			* **Look normal** : look normal method for the attached object.
				* **Revert normal rotation** : inverse normal direction of the surface hit.
			* **Along normal** : along normal method for the attached object.
				* **Along normal base** : normal base value (default Vector3(0,1,0)).	
		* **Ignore previous created** : ignore previous created objects by brush.
		* **Snap to cell** : snap tile to cell grid (available only for 1 object).
		* **Has slope angle**
			* **Slope angle value** : angle to the surface allowed to create objects.
			
			
	.. image:: images/modes/BrushMode/BrushModeTab2.png
	
	**Brush settings:**		
		* **Brush radius** : radius of the brush.
		* **Spacing length** : distance between the points that the objects are created.
		* **Randomize object count** : random count value of objects of the brush.
			* **Min object count** : minimum object count of random object creation.
			* **Max object count** : maximum object count of random object creation.
		* **Object count** : fixed count value of objects of the brush.
		* **Rotation along brush** : rotation of each object is rotated along the line of brush creation.
			* **Additional rotation along brush** : additional rotation offset for along line objects.


	.. image:: images/modes/BrushMode/BrushAnim1.gif
	Brush example1.
	
	
	.. image:: images/modes/BrushMode/BrushAnim2.gif
	Brush example2.
	
	
	.. image:: images/modes/BrushMode/BrushAnim3.gif
	Brush example3 (slope angle 30 degrees enabled).
	

Line mode
------------

``Line mode is designed for placing objects along a line``

	* **Line type:**
	
		.. image:: images/modes/LineMode/LineModeTab1.png
		* **Free** : places objects on a grid in the direction of the cursor.

		
		.. image:: images/modes/LineMode/LineModeTab2.png
		* **Fixed** : create straight lines on a grid.
		
		.. image:: images/modes/LineMode/LineModeTab3-0.png
		* **Curved** : place objects along a curved line.
	* **Show info** : show information about object count of the line.
	* **Spacing cell** : spacing cell beetween objects.
	* **Endless line** : the line automatically continues after the created previous one. 
	* **Show snap neighbors**
	* **Multifloor support:** : enable multi floor feature
		* **Auto reset floor** : auto reset floor count to 1 after unselect.
		* **Floor count** : count of object floors.
		* **Floor offset mode:**
			* **Custom** : user floor offset.		
			* **Mesh bounds** : Y axis size mesh renderer floor offset.			
			* **Collider bounds** : Y axis size collider floor offset.				
		* **Floor offset** : additional floor offset.
	* **Rotation along line** : rotation of each object is rotated along the line.

	.. note::
		`Snap same floor` feature for autosnap available
		
Area mode
------------

``Area mode is designed for positioning objects by area``

	* **Show info** : show information about object count of the area.
	* **Area mode type:**
		* **Default** : placing the object set on the area.
		* **Scale**	: scaling a single object on an area.
	* **Random spacing cell** : spacing cell beetween objects.
	* **Spacing cell** : spacing cell beetween objects.
	* **Multifloor support:** : enable multi floor feature
		* **Auto reset floor** : auto reset floor count to 1 after unselect.
		* **Floor count** : count of object floors.
		* **Floor offset mode:**
			* **Custom** : user floor offset.		
			* **Mesh bounds** : Y axis size mesh renderer floor offset.			
			* **Collider bounds** : Y axis size collider floor offset.				
		* **Floor offset** : additional floor offset.
		
	.. note::
		`Snap same floor` feature for autosnap available

Destroy mode
------------

``Destroy mode is designed for convenient destruction of objects in the scene``



	* **Delete mode:**
		* **MapTile grid delete**	
		
		.. note::
			**How to use:**
						
			Click `E` button to start the destroy area, after the area is set, press the E button again
			
			* **Delete floor method:**
				* **Disabled**
				* **Selected** : selected floors are deleted.
				* **Cell last amount** : selected top floors are deleted.
				* **Area max amount** : maximal level floors are removed.
				
					
			
		* **Raycast deletion:**	
			* **Common delete settings:**
				* **Allow delete not prefab** : not prefabs can be deleted.
				* **Object type:**
					* **Any** : any object can be deleted.
					* **MapTile** : only `MapTile` objects can be deleted.
					* **Default gameobject** : only default gameobject (without `MapTile` component) objects can be deleted.
				* **Target layer** : layers that will be deleted.
				* **Draw debug** : show bounds of deletion.
				* **Debug color** : color of debug.
			* **Unique delete settings:**
				* **Box raycast**			
					* **Y box offset** : offset from surface.
					* **Max box raycast distance** : raycast distance from offset point.
				* **Brush raycast**
					* **Brush radius** : radius of the delete brush.
					* **Attach to surface:**
						* **Attach layer** : layer to which the brush is attached.
					* **Y brush raycast normal offset** : offset from brush hit surface.
					* **Max brush raycast distance** : raycast distance from offset point.
				* **Screen selection**
				
				.. note::
					**How to use:**
						
					Click `E` button to start the selection box, after the objects are selected, press the space button to destroy them
						
					* **Selection object method:**
						* **Multiple** : all objects under selection box will be selected.
						* **Single** : only 1 object under the cursor will be selected.
					* **Auto destroy on select** : object will automatically be deleted after selection.
					* **Selection color** : color of the selection box.
					
					
					

Tileset mode
------------

``Tileset area is created to create areas of linked tiles``

	* **Selected MapTile prefab**
	* **Selected tileset**
	
	**How to create tileset:**
	* **Create new tileset settings**
	* **Tileset name**
	
Translate mode
------------

``Translate mode is designed to move the set of object``

	* **Movement type:**
		* **World cursor**
		* **Scene handle**
	* **Translate mode:**
		* **Full translate**
		* **Partial translate**
		* **Can replace**
	* **Selection method:**
		* **Map**
		* **Screen selection**
	* **Hide source selected objects**
	* **Show intersected objects**
	* **Intersected objects color**
	* **Report translate result**
	* **Snap to grid**	
		* Snap grid enabled:
			* **Cell offset**
			* **Custom Y Snap**
		* Snap grid disabled:		
			* **Translate snap type:**
				* **Snap translate**
				* **Snap position**
			* **Snap value**
	* **Lock Y Axis**

Create template mode
------------

``Template mode is designed to create template prefabs from existing prefabs``

	* **Selection method:**
		* **Map**
		* **Screen selection**
			* **Object type:**
				* **Any**
				* **MapTile**
				* **Default gameobject**
			* **Target layer**
			* **Selection object method:**
				* **Multiple**
				* **Single**
			* **Auto destroy on select**
			* **Selection color**
	* **Template prefab name**
	* **Template create path**
	* **Template object type**
		* **MapTile**
		* **Defalt gameobject**
	* **Child prefab type:**
		* **Linked prefab**
		* **Prefab clone**
	* **Category type**
		* **Template**
		* **Custom**
			* **Category**
	* **Delete child components**
		* **Delete only MapTile**
	* **Delete child colliders**
	* **Selected object count**
	* **Template pivot**
	* **Current template tile size**
	* **Draw bounds**
	* **Y bounds size**
	* **Bounds color**

