
.. code:: python

    >>> !date 


.. parsed-literal::

    dimanche 12 fvrier 2017, 10:09:31 (UTC+0100)


Description of the propagation environment
==========================================

The ``Layout`` class contains the data structure for describing a
propagation environment. It contains different graphs helping the
implementation of the ray tracing. The class is implemented in the

`layout.py <http://pylayers.github.io/pylayers/modules/pylayers.gis.layout.html>`__

.. code:: python

    >>> from pylayers.gis.layout import *
    >>> from IPython.display import Image
    >>> import os
    >>> %matplotlib inline

Getting the list of all available Layouts : the ``ls()`` method
---------------------------------------------------------------

Creating a default Layout is as simple as :

.. code:: python

    >>> L=Layout()
    >>> L




.. parsed-literal::

    
    ----------------
    Project : /home/uguen/Bureau/P1
    newfile.ini
    Not built 
    Coordinates : cart
    ----------------
    
    Number of points  : 0
    Number of segments  : 0
    Number of sub segments  : 0
    Number of cycles  : 0
    Number of rooms  : 0
    
    xrange :(-50, 50)
    yrange :(-50, 50)
    Segment s in Gs => s_ab coordinates 
    s -> u = self.tgs[s] -> v = self.tahe[:,u] -> s_ab = self.pt[:,v]




Querying the file name associated with the Layout.

.. code:: python

    >>> L._filename




.. parsed-literal::

    'newfile.ini'



The Layout is described in an ``.ini`` file.

The ``ls()`` method lists the layout files which are available in the
``struc`` directory of your current project, which is set up via the
$BASENAME environment variable which should be defined in order PyLayers
find the good directories.

.. code:: python

    >>> L.ls('ini')




.. parsed-literal::

    ['11Dbibli.ini',
     'B11.ini',
     'CORM1.ini',
     'DLR.ini',
     'DLR2.ini',
     'Luebbers.ini',
     'MOCAP-small.ini',
     'MOCAP-small2.ini',
     'MOCAP.ini',
     'MOCAPext.ini',
     'Scene.ini',
     'TA-Office.ini',
     'TA-Office3.ini',
     'TC1_METIS.ini',
     'TC2_METIS.ini',
     'W2PTIN.ini',
     'WHERE1.ini',
     'defdiff.ini',
     'defsthdiff.ini',
     'defstr.ini',
     'edge.ini',
     'klepal.ini',
     'scattering.ini',
     'test.ini']



.. code:: python

    >>> L=Layout('defstr.ini')

.. code:: python

    >>> L




.. parsed-literal::

    
    ----------------
    Project : /home/uguen/Bureau/P1
    defstr.ini : ad95181c1d17466c25e2799901ca1da7
    Built with : ad95181c1d17466c25e2799901ca1da7
    Coordinates : cart
    ----------------
    
    Number of points  : 12
    Number of segments  : 19
    Number of sub segments  : 0
    Number of cycles  : 7
    Number of rooms  : 0
    degree 0 : [-12 -11 -10  -9]
    degree 1 : []
    number of node point of degree 2 : 4
    number of node point of degree 3 : 4
    
    xrange :(757.0, 770.0)
    yrange :(1110.9549999999999, 1116.5450000000001)
    Segment s in Gs => s_ab coordinates 
    s -> u = self.tgs[s] -> v = self.tahe[:,u] -> s_ab = self.pt[:,v]




.. code:: python

    >>> f,a=L.showG('s',nodes=True,slab=True,subseg=True,figsize=(10,10),labels=True)



.. image:: Layout_files/Layout_11_0.png


L.ax provides the boundary of the layout with the following format :
(xmin,xmax,ymin,ymax)

.. code:: python

    >>> L.ax




.. parsed-literal::

    (757.0, 770.0, 1110.9549999999999, 1116.5450000000001)



.. code:: python

    >>> L.build()


.. parsed-literal::

    building Layout ...
    check len(ncycles) == 2
    passed


This Layout is decomposed into convex cycles which are stored in the Gt
graph. The diffraction points are stored in the dictionnary ``L.ddiff``.
The keys of this dictionnary are the diffraction points number and the
values are a zipped list of output cycles and corresponding wedge
angles.

.. code:: python

    >>> L.Gv.node




.. parsed-literal::

    {-6: {},
     -4: {},
     -3: {},
     -1: {},
     1: {},
     2: {},
     3: {},
     4: {},
     5: {},
     6: {},
     7: {},
     8: {},
     9: {},
     10: {},
     11: {},
     17: {},
     21: {},
     27: {},
     30: {}}



.. code:: python

    >>> L.ddiff




.. parsed-literal::

    {-6: ([4, 1], 4.7123889803846897),
     -4: ([6, 4], 4.7123889803846897),
     -3: ([6, 3], 4.7123889803846897),
     -1: ([3, 1], 4.7723171355059337)}



.. code:: python

    >>> L.Gt.node




