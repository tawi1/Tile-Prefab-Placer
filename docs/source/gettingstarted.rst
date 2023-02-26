Getting Started
************

.. contents::
   :local:
   
.. _installation:

Installation
============

`Getting started tutorial <https://youtu.be/Y_LklnjDQ2U>`_

**Steps:**

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
	
#. Set the tile path in the `MapCreator`'s :ref:`cached tab <cachedValues>` where the prefab categories are stored.

	.. image:: images/gettingstarted/CachedValuesTabPrefabPath.png

#. Add your :ref:`prefabs <prefabs>`.
#. Place the desired prefabs on the scene using various :ref:`modes <modes>`.
#. When the scene is finished, if you have used a large number of :ref:`MapTiles <maptile>`, it may be useful to clean up the scene before make build with :ref:`Map Utils <mapUtils>` tool.