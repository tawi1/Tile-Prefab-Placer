Getting started
=====

.. _installation:

Installation
------------

To use Tile Prefab Placer steps:

1. Download & import from unity asset store
2. Initilization window will be open automatically first time or you can open it manually in toolbar 
``604Spirit/MapEditor/Window/Map Creator Initialization``

3. Click `Load Packages` to start downloading required packages for this tool
[Image](/images/InitilizationWindow.png)

Required packages:
- Editor coroutine ('com.unity.editorcoroutines')
- Naughty Atrributes ('com.dbrizov.naughtyattributes') made by Denis Rizov extension for unity inspector, 
you can manually download it from unity asset store `Naughty Atrributes <https://assetstore.unity.com/packages/tools/utilities/naughtyattributes-129996>`

4.

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