.. parsed-literal::

    {0: {'hash': 'ad95181c1d17466c25e2799901ca1da7', 'indoor': False},
     1: {'indoor': False,
      'inter': [(15, 1, 0),
       (15, 0, 1),
       (21, 1, 4),
       (21, 4, 1),
       (7, 1),
       (7, 1, 2),
       (7, 2, 1),
       (17, 1, 3),
       (17, 3, 1),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (757.0,1110.955)
      (757.0,1116.545)
      (758.5,1115.9)
      (758.5,1111.6)
      
      vnodes : (-9 15 -12 21 -6 7 -1 17 )},
     2: {'indoor': True,
      'inter': [(1, 2),
       (1, 2, 5),
       (1, 5, 2),
       (2, 2, 5),
       (2, 5, 2),
       (3, 2),
       (3, 2, 5),
       (3, 5, 2),
       (5, 2),
       (5, 2, 5),
       (5, 5, 2),
       (10, 2),
       (10, 2, 3),
       (10, 3, 2),
       (7, 2),
       (7, 2, 1),
       (7, 1, 2),
       (6, 2),
       (6, 2, 4),
       (6, 4, 2),
       (4, 2),
       (4, 2, 5),
       (4, 5, 2),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (763.5,1114.432)
      (763.5,1113.432)
      (763.5,1111.9)
      (758.5,1111.6)
      (758.5,1115.9)
      (763.5,1115.9)
      
      vnodes : (-7 1 2 3 -8 5 -2 10 -1 7 -6 6 -5 4 )},
     3: {'indoor': False,
      'inter': [(11, 3),
       (11, 3, 5),
       (11, 5, 3),
       (27, 3, 6),
       (27, 6, 3),
       (12, 3, 0),
       (12, 0, 3),
       (17, 3, 1),
       (17, 1, 3),
       (10, 3),
       (10, 3, 2),
       (10, 2, 3),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (763.5,1111.9)
      (768.5,1111.9)
      (770.0,1110.955)
      (757.0,1110.955)
      (758.5,1111.6)
      
      vnodes : (-2 11 -3 27 -10 12 -9 17 -1 10 )},
     4: {'indoor': False,
      'inter': [(30, 4, 6),
       (30, 6, 4),
       (9, 4),
       (9, 4, 5),
       (9, 5, 4),
       (6, 4),
       (6, 4, 2),
       (6, 2, 4),
       (21, 4, 1),
       (21, 1, 4),
       (14, 4, 0),
       (14, 0, 4),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (770.0,1116.545)
      (768.5,1115.9)
      (763.5,1115.9)
      (758.5,1115.9)
      (757.0,1116.545)
      
      vnodes : (-11 30 -4 9 -5 6 -6 21 -12 14 )},
     5: {'indoor': True,
      'inter': [(4, 5),
       (4, 5, 2),
       (4, 2, 5),
       (9, 5),
       (9, 5, 4),
       (9, 4, 5),
       (8, 5),
       (8, 5, 6),
       (8, 6, 5),
       (11, 5),
       (11, 5, 3),
       (11, 3, 5),
       (5, 5),
       (5, 5, 2),
       (5, 2, 5),
       (1, 5),
       (1, 5, 2),
       (1, 2, 5),
       (2, 5, 2),
       (2, 2, 5),
       (3, 5),
       (3, 5, 2),
       (3, 2, 5),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (763.5,1114.432)
      (763.5,1115.9)
      (768.5,1115.9)
      (768.5,1111.9)
      (763.5,1111.9)
      (763.5,1113.432)
      
      vnodes : (-7 4 -5 9 -4 8 -3 11 -2 5 -8 1 2 3 )},
     6: {'indoor': False,
      'inter': [(8, 6),
       (8, 6, 5),
       (8, 5, 6),
       (30, 6, 4),
       (30, 4, 6),
       (13, 6, 0),
       (13, 0, 6),
       (27, 6, 3),
       (27, 3, 6),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (768.5,1111.9)
      (768.5,1115.9)
      (770.0,1116.545)
      (770.0,1110.955)
      
      vnodes : (-3 8 -4 30 -11 13 -10 27 )}}



.. code:: python

    >>> L=Layout('DLR.ini')

.. code:: python

    >>> f,a=L.showG('s',aw=False)



.. image:: Layout_files/Layout_20_0.png


To check which are the used slabs :

.. code:: python

    >>> L.sl




.. parsed-literal::

    List of Slabs
    -----------------------------
    
    _AIR : AIR | [0.05]
           white 1
    DOOR : WOOD | [0.05]
           red1 1
    FLOOR : REINFORCED_CONCRETE | [0.05]
           grey40 1
    WALL : BRICK | [0.05]
           grey20 3
    3D_WINDOW_GLASS : GLASS | AIR | GLASS | [0.05, 0.05, 0.05]
           blue3 1
    PARTITION : PLASTER | [0.05]
           grey80 4
    METAL : METAL | [0.05]
           black 4
    AIR : AIR | [0.05]
           white 1
    CEIL : REINFORCED_CONCRETE | [0.05]
           grey20 1




Let's load an other layout. This an indoor office where the FP7 WHERE
project UWB impulse radio measuremnts have been performed.

.. code:: python

    >>> L=Layout('WHERE1.ini')


.. parsed-literal::

    building Layout ...
    check len(ncycles) == 2
    passed


The showG method provides many possible visualization of the layout

.. code:: python

    >>> f,a=L.showG('s',airwalls=False,figsize=(20,10))



.. image:: Layout_files/Layout_26_0.png


.. code:: python

    >>> L=Layout('W2PTIN.ini')


.. parsed-literal::

    It exists degree 1 points : [-80]
    building Layout ...
    check len(ncycles) == 2
    passed



.. image:: Layout_files/Layout_27_1.png


.. code:: python

    >>> f,a = L.showG('s')



.. image:: Layout_files/Layout_28_0.png


The useful numpy arrays of the Layout
-------------------------------------

The layout data structure is a mix between graph and numpy array. numpy
arrays are used when high performance is required while graph structure
is convenient when dealing with different specific tasks. The tricky
thing for the mind is to have to transcode between node index excluding
0 and numpy array index including 0. Below are listed various useful
numpy array which are mostly used internally.

-  tsg : get segment index in Gs from tahe
-  isss : sub-segment index above Nsmax
-  tgs : get segment index in tahe from Gs
-  lsss : list of segments with sub-segment
-  sla : list of all slab names (Nsmax+Nss+1)
-  degree : degree of nodes

``pt`` the array of points
~~~~~~~~~~~~~~~~~~~~~~~~~~

The point coordinates are stored in two different places

-  L.Gs.pos : in a dictionary form (key is the point negative index)
-  L.pt : in a numpy array

.. code:: python

    >>> print np.shape(L.pt)
    >>> print len(filter(lambda x: x<0,L.Gs.pos))


.. parsed-literal::

    (2, 185)
    185


This dual storage is chosen for computational efficiency reason. The
priority goes to the graph and the numpy array is calculated at the end
of the edition in the ``Layout.g2npy`` method (graph to numpy) which is
in charge of the conversion.

tahe (tail-head)
~~~~~~~~~~~~~~~~

``tahe`` is a :math:`(2\times N_{s})` where :math:`N_s` denotes the
number of segment. The first line is the tail index of the segment
:math:`k` and the second line is the head of the segment :math:`k`.
Where :math:`k` is the index of a given segment (starting in 0).

.. code:: python

    >>> L.build()


.. parsed-literal::

    building Layout ...
    check len(ncycles) == 2
    passed


The figure below illustrates a Layout and a superimposition of the graph
of cycles :math:`\mathcal{G}_c`. Those cycles are automatically
extracted from a well defined layout. This concept of **cycles** is
central in the ray determination algorithm which is implemented in
PyLayers. Notice that the exterior region is the cycle indexed by 0. All
the rooms which have a common frontier with the exterior cycle are here
connected to the origin (corresponding to exterior cycle).

.. code:: python

    >>> f,a = L.showG('s')



.. image:: Layout_files/Layout_34_0.png


.. code:: python

    >>> nx.draw_networkx_nodes(L.Gi,L.Gi.pos,node_color='blue',node_size=1)
    >>> nx.draw_networkx_edges(L.Gi,L.Gi.pos,node_color='blue',node_size=1)




.. parsed-literal::

    <matplotlib.collections.LineCollection at 0x7fadde3fedd0>




.. image:: Layout_files/Layout_35_1.png


``tgs`` : trancodage from graph indexing to numpy array indexing
----------------------------------------------------------------

``tgs`` is an array with length :math:`N_s`\ +1. The index 0 is not used
because none segment has 0 as an index.

.. code:: python

    >>> ns = 5
    >>> utahe = L.tgs[ns]

.. code:: python

    >>> tahe =  L.tahe[:,utahe]

.. code:: python

    >>> ptail = L.pt[:,tahe[0]]
    >>> phead = L.pt[:,tahe[1]]

.. code:: python

    >>> print ptail


.. parsed-literal::

    [ 24.574  23.297]


.. code:: python

    >>> print phead


.. parsed-literal::

    [ 24.573  23.19 ]


.. code:: python

    >>> L.Gs.node[5]




.. parsed-literal::

    {'connect': [-165, -163],
     'iso': [],
     'name': 'PARTITION',
     'ncycles': [88, 89],
     'norm': array([-0.99995633,  0.00934539,  0.        ]),
     'offset': 0,
     'transition': False,
     'z': (0, 3.0)}



.. code:: python

    >>> print L.Gs.pos[-8]


.. parsed-literal::

    (29.785, 6.822)


.. code:: python

    >>> aseg = np.array([4,7,134])

.. code:: python

    >>> print np.shape(aseg)


.. parsed-literal::

    (3,)


.. code:: python

    >>> pt  = L.tahe[:,L.tgs[aseg]][0,:]
    >>> ph = L.tahe[:,L.tgs[aseg]][1,:]
    >>> pth = np.vstack((pt,ph))
