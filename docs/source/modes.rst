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

`Single mode tutorial <https://youtu.be/wHtF12qiRgI>`_

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
			
			.. note::
				Rigidbody and collider components will automatically be temporarily added if they are missing.
		
		
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
		`Snap cube to cell example.`
		
		
	**Draw forward arrow** : show forward rotation of target object.
	
	**Show edit info** : show rotation and local of position of target object.
	
	**Snapping settings:**
	
		.. image:: images/modes/SingleMode/SingleModeTab7.png
	
		**Enable rotation snapping:**
			* **Snap angle value** : value of rotation snapping.					
		**Enable position snapping:**
			* **Snap position value** : value of position snapping.
		**Enable scale snapping:**
			* **Snap scale value** : value of scale snapping.
			* **Scale step** : value of increasing scale by button.

Brush mode
------------

``Brush mode is used to position multiple objects on any surface.``

`Brush mode tutorial <https://youtu.be/CrvR2lRYawo>`_

	.. note::
		**How to use:**
							
		Click `E` button to spawn objects under the brush.		


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
	`Brush example 1.`
	
	
	.. image:: images/modes/BrushMode/BrushAnim2.gif
	`Brush example 2.`
	
	
	.. image:: images/modes/BrushMode/BrushAnim3.gif
	`Brush example 3 (slope angle 30 degrees enabled).`

Line mode
------------

``Line mode is designed for placing objects along a line.``

`Line mode tutorial <https://youtu.be/BPoSkfNI7FY>`_

	.. note::
		**How to use:**
							
		Click `E` button to start the line, after the line is set, press the `E` button again to spawn line of the objects.
		
	* **Line type:**
	
		.. image:: images/modes/LineMode/LineModeTab1.png
		* **Free** : places objects on a grid in the direction of the cursor.

		.. image:: images/modes/LineMode/LineModeTab2.png
		`Free line example (endless line enabled).`
		
		
		.. image:: images/modes/LineMode/LineModeTab3.png
		* **Fixed** : create straight lines on a grid.
		
		* **Free/Fixed line settings:**
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
			
			
		.. image:: images/modes/LineMode/LineModeTab4.png
		`Fixed line example.`
		
		.. note::
			`Snap same floor` feature for auto-snap available.
		
		.. image:: images/modes/LineMode/LineModeTab5.png
		* **Curved** : place objects along a curved line.	
			* **Common settings:**
				* **Curve line type:**
					* **Bezier**
					* **Simple line**
					* **Circle**
				* **Snap type:**
					* **Disabled**
					* **Lock Y** : Y position is fixed.
					* **Auto Snap** : the object of the curve is automatically attached to the surface.
				* **Object normal type:**
					* **Up**
					* **Curve direction**
					* **Surface normal**
					* **Custom** : user normal.
			* **Tabs:**
				* **Common**
					* **Loop line** : should the line be looped.
					* **Additive euler rotation** : additional rotation for each object.
					* **Flexible spacing** : position of objects on the curve depending on their size.
					* **Spacing length** : user spacing.
					* **Clamp tangents** : tangents move together relative to the central node.
				* **Custom**
					* **Auto snap:**
						* **Attach to mesh** : should the object be attached to the mesh.
						* **Snap layer mask** : layer for attaching objects.
						* **Raycast direction** : direction of the raycast.
						* **Raycast distance** : raycast from offset point to raycast direction distance.
						* **Offset raycast distance** : offset from zero Y surface.
				* **Visual**
					* **Curve color** : color of the curve.
					* **Handles type** : handle type for tangents.
						* **Sphere**
						* **Position handle**
					* **Draw nodes** : display handles of the nodes.
					* **Draw buttons** : display add/remove buttons of the curve segments.
					* **Draw tangents** : display tangents of the nodes.
					* **Bezier segment line count** : count of bezier segments between nodes (the more segments the more accurate the curve).
					
		.. image:: images/modes/LineMode/LineModeTab6.png
		`Simple line example (random pattern enabled).`		
		
		.. image:: images/modes/LineMode/LineModeTab7.png
		`Bezier line example (auto-snap enabled).`		
		
		.. image:: images/modes/LineMode/LineModeTab8.png
		`Circle line example (object random enabled).`

		.. note::
			For simple line segment can be added by `Ctrl` and `left-mouse click` hotkeys.
		
Area mode
------------

``Area mode is designed for positioning objects by area.``

