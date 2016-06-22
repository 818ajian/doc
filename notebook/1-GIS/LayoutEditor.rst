
The Layout class
----------------

Introduction
~~~~~~~~~~~~

This section explains the main features of the **Layout** class.

A Layout is a representation of a floorplan, it is handled by the module
**pylayers.gis.layout**.

This module recognizes different file formats including geo-referenced
files in open street map format ``.osm``.

Using osm allows to take advantage of a mature floor plan editor *JOSM*
with the plugin *PicLayer*. This is well described in
http://wiki.openstreetmap.org/wiki/IndoorOSM

The ``pylayers.gis.osmparser`` module parses ``osm`` files.

See the following methods of the layout object

-  ``loadosm()``
-  ``saveosm()``

Structure of a Layout
~~~~~~~~~~~~~~~~~~~~~

At first a Layout is described by a set of points (negative index) and a
set of segments (positive index).

Points and segments are nodes of the :math:`\mathcal{G}_s` graph.

It is required to respect a strict non overlapping rule. **No segments
can recover partially or totally an other segment**.

This rule allows to capture topological relations of the network which
are exploited for further analysis.

Subsegments
~~~~~~~~~~~

To describe doors and windows, the concept of ``subsegment`` is
introduced.

A ``segment`` has attributes :

-  ``name`` : slab name
-  ``z`` : tuple of minimum and maximum heights with respect to ground
   (meters)
-  ``transition`` : a boolean indicating if a human can cross this
   segment. For example, segments associated with a door are transition
   segments but we will see later that it may be judicious to split
   space with transparent segments which have the name 'AIR'. Those
   segments are also ``transition=True``

A ``subsegment`` belongs to a ``segment``, it has mainly 2 attached
parameters :

-  ``ss_name`` : subsegment slab name
-  ``ss_z`` : [(zmin1,zmax1),(zmin2,zmax2),...,(zminK,zmaxK))] list of
   minimum and maximum height of associated subsegments (meters)

When appearing in a 3D ray a subsegment should have a unique index
different from the segment index.

The different layout format
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The layout format has regularly evolved over time and is going to evolve
again. Currently, the different recognized file extensions are the
following :

-  ``.str2``: a ASCII file (Node list + edge list)
-  ``.str`` : a binary file which includes visibility relations between
   point and segments
-  ``.ini`` : an ini file which gather node list and edge list as well
   as the state of the current ``display`` dictionnary
-  ``.osm`` : an xml file which can be edited with
   `JOSM <http://josm.openstreetmap.de/>`__

.. code:: python

    >>> from pylayers.gis.layout import *
    >>> from pylayers.util.project import *
    >>> %matplotlib inline


.. parsed-literal::

    Layout:Mayavi is not installed


Reading an exiting Layout
~~~~~~~~~~~~~~~~~~~~~~~~~

To read an existing layout it is sufficient to create a Layout object
with, as an argument, a file name with one of the recognized extension.
All files are stored in the ``pstruc['DIRSTRUC']`` directory of the
project. The project root directory is defined in the ``$BASENAME``
environment variable.

.. code:: python

    >>> print pstruc['DIRSTRUC']
    struc/str


.. parsed-literal::

    struc/str


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-ec9ba75a5513> in <module>()
          1 print pstruc['DIRSTRUC']
    ----> 2 struc/str
    

    NameError: name 'struc' is not defined


``pstruc`` is a dictionnary which gathers all directories which are used
in ``PyLayers``

.. code:: python

    >>> pstruc




.. parsed-literal::

    {'DIRANT': 'ant',
     'DIRBODY': 'body',
     'DIRC3D': 'body/c3d',
     'DIRCIR': 'output',
     'DIRCT': 'output/Ct',
     'DIRFUR': 'struc/furnitures',
     'DIRGEOM': 'geom',
     'DIRGIS': 'gis',
     'DIRH': 'output/H',
     'DIRIMAGE': 'struc/images',
     'DIRINI': 'struc/ini',
     'DIRLCH': 'output',
     'DIRLNK': 'output',
     'DIRMAT': 'ini',
     'DIRMAT2': 'ini',
     'DIRMES': 'meas',
     'DIRNETSAVE': 'netsave',
     'DIROOSM': 'gis/osm',
     'DIROSM': 'struc/osm',
     'DIRPICKLE': 'struc/gpickle',
     'DIRR2D': 'output/r2d',
     'DIRR3D': 'output/r3d',
     'DIRSIG': 'output/sig',
     'DIRSIMUL': 'ini',
     'DIRSLAB': 'ini',
     'DIRSLAB2': 'ini',
     'DIRSTRUC': 'struc/str',
     'DIRSTRUC2': 'struc/str',
     'DIRTRA': 'output',
     'DIRTUD': 'output',
     'DIRTx': 'output/Tx001',
     'DIRWEAR': 'body/wear',
     'DIRWRL': 'struc/wrl'}



