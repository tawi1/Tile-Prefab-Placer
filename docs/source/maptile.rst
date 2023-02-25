.. _maptile:

MapTile Component Overview
=====

.. contents::
   :local:
   
Component Settings
------------

``MapTile component is used in order to determine intersections on the grid, but if you don't need it, you can use default game objects without `MapTile` component.``

	.. image:: images/maptile/MapTile.png
	
* **Map** : reference to :ref:`MapCreator <mapCreator>`.
* **Map tile layer** : current `MapTile` :ref:`layer <maptileLayer>`.

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
			
.. _maptileLayer:

MapTile Layer
------------

``Each `MapTile` object has its own layer, (Layer 1, Layer2, ..., Layer9) are default layers that are used to calculate the grid, and the overlay layer is used for objects that do not need a grid.``

	.. note::
		You can change the name of the layer here :ref:`mapHolder`.	