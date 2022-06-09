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

Single mode is used to position single objects.

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
			:width: 400

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

Brush mode is used to position multiple objects on any surface

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

Line mode is designed for placing objects along a line


Area mode
------------

Area mode is designed for positioning objects by area


Destroy mode
------------

Destroy mode is designed for convenient destruction of objects in the scene


Tileset mode
------------

Tileset area is created to create areas of linked tiles

Translate mode
------------

Translate mode is designed to move the set of object


Create template mode
------------

Template mode is designed to create template prefabs from existing prefabs