The structure of the ``.osm`` file is shown below

.. code:: python

    >>> %%bash
        cd $BASENAME/struc
        ls *.osm



.. parsed-literal::

    convexity.osm
    Jimmy.osm
    nonconvex.osm


.. code:: python

    >>> %%bash
         cd $BASENAME/struc
         head DLR.osm
         echo '---'
         tail -17 DLR.osm


.. parsed-literal::

    ---


.. parsed-literal::

    head: impossible d'ouvrir «DLR.osm» en lecture: Aucun fichier ou dossier de ce type
    tail: impossible d'ouvrir «DLR.osm» en lecture: Aucun fichier ou dossier de ce type


To read a new layout in osm format :

.. code:: python

    >>> L=Layout('DLR.ini')

.. code:: python

    >>> fig,ax=L.showGs()



.. image:: LayoutEditor_files/LayoutEditor_11_0.png


.. code:: python

    >>> L.info()


.. parsed-literal::

    filestr :  DLR.ini
    filematini :  matDB.ini
    fileslabini :  slabDB.ini
    filegeom :  DLR.off
    boundaries  (-10.505, 42.586, -18.277, 18.878)
    number of Points : 109
    number of Segments : 138
    number of Sub-Segments : 30
    Gs Nodes :  247
    Gs Edges :  276
    Gt Nodes :  31
    Gt Edges :  79
    vnodes = Gt.node[Nc]['cycles'].cycle 
    poly = Gt.node[Nc]['cycle'].polyg 
    Gr Nodes    : 21
    Gr Edges    : 21
    Nc  = Gr.node[nroom]['cycles']  


The different graphs associated with the layout are then built

.. code:: python

    >>> L.build()


::


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-9-63002b766909> in <module>()
    ----> 1 L.build()
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4682             if verbose:
       4683                 print "Gr"
    -> 4684             self.buildGr()
       4685             self.lbltg.extend('r')
       4686 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGr(self)
       8783                     pass
       8784                 else:
    -> 8785                     self.Gr.remove_node(cy)
       8786                     self.Gr.pos.pop(cy)
       8787 


    /home/uguen/anaconda/lib/python2.7/site-packages/networkx/classes/graph.pyc in remove_node(self, n)
        569             raise NetworkXError("The node %s is not in the graph." % (n,))
        570         for u in nbrs:
    --> 571             del adj[u][n]   # remove all edges n-u in graph
        572         del adj[n]          # now remove node
        573 


    KeyError: 13


The topological graph :math:`\mathcal{G}_t` or graph of non overlapping
cycles.

.. code:: python

    >>> f,a=L.showG('t')
    >>> b=plt.axis('off')



.. image:: LayoutEditor_files/LayoutEditor_16_0.png


The graph of room :math:`\mathcal{G}_r`. Two rooms which share at least
a wall are connected. Two rooms which share only a corner (punctual
connection) are not connected

.. code:: python

    >>> f,a=L.showG('r')
    >>> b=plt.axis('off')


::


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-11-691b11b3fe3c> in <module>()
    ----> 1 f,a=L.showG('r')
          2 b=plt.axis('off')


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in showG(self, graph, **kwargs)
       7769             else:
       7770                 kwargs['labels']=False
    -> 7771             fig,ax = gru.draw(G,**kwargs)
       7772             kwargs['fig']=fig
       7773             kwargs['ax']=ax


    /home/uguen/Documents/rch/devel/pylayers/pylayers/util/graphutil.pyc in draw(G, **kwargs)
        157                                width = kwargs['width'],
        158                                arrows= kwargs['arrows'],
    --> 159                                alpha = kwargs['alphae'],ax=ax)
        160         if kwargs['airwalls']:
        161             try:


    /home/uguen/anaconda/lib/python2.7/site-packages/networkx/drawing/nx_pylab.pyc in draw_networkx_edges(G, pos, edgelist, width, edge_color, style, alpha, edge_cmap, edge_vmin, edge_vmax, ax, arrows, label, **kwds)
        513 
        514     # set edge positions
    --> 515     edge_pos = numpy.asarray([(pos[e[0]], pos[e[1]]) for e in edgelist])
        516 
        517     if not cb.iterable(width):


    KeyError: 0



