Getting started
************

.. _installation:

.. contents::
   :local:

Installation
============

`Getting started tutorial <https://youtu.be/Y_LklnjDQ2U>`_

**Steps to use Tile Prefab Placer:**

#. Download & import from unity asset store.

#. First time initialization window will appear automatically or you can open it manually in toolbar ``604Spirit/MapEditor/Window/Map Creator Initialization.``

	.. image:: images/gettingstarted/InitilizationWindow.png

#. Set the root path of the tool, it is automatically detected (or manually press the `Detect Root` button if you changed the root of the tool prefab path).

#. Click the `Create & init MapCreator` button (if you want to change the tool prefab root path, you will need to repeat the previous 2 steps). 

#. Select tile 1x1 size to adjust the tile size of the tool.

		.. image:: images/gettingstarted/TileInitilization.png
		
	|
	* Drag the 1x1 size of the tile into the field & press `Show info` button.
		.. image:: images/gettingstarted/TileInitilization2.png

	* Press `Set exist config` to assign the tile size to the tool.
	
	|
	
#. Click `Load Packages` to start downloading the packages required for this tool.

	.. image:: images/gettingstarted/PackageSetupWindow.png

	.. note::
		**Required packages:**
		
		* **Editor coroutines** (`com.unity.editorcoroutines`) - unity package which allows developers to run constructs similar to Unity’s monobehaviour based coroutines within the editor using arbitrary objects.
		
		* **Naughty Attributes** (`com.dbrizov.naughtyattributes`) - extension for unity inspector made by Denis Rizov, also you can manually download it from unity asset store `Naughty Attributes <https://assetstore.unity.com/packages/tools/utilities/naughtyattributes-129996>`_


	.. note::
		**Script define symbols required for the project:**
			* **MAP_EDITOR**
	
#. Set the tile path in the `MapCreator`'s cached tab where the prefab categories are stored.

	.. image:: images/gettingstarted/CachedValuesTabPrefabPath.png

.. _prefabs:

Prefabs
=======

``MapCreator's scroll view consists of prefab categories.``

**Category** - it's a prefab set, create categories according to your needs.

**How to create categories**
-----------------------------

	.. image:: images/gettingstarted/AddCategory1.png

* Click ``+`` button to start adding category.
* Enter category name.
* Click ``add`` button.

	.. note::
		To delete a category, select category and click the ``-`` button.

**How to add prefabs**
-----------------------

	* Drag & drop desirable prefabs to drop tab.	
		.. image:: images/gettingstarted/AddingPrefabs1.png


	* Prefabs are ready to use.
		.. image:: images/gettingstarted/AddingPrefabs2.png

	.. note::
		:ref:`MapTile <maptile>` component is used in order to calculate intersections of objects on the grid without colliders, so if you don't need it, you can use default game objects.


.. _category:

Category
========

.. image:: images/gettingstarted/CategorySOExample.png

