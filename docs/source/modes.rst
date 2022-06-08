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

Single mode is used to position single objects

	.. image:: images/modes/SingleMode/SingleModeTab1.png
	
	**Object mode:**
		* **Create new** : create a new object by using different tools.
		* **Select** : select an existing object in the scene and modify it with various single edit tools described bellow.
		
	**Single edit mode:**
		* **Simple** : spawn objects without any additional adjustments.
		
		* **Custom handles** : create object by modifying it with position, rotation, scale handles.
		
			.. image:: images/modes/SingleMode/SingleModeTab2.png
				
			* **Show rotation handle** : show rotation handle of target object.
			* **Rotation handle type**
				* **Sphere** : edit object rotation with sphere handle.
				* **Arc** : edit object rotation with arc handle.
			* **Show movement handle** : show movement handle of target object.
			* **Clamp cell movement** : clamp the object movement within grid cell

		.. image:: images/modes/SingleMode/SelectEditAnim.gif
	

		* **Cursor point rotation** : rotates the object in the direction of the cursor.
		
		.. image:: images/modes/SingleMode/SingleModeTab3.png
		.. image:: images/modes/SingleMode/CursorPointAnim.gif
		

		* **Custom point rotation** : rotates the object in the direction of the target object
		
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
		.. image:: images/modes/SingleMode/SingleModeTab6-2.png
		.. image:: images/modes/SingleMode/SingleModeTab6-3.png
		
		
	**Draw forward arrow** : show forward rotation of target object.
	
	**Show edit info** : show rotation and local of position of target object.
	
	**Snapping settings**
	
	.. image:: images/modes/SingleMode/SingleModeTab7.png
	
		**Enable rotation snapping**
			**Snap angle value**					
		**Enable position snapping**
			**Snap position value**
		**Enable scale snapping**
			**Snap scale value**
			**Scale step**

Brush mode
------------

Brush mode is used to position multiple objects on any surface


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