`Area mode tutorial <https://youtu.be/QqRKa3xVoyI>`_

	.. note::
		**How to use:**
							
		* Click `E` button to start the area, 
		.. image:: images/modes/AreaMode/AreaModeTab1.png
		
		* After the area is set, press the `E` button again to spawn area of the objects.
		.. image:: images/modes/AreaMode/AreaModeTab2.png
		
	.. image:: images/modes/AreaMode/AreaModeTab3.png

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
		`Snap same floor` feature for auto-snap available.

Destroy mode
------------

``Destroy mode is designed for convenient destruction of objects in the scene.``

`Destroy mode tutorial <https://youtu.be/aZUhq0YlEk8>`_

	.. note::
		**How to use:**
								
		Click `E` button to start the destroy area, after the area is set, press the `E` button again to destroy the selected area.
			
	.. image:: images/modes/DestroyMode/DestroyModeTab1.png
	
	* **Delete mode:**
		* **MapTile grid delete**	
			* **Delete floor method:**
				* **Disabled**
				
				.. image:: images/modes/DestroyMode/DestroyModeTab2.png
				* **Selected** : selected floors are deleted.
					* **Floor height** : floor height in unity units.
					* **Floor precision** : offset on the edges between floors.
					* **Min floor number** : min floor number for delete. 
					* **Max floor number** : max floor number for delete. 
					
				.. image:: images/modes/DestroyMode/DestroyModeTab3.png
				* **Cell last amount** : selected top floors are deleted.
					* **Floor amount** : number of floors to remove.
					
				.. image:: images/modes/DestroyMode/DestroyModeTab4.png
				* **Area max amount** : maximal level floors are deleted.
					* **Floor amount** : number of floors to remove.	
					
			.. image:: images/modes/DestroyMode/DestroyModeTab5.png
			`Cell last amount remove example.`			
			
			.. image:: images/modes/DestroyMode/DestroyModeTab6.png
			`Selected 0 - 2 floors to remove example.`
					
					
		.. note::
			* The floor delete method only works on GameObjects with MapTile component.
			* Enable auto-snap to attach cursor for any surface.
			
		* **Raycast deletion:**	
			* **Common delete settings:**
				* **Allow delete not prefab** : gameobjects (not prefabs) can be deleted.
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
					
				.. note::
					**How to use:**
					
					Click `E` button to destroy objects under the brush.
					
			.. image:: images/modes/DestroyMode/DestroyModeTab7.png
			`Box raycast remove example.`		
			
			.. image:: images/modes/DestroyMode/DestroyModeTab8.png
			`Brush raycast remove example.`		
					
		.. note::
			The raycast method only works on any GameObject with collider.
			
				* **Screen selection**
					* **Selection object method:**
						* **Multiple** : all objects under selection box will be selected.
						* **Single** : only 1 object under the cursor will be selected.
					* **Auto destroy on select** : object will automatically be deleted after selection.
					* **Selection color** : color of the selection box.
					
				.. note::
					**How to use:**
							
					Click `E` button to start the selection box, after the objects are selected, press the `space` button to destroy them.
					
			.. image:: images/modes/DestroyMode/DestroyModeTab9.png
			`Screen selection remove example.`		

Tileset mode
------------

``Tileset area is created to create areas of linked tiles.``

`Tileset area mode tutorial <https://youtu.be/LaKgNFQdPNI>`_

	.. note::
		**How to use:**
							
		Click `E` button to start the tileset area, after the area is set, press the `E` button again to spawn tileset area.

	* **Selected MapTile prefab** : what MapTile prefab is selected.
	* **Selected tileset** : what tileset prefab is selected.
	
	**How to create tileset:**	
		* Toggle `create new tileset settings`.
		* Enter tileset name.
		* Press create button.
		.. image:: images/modes/TilesetArea/TilesetAreaTab1.png
		
		* Drag and drop the desired prefabs into the box (the default prefab should drop first).
		
		.. image:: images/modes/TilesetArea/TilesetAnim1.gif
		* Press open tile edit mode prefab to configure the tile set.
		* Select the cells where the connection of the tiles will be.
		
			.. image:: images/modes/TilesetArea/TilesetAnim2.gif
				:width: 250
			.. image:: images/modes/TilesetArea/TilesetAnim3.gif
				:width: 250
			.. image:: images/modes/TilesetArea/TilesetAnim4.gif
				:width: 250
			.. image:: images/modes/TilesetArea/TilesetAnim5.gif
				:width: 250
			.. image:: images/modes/TilesetArea/TilesetAnim6.gif
	