* **Title** : name of category.
* **Prefab data:**
	* **Prefab** : reference to the prefab gameobject.
	* **MapTilePrefab** : reference to the :ref:`MapTile <maptile>` prefab.
	* **TileSize** : object size in grid cells (you can set the size manually if the prefab doesn't have a :ref:`MapTile <maptile>` component).
* **MapTile category parent type:** 
	* **Local map path** : object is created regarding to the path of the `MapCreator` layer.
	* **Scene path** : object is created regarding to the path of the scene root.
* **Scene path** : object creation path.


.. _configs:

Configs
=======

**Cached Values Settings**
--------------------------

	.. image:: images/gettingstarted/CachedValuesTab.png

* **Root** : root for `MapCreator`'s stuff.
* **Default Game Objects Root** : root for created default game objects (without :ref:`MapTile <maptile>` component).
* **Tile Path** : the path in the project where the categories are located.
* **Tileset Path** : the path in the project where the tilesets are located.
* **Map Preference Config** : :ref:`Map Preference Config` scriptable object.
* **Map Config** : `MapCreator` config scriptable object.
* **Hotkey Config** : :ref:`hotkey config <Common hotkey config>` scriptable object.
* **Map Creator Tab View** : internal `MapCreator's` tabs view.
* **Map Data Holder** : :ref:`map layer data <Map Data Holder Settings>`.


.. _mapHolder:

**Map Data Holder Settings**
-----------------------

	.. image:: images/gettingstarted/MapHolderTab.png
	
Here are references to the maps and the names of the layers.


**Map Preference Config**
-------------------------

	.. image:: images/gettingstarted/MapPreferenceWindow.png
	
* Common Settings
	* **Tile Size** : default tile size of `MapCreator`.
	* **World Tile Relative Offset** : world offset regarding to the floor of the cell position.
	
* Tool Settings
	* **Show Scene Tool Panel** : displays ``M`` (select `MapCreator`) UI button on the scene view.
	* **Tool Bar Max Count** : the number of category buttons in one row of the toolbar.
	* **Tile Button Size** : the size of the prefab button in `MapCreator's` prefab scroll view.
	* **Has Remove Buttons** : enable buttons to remove prefabs from categories in `MapCreator's` prefab scroll view.
	* **Remove Button Size** : size of remove button.
	* **Buttons Row Count** : the number of prefab buttons in the scroll view in one row.
	* **Prefab Scroll View Height** : height of scroll view of `MapCreator`.
	
* Temp Mesh Settings
	* **Default Draw Mesh Type** : object view type for temporary meshes.
		* **Draw Mesh** : display the temporary mesh object at the end of a render pipeline cycle.
		* **Draw Mesh Now** : the display of the temporary mesh object at the moment.
	* **Apply Allow Color To Objects** : enable custom allow colour for the objects that can be placed.
	* **Allow Mesh Grid Color** : colour of the mesh grid when the object can be placed.
	* **Allow Object Color** : colour of the object that can be placed.
	* **Forbidden Mesh Grid Color** : colour of the object that can't be placed.
	* **Intersection Mesh Grid Color** : colour of the object that intersects another object.
	
* Temp Overlay Mesh Grid Settings
	* **Mesh Surface Offset** : offset from surface to mesh grid.

**Common Settings**
-------------------

	.. image:: images/gettingstarted/CommonSettingsTab.png

* **Show Map Tile Bounds** : display the mesh grid of the object.
* **Draw Grid** : display scene view grid.
* **Always Visible Grid** : the scene view grid is always displayed, regardless of the overlap with other objects.
* **Grid Size** : size of the grid in the scene view.
* **Grid Color** : colour of scene view grid.
* **Async Creation** : async instantiation of the objects.
	* **Create Objects Per Frame** : the number of instantiated objects per frame.
* **Create Prefab Mode:**
	* **Linked prefab** : created object will be linked with source prefab.
	* **Prefab clone** : created object will be cloned from source prefab.
* **Key Rotate Angle** : the angle of rotation of the object by pressing the key (by default `Capslock` key).
* **Show Edit Category Buttons** : show add/remove buttons for category in the `MapCreator` inspector.
* **Show Map Tile Selected Info Tab** : show `MapTile selected info` tab.
* **Show Add New Prefab Tab** : show drag'n'drop prefab box in the `MapCreator` inspector.

.. _hotKeys:

Hotkeys
=======

Common hotkey config
------------------------

	.. image:: images/gettingstarted/HotKeyConfig.png
	
* **Rotate button** : rotate button of the object.
* **Switch sub prefab button** : re-randomize TRS (transform, rotation, scale) or selected objects (if randomize feature is enabled and configured).
* **Action button** : action of the `MapCreator` `edit mode` (for example object spawning).
* **Unselect prefab button** : cancel action or unselect selected temporary prefab.
* **Select default edit mode button** : select :ref:`default <singleMode>` edit mode hotkey.
* **Select brush mode button** : select :ref:`brush <brushMode>` mode hotkey.
* **Select line mode button** : select :ref:`line <lineMode>` mode hotkey.
* **Select area mode button** : select :ref:`area <areaMode>` mode hotkey.
* **Select destroy mode button** : select :ref:`destroy <destroyMode>` mode hotkey.
* **Select tileset mode button** : select :ref:`tileset <tilesetMode>` mode hotkey.
* **Select translate mode button** : select :ref:`translate <translateMode>` mode hotkey.
* **Select template mode button** : select :ref:`template <templateMode>` mode hotkey.
* **Scroll wheel button** : additional action in the `edit mode` using the mouse wheel and the selected key.

Custom hotkey settings
--------------------------

	* **Single mode:**
		* `Ctrl & scroll wheel button` : increasing and decreasing the scale of the object.
	* **Line mode:**
		* **Default:**
			* `Ctrl & scroll wheel button` : increase number of the floors (multi-floor support should be enabled).
		* **Curved:**
			* **Simple line:**
				* `Ctrl & left-mouse click` : add a new segment of the line.
	* **Area mode:**
		* **Default:**
			* `Ctrl & scroll wheel button` : increase number of the floors (multi-floor support should be enabled).
	* **Destroy mode:**
		* **Selection mode:**
			* `Space` : deleting selected objects using the selection box.