.. image:: LayoutEditor_files/LayoutEditor_18_1.png


The graph of waypath :math:`\mathcal{G}_w`. This graph is used for agent
mobility. This allows to determine the shortest path between 2 rooms.
This information could be included in the osm file. This is not the case
yet

.. code:: python

    >>> f,a=L.showG('w')
    >>> b=plt.axis('off')



.. image:: LayoutEditor_files/LayoutEditor_20_0.png


The graph of visibility :math:`\mathcal{G_v}`

.. code:: python

    >>> f,a=L.showG('v')
    >>> b=plt.axis('off')



.. image:: LayoutEditor_files/LayoutEditor_22_0.png


The graph of interactions :math:`\mathcal{G}_i` used to determine the
ray signatures.

.. code:: python

    >>> f=plt.figure(figsize=(15,15))
    >>> a = f.gca()
    >>> f,a=L.showG('i',fig=f,ax=a)
    >>> b= plt.axis('off')



.. image:: LayoutEditor_files/LayoutEditor_24_0.png


The display options dictionnary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> L.info()


.. parsed-literal::

    filestr :  DLR.ini
    filematini :  matDB.ini
    fileslabini :  slabDB.ini
    filegeom :  DLR.off
    boundaries  (-10.505, 42.586, -18.277, 18.878)
    number of Points : 109
    number of Segments : 138
    number of Sub-Segments : 30
    Gs Nodes :  247
    Gs Edges :  276
    Gt Nodes :  31
    Gt Edges :  140
    vnodes = Gt.node[Nc]['cycles'].cycle 
    poly = Gt.node[Nc]['cycle'].polyg 
    Gr Nodes    : 26
    Gr Edges    : 114
    Nc  = Gr.node[nroom]['cycles']  


The layout can be displayed using matplotlib plotting primitive. Several
display options are specified in the display dictionary. Those options
are exploited in ``showGs()`` visualization method.

.. code:: python

    >>> L.display




.. parsed-literal::

    {'activelayer': 'WALL',
     'alpha': 0.5,
     'box': (-10.505, 42.586, -18.277, 18.878),
     'clear': True,
     'edges': True,
     'edlabel': False,
     'edlblsize': 20,
     'ednodes': True,
     'fontsize': 10,
     'layer': [],
     'layers': ['WALL', 'PARTITION', 'AIR', 'WINDOW_GLASS', '3D_WINDOW_GLASS'],
     'layerset': ['WINDOW_GLASS',
      'PLASTERBOARD_7CM',
      'WALL',
      'AIR',
      'WINDOW',
      'METALIC',
      'PLASTERBOARD_14CM',
      'DOOR',
      'FLOOR',
      'METAL',
      'PARTITION',
      'CONCRETE_20CM3D',
      'PLASTERBOARD_10CM',
      'CEIL',
      'CONCRETE_6CM3D',
      'CONCRETE_15CM3D',
      '3D_WINDOW_GLASS',
      'WALLS',
      'WOOD',
      'CONCRETE_7CM3D',
      'PILLAR',
      'ABSORBENT'],
     'ndlabel': False,
     'ndlblsize': 20,
     'ndsize': 10,
     'nodes': True,
     'overlay': False,
     'overlay_axis': [-6.571295099826252,
      38.37510026097863,
      -11.339789148099044,
      11.170751733658253],
     'overlay_file': 'DLR4991.png',
     'overlay_flip': '',
     'scaled': True,
     'subseg': True,
     'subsegnb': True,
     'thin': False,
     'ticksoff': True,
     'title': 'Init',
     'transition': True,
     'visu': False}



Layers
^^^^^^

-  'layer' : list , []
-  'layerset',list, list of available layers
-  'layers', list , []
-  'activelayer', str , 'WINDOW\_GLASS'
-  'alpha', float , 0.5 , overlay transparency
-  'box', tuple , (-20,20,-10,10), (xmin xmax,ymin,ymax)

Strings
^^^^^^^

-  'title' : str , 'Init'
-  'fileoverlay' : str , 'TA-Office.png'

Sizes
^^^^^

-  'fontsize', float , 10
-  'ndsize', float , 10
-  'ndlblsize' : float 20
-  'edlblsize' : float , 20

Booleans
^^^^^^^^

