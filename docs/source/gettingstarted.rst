Getting started
=====

.. _installation:

Installation
------------

**To use Tile Prefab Placer steps:**

#. Download & import from unity asset store

#. First time initilization window will appear automatically or you can open it manually in toolbar ``604Spirit/MapEditor/Window/Map Creator Initialization``

#. Click `Load Packages` to start downloading required packages for this tool

	.. image:: images/InitilizationWindow.png


	.. note::
		**Required packages:**
		
		* **Editor coroutines** (`com.unity.editorcoroutines`) - unity package allows developers to start constructs similar to Unity’s monobehaviour based coroutines within the editor using abitrary objects.
		
		* **Naughty Atrributes** (`com.dbrizov.naughtyattributes`) - made by Denis Rizov extension for unity inspector, also you can manually download it from unity asset store `Naughty Attributes <https://assetstore.unity.com/packages/tools/utilities/naughtyattributes-129996>`_


#. Select tile 1x1 size to customize tile size of the tool

	.. image:: images/TileInitilization.png


	* Move the 1x1 size of the tile into the field & press show info button

	.. image:: images/TileInitilization2.png

	* Press click set exist config to assign the tile size to the tool


.. _prefabs:


Prefabs
------------

**Category** - it's a prefab set, create categories according to your needs

**How to create categories:**

	.. image:: images/AddCategory1.png

* Click `+` button to start adding category
* Enter category name
* Click `add` button

	.. note::
		To delete a category, select category and click the `-` button

**How to add prefabs:**

	.. image:: images/AddingPrefabs1.png

* Drag & drop desirable prefabs to drop tab

	.. image:: images/AddingPrefabs2.png

* Prefabs are ready to use

	.. note::
		Map tile component is used for the calculation of intersections on the grid, so if you don't need it you can use default game objects


.. _configs:

Configs
------------

**Cached Values Settings**

	.. image:: images/CachedValuesTab.png

* Root
* Default Game Objects Root
* Tile Path
* Tileset Path	
* Map Preference Config
* Map Config
* Hotkey Config
* Map Creator Tab View
* Map Data Holder


**Map Holder Settings**

	.. image:: images/MapHolderTab.png


**Map Preference Config**

	.. image:: images/MapPreferenceWindow.png

* Common Settings
	* Tile Size
	* World Tile Relative Offset
	
* Tool Settings
	* Show Scene Tool Panel
	* Tool Bar Max Count
	* Tile Button Size
	* Has Remove Buttons
	* Remove Button Size
	* Buttons Row Count
	* Prefab Scroll View Height
	
* Temp Mesh Settings
	* Default Draw Mesh Type
	* Apply Allow Color To Objects
	* Allow Mesh Grid Color
	* Allow Object Color
	* Forbidden Mesh Grid Color
	* Intersection Mesh Grid Color


**Hotkey config**

	.. image:: images/HotKeyConfig.png


**Common Settings**

	.. image:: images/CommonSettingsTab.png

* Show Map Tile Bounds
* Draw Grid
* Always Visible Grid
* Grid Size
* Grid Color
* Async Creation
* Create Objects Per Frame
* Create Prefab Mode
* Key Rotate Angle
* Show Edit Category Buttons
* Show Map Tile Selected Info Tab
* Show Add New Prefab Tab