Translate mode
------------

``Translate mode is designed to move the set of object.``

`Translate mode tutorial <https://youtu.be/mlIa1BwmDiE>`_

	.. note::
		**How to use:**							
			* Click `E` button to start the selection area.
			* Move the scene handle to the desired position.
			* Press the `E` button again to translate selected objects.

	.. image:: images/modes/TranslateMode/TranslateModeTab1.png
	
	* **Movement type:**
		* **World cursor** : objects move along the world cursor.
		* **Scene handle** : objects move along the scene handle.
	* **Translate mode:**
		* **Full translate** : objects can be moved only if all selected objects can be moved.
		* **Partial translate** : will be translated those objects that do not intersect other objects.
		* **Can replace** : intersected objects can be replaced when the selected objects are translated.
	* **Selection method:**
		* **Map** : selecting objects on the grid.
		* **Screen selection** : selecting objects under the selection box.
	* **Hide source selected objects** : source objects will be hidden for the time of the translating.
	* **Show intersected objects** : intersected objects will be highlighted.
		* **Intersected objects color** : the color of the intersected objects highlighting.
	* **Report translate result** : on/off translate result report in the console.
	* **Snap to grid**	
		* **Snap grid enabled** : snapping on the grid.
			* **Cell offset** : value of offset in grid cells.
			* **Custom Y Snap** : custom snapping value for Y axis.
		* **Snap grid disabled:**	
			* **Translate snap type** : custom snapping.
				* **Snap translate** : offset of translation will be snapped.
				* **Snap position** : position of translated objects will be snapped.
			* **Snap value**
	* **Lock Y Axis** : when moving objects, the Y axis will be locked.
	
	.. image:: images/modes/TranslateMode/TranslateModeAnim1.gif
	`Translate mode example 1`	
	
	
	.. image:: images/modes/TranslateMode/TranslateModeAnim2.gif
	`Translate mode example 2`

Create template mode
------------

``Template mode is designed to create template prefabs from existing prefabs.``

`Template mode tutorial <https://youtu.be/c67ExYwabG0>`_

	.. note::
		**How to use:**
			* Click `E` button to start the selection area, after the desired objects are selected, configure the template parameters and click the `create` button.
			.. image:: images/modes/TemplateMode/TemplateMode1.png
			* After the desired objects are selected, configure the template parameters.
			* Click the `create` button.

	.. image:: images/modes/TemplateMode/TemplateMode2.png
	
	* **Selection method:**
		* **Map:** selecting objects on the grid.
		* **Screen selection:** selecting objects under the selection box.
			* **Object type:**
				* **Any** : any object can be selected.
				* **MapTile** : only `MapTile` objects can be selected.
				* **Default gameobject** : only default gameobject (without `MapTile` component) objects can be selected.
			* **Target layer** : layer of objects to be selected.
			* **Selection object method:**
				* **Multiple** : all objects under selection box will be selected.
				* **Single** : only 1 object under the cursor will be selected.
			* **Selection color** : color of the selection box.
	* **Template prefab name** : template name.
	* **Template create path** : template creation path.
	* **Template object type:**
		* **MapTile** : template will be created with the MapTile component.
		* **Default gameobject** : template will be created without the MapTile component.
	* **Child prefab type:**
		* **Linked prefab** : child objects of the template are linked prefabs.
		* **Prefab clone**: child objects of the template are prefab clones.
	* **Category type:**
		* **Template**: template prefab is added to the template category.
		* **Custom**: template prefab is added to the custom category.
			* **Category**: name of the custom category.
	* **Delete child components**: delete all unity-components of the object.
		* **Delete only MapTile**: or only MapTile component
	* **Delete child colliders**: delete colliders of created object
	* **Selected object count**: the number of selected objects for the template.
	* **Template pivot**: local pivot position of the template.
	* **Current template tile size**: the current grid size of the template.
	* **Draw bounds**: draw bounds of the template.
		* **Y bounds size**: y bounds size of the template.
		* **Bounds color**: color of the bounds.
		
	.. image:: images/modes/TemplateMode/TemplateMode3.png
	
	.. image:: images/modes/TemplateMode/TemplateModeAnim1.gif
	`Template mode example.`