-  'edlabel', boolean, False
-  'ticksoff',boolean, True
-  'scaled' : boolean , True
-  'subseg' : boolean , True
-  'nodes', boolean , True
-  'visu', boolean , False
-  'edges', boolean , True
-  'clear', boolean, False
-  'overlay', boolean , False
-  'thin', boolean , False , If True trace all segments with thickness 1
-  'ndlabel',boolean, If True display node labels
-  'ednodes', boolean, True

Interactive Editor
~~~~~~~~~~~~~~~~~~

The command L.editor() launches an interactive editor. The state machine
is implemented in module ``pylayers.gis.selectl.py``.

To have an idea of all available options, look in the

```pylayers.gis.SelectL`` <http://pylayers.github.io/pylayers/_modules/pylayers/gis/selectl.html#SelectL.new_state>`__
module

PyLayers comes along with a low level structure editor based on
``matplotlib`` which can be invoked using the ``editor()`` method. This
editor is more suited for modifying constitutive properties of walls. In
the future a dedicated plugin in ``JOSM`` could be a much better
solution.

There are two different modes of edition

-  A create points mode CP

.. code:: python

    + left clic   : free point
    + right clic  : same x point
    + center clic : same y point


::


      File "<ipython-input-17-3fbadf730daa>", line 1
        + left clic   : free point
                  ^
    SyntaxError: invalid syntax



-  A create segments mode

   -  left clic : select point 1
   -  left clic : select point 2
   -  left clic : create a segment between point 1 and point 2

**m** : to switch from one mode to an other

**i** : to return to init state

Image overlay
^^^^^^^^^^^^^

It is useful while editing a layout to have an overlay of an image in
order to help placing points. The image overlay can either be an url or
a filename. In that case the file is stored in

.. code:: python

    >>> L=Layout()
    >>> L.display['fileoverlay']='http://images.wikia.com/theoffice/images/9/9e/Layout.jpg'

.. code:: python

    >>> L.display['overlay']=True
    >>> L.display['alpha']=1
    >>> L.display['scaled']=False
    >>> L.display['ticksoff']=False
    >>> L.display['inverse']=True

.. code:: python

    >>> plt.figure(figsize=(10,10))
    >>> L.showGs()




.. parsed-literal::

    (<matplotlib.figure.Figure at 0x2abb60121a50>,
     <matplotlib.axes._subplots.AxesSubplot at 0x2abb6077b790>)




.. parsed-literal::

    <matplotlib.figure.Figure at 0x2abb60121910>



.. image:: LayoutEditor_files/LayoutEditor_34_2.png


Scaling the figure overlay
^^^^^^^^^^^^^^^^^^^^^^^^^^

Before going further it is necessary :

-  to place the global origin
-  to precise the vertical and horizontal scale of the image

This is done by the following commands :

-  'i' : back to init state
-  'm' : goes to CP state
-  'o' : define the origin
-  'left click' on the point of the figure chasen as the origin
-  'left click' on a point at a known distance from the origin along x
   axis. Fill the dialog box with the actual distance (expressed in
   meters) between the two points.
-  'left click' on a point at a known distance from the origin along y
   axis. Fill the dialog box with the actual distance (expressed in
   meters) between the two points.

In that sequence of operation it is useful to rescale the figure with
'r'.

At that stage, it is possible to start creating points

.. code:: python

    'b'  : selct a segment
    'l'  : select activelayer
    'i'  : back to init state
    'e'  : edit segment
    't'  : translate  structure
    'h'  : add subsegment
    'd'  : delete subsegment
    'r'  : refresh
    'o'  : toggle overlay
    'm'  : toggle mode (point or segment)
    'z'  : change display parameters
    'q'  : quit interactive mode
    'x'  : save .str2 file
    'w'  : display all layers


::


      File "<ipython-input-21-f38a305b0b72>", line 1
        'b'  : selct a segment
             ^
    SyntaxError: invalid syntax



Vizualisation of the layout
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    >>> L = Layout('TA-Office.ini')
    >>> L.dumpr()
    >>> fig = plt.figure(figsize=(25,25))
    >>> ax = fig.gca()
    >>> fig,ax = L.showG(fig=fig,ax=ax,graph='s',labels=True,font_size=9,node_size=220,node_color='c')
    >>> a = plt.axis('off')



.. image:: LayoutEditor_files/LayoutEditor_38_0.png


Each node of :math:`\mathcal{G}_s` with a negative index is a point.

Each node of :math:`\mathcal{G}_s` with a positive index corresponds to
a segment (wall,door,window,...).

The segment name is the key of the **slab** dictionnary.

`Multi Subsegments <./Multisubsegments.html>`__
