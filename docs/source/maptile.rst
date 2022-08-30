.. _maptile:

MapTile component overview
=====

MapTile component settings
------------

``Map tile component is used for the calculation of intersections on the grid, but if you don't need it, you can use default game objects without `MapTile` component.``

	.. image:: images/maptile/MapTile.png
	
* **Map** : reference to `MapCreator`.
* **Map tile layer** : current `MapTile` layer.
* **Movement type:**
	* **Cell** : moving an object on a grid.
		* **Auto snap position** : enable grid snapping for the object.
			* **Allow y axis movement** : can the object move along the Y-axis.
			* **Auto apply old local offset** : the object in the new cell will be set with the old local offset.
	* **Local offset** : moving within a grid cell.
		* **Clamp local offset** : fixing the object only inside the current object cell.
	* **Default** : default moving.
* **Auto make changes map** : any change of the object's position changes the map grid.
* **Allow replace intersted tiles** : if objects in the current layer intersect (except Overlay layer), they will be deleted.
* **Size:**
	* **Width** : X tile size of the object.
	* **Height** : Y tile size of the object.
* **Cell local offset** : the current local offset relative to the center of the current object cell.
* **Tiles** : coordinates of the grid on which the objects are located.
* **Draw bounds:**
	* **Draw current bounds** : displays the bounds of the current object.
	* **Draw cell bounds** : displays the bounds of the current object on the grid.
	* **Bounds color** : color of the bounds of the current object.
	* **Cell bounds color** : color of the bounds of the current object on the grid.
	* **Y bounds size** : Y-axis size of the bounds object.
* **Show cells** : settings to add cells to ignore calculations.
	* **Object Y space** : cells are displayed at the Y position of the object.
	* **Show buttons** : displays buttons to add ignore cells.
	* **Show buttons relative cursor** : displays buttons only under the cursor.
	* **Local gaps** : local coordinates of cells that are ignored for calculations.
		
	.. note::
		Cell ignoring can be useful for non-square or square tiles with gaps.
			
MapTile layer
------------

``Each `MapTile` object has its own layer, (Layer 1, Layer2, ..., Layer9) are default layers that are used to calculate the grid, and the overlay layer is used for objects that do not need a grid.``

	.. note::
		You can change the name of the layer here :ref:`mapHolder`.
		
MapCreator layer
------------

``MapCreator layers is used to configure the display, selection, removal of objects of the selected layer in the scene and display in the inspector, depending on the selected edit mode.``

	.. image:: images/maptile/LayerSettings1.png
	* **Show all layers [if disabled]:`**
		* **Selected `MapTile` layer**
		* **Disable other object layers** : turn off objects in the scene with the improper layer.
	
	|
	
	Adjust the layers for displaying objects in the inspector according to their layer.
	
	.. image:: images/maptile/LayerSettings2.png
	
	.. image:: images/maptile/LayerSettings3.png
	
	|
	.. image:: images/maptile/LayerSettings4.png	
	`Show only Layer1 objects example.`
	
	|
	.. image:: images/maptile/LayerSettings5.png
	`Show only Layer2 objects example.`
	
	|
	.. image:: images/maptile/LayerSettings6.png
	`Show only Overlay objects example.`