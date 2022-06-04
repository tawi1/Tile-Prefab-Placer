Getting started
=====

.. _installation:

Installation
------------

To use Tile Prefab Placer steps:

- Download & import from unity asset store
- Initilization window will be open automatically first time or you can open it manually in toolbar '604Spirit/MapEditor/Window/Map Creator Initilizaiton'

(/images/InitilizationWindow.png)

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

