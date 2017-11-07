
.. code:: 

    >>> !date 


.. parsed-literal::

    samedi 4 novembre 2017, 10:14:00 (UTC+0100)


Description of the propagation environment
==========================================

The ``Layout`` class contains the data structure for describing a
propagation environment. It contains different graphs helping the
implementation of the ray tracing. The class is implemented in the

`layout.py <http://pylayers.github.io/pylayers/modules/pylayers.gis.layout.html>`__

.. code:: 

    >>> from pylayers.gis.layout import *
    >>> from IPython.display import Image
    >>> import os
    >>> %matplotlib inline

Getting the list of all available Layouts : the ``ls()`` method
---------------------------------------------------------------

Creating an empty Layout is as simple as :

.. code:: 

    >>> L=Layout()
    >>> L




.. parsed-literal::

    
    ----------------
    Project : /home/uguen/Bureau/P1
    
    newfile.lay
    Type : indoor
    Coordinates : cart
    ----------------
    Gs : 0(0/0/0) :0
    Gt : 0 : 0
    Gr : 0 : 0
    ----------------
    
    
    xrange :(-50, 50)
    yrange :(-50, 50)
    Segment s in Gs => s_ab coordinates 
    s2pc : segment to point coordinates (sparse) [p1,p2] = L.s2pc.toarray().reshape(2,2).T 
    s -> u = self.tgs[s] -> v = self.tahe[:,u] -> s_ab = self.pt[:,v]




The different argument of the **init** function are listed below

.. code:: 

    >>> L=Layout(string='',
                     _filematini='matDB.ini',
                     _fileslabini='slabDB.ini',
                     _filefur='',
                     bcheck=True,
                     bbuild=True,
                     bverbose=False,
                     bcartesian=True,
                     dist_m=400,
                     typ='indoor')

-  **string** is either an existing layout filename (.ini,.osm,.res) or
   the coordinates (lat,lon)
-  \*\* \_filematini\*\* is the a material filename material ans slab
   are now described in .lay file
-  \*\* \_fileslabini\*\* is the a slab filename
-  \*\* \_filefur\*\* is the furniture filename
-  \*\* bcheck\*\* is a boolean which force layout integrity checking
-  \*\* bbuild\*\* is a boolean which force rebuilding the layouts
   graphs
-  \*\* bverbose\*\* is a boolean output verbosity
-  \*\* bcartesian\*\* is a boolean controling the type of coordinates
   cartesian or (lat,lon)
-  **dist\_m** is a float value which indicates the zone radius in
   meters for openstreet map extraction
-  **typ** is a string which takes values either 'floorplan' or
   'outdoor'

Querying the file name associated with the Layout.

.. code:: 

    >>> L._filename




.. parsed-literal::

    'newfile.lay'



The Layout is described in an ``.lay`` file, a ``.osm``\ file or a
``.res`` file.

The ``ls()`` method lists the layout files which are available in the
``struc`` directory of your current project, which is set up via the
$BASENAME environment variable which should be defined in order PyLayers
find the good directories.

.. code:: 

    >>> L.ls('lay')




.. parsed-literal::

    ['11Dbibli.lay',
     'B11.lay',
     'CEA2.lay',
     'CEA2_.lay',
     'CORM1.lay',
     'DLR.lay',
     'DLR2.lay',
     'Luebbers.lay',
     'Luebbers_v12.lay',
     'MOCAP-small.lay',
     'MOCAP-small2.lay',
     'MOCAP.lay',
     'MOCAPext.lay',
     'Munich.lay',
     'Munich_buildings.lay',
     'Scene.lay',
     'TA-Office.lay',
     'TA-Office3.lay',
     'TC1_METIS.lay',
     'TC2_METIS.lay',
     'W2PTIN.lay',
     'WHERE1.lay',
     'defdiff.lay',
     'defsthdiff.lay',
     'defstr.lay',
     'edge.lay',
     'espoo.lay',
     'espoo2.lay',
     'espoo3.lay',
     'homeK_vf.lay',
     'klepal.lay',
     'klepal_.lay',
     'klepal__.lay',
     'library_I2_final.lay',
     'office_I1.lay',
     'office_I1_aki_4m.lay',
     'office_I1_final.lay',
     'otakaari5A.lay',
     'otakari.lay',
     'otakari_.lay',
     'scattering.lay',
     'stromberg15GHz.lay',
     'stromberg28GHz.lay',
     'stromberg83GHz.lay',
     'test.lay',
     'test_face.lay',
     'testair0.lay',
     'testair1.lay']



.. code:: 

    >>> L=Layout('defstr.lay')

.. code:: 

    >>> L




.. parsed-literal::

    
    ----------------
    Project : /home/uguen/Bureau/P1
    
    defstr.lay : 5b06adf51ef872a343dfa53c57a587a9
    Type : indoor
    Coordinates : cart
    ----------------
    Gs : 27(12/15/11) :30
    Gt : 0 : 0
    Gr : 0 : 0
    ----------------
    
    degree 0 : [-11 -12 -10  -9]
    degree 1 : []
    number of node point of degree 2 : 4
    number of node point of degree 3 : 4
    
    xrange :(-1.5, 11.5)
    yrange :(-0.75, 5.75)
    Segment s in Gs => s_ab coordinates 
    s2pc : segment to point coordinates (sparse) [p1,p2] = L.s2pc.toarray().reshape(2,2).T 
    s -> u = self.tgs[s] -> v = self.tahe[:,u] -> s_ab = self.pt[:,v]




.. code:: 

    >>> f,a=L.showG('s',
                 nodes=True,
     	     slab=True,
    	     subseg=True,
    	     figsize=(10,10),labels=True)



.. image:: Layout_files/Layout_13_0.png


L.ax provides the boundary of the layout with the following tuple format
: (xmin,xmax,ymin,ymax)

.. code:: 

    >>> L.ax




.. parsed-literal::

    (-1.5, 11.5, -0.75, 5.75)



.. code:: 

    >>> L.build()

A Layout is decomposed into convex cycles which are stored in the Gt
graph. The diffraction points are stored in the dictionnary ``L.ddiff``.
The keys of this dictionnary are the diffraction points number and the
values are a zipped list of output cycles and corresponding wedge
angles.

.. code:: 

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
     22: {},
     28: {},
     30: {}}



.. code:: 

    >>> L.ddiff




.. parsed-literal::

    {-6: ([4, 1], 4.7123889803846897),
     -4: ([6, 4], 4.7123889803846897),
     -3: ([6, 3], 4.7123889803846897),
     -1: ([3, 1], 4.7123889803846897)}



.. code:: 

    >>> L.Gt.node




.. parsed-literal::

    {0: {'hash': '5b06adf51ef872a343dfa53c57a587a9', 'indoor': False},
     1: {'indoor': False,
      'inter': [(15, 1, 0),
       (15, 0, 1),
       (22, 1, 4),
       (22, 4, 1),
       (7, 1),
       (7, 1, 2),
       (7, 2, 1),
       (17, 1, 3),
       (17, 3, 1),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (-1.5,-0.75)
      (-1.5,5.75)
      (0.0,5.0)
      (0.0,0.0)
      
      vnodes : (-9 15 -12 22 -6 7 -1 17 )},
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
      'polyg': (5.0,4.0)
      (5.0,3.0)
      (5.0,0.0)
      (0.0,0.0)
      (0.0,5.0)
      (5.0,5.0)
      
      vnodes : (-7 1 2 3 -8 5 -2 10 -1 7 -6 6 -5 4 )},
     3: {'indoor': False,
      'inter': [(11, 3),
       (11, 3, 5),
       (11, 5, 3),
       (28, 3, 6),
       (28, 6, 3),
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
      'polyg': (5.0,0.0)
      (10.0,0.0)
      (11.5,-0.75)
      (-1.5,-0.75)
      (0.0,0.0)
      
      vnodes : (-2 11 -3 28 -10 12 -9 17 -1 10 )},
     4: {'indoor': False,
      'inter': [(30, 4, 6),
       (30, 6, 4),
       (9, 4),
       (9, 4, 5),
       (9, 5, 4),
       (6, 4),
       (6, 4, 2),
       (6, 2, 4),
       (22, 4, 1),
       (22, 1, 4),
       (14, 4, 0),
       (14, 0, 4),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (11.5,5.75)
      (10.0,5.0)
      (5.0,5.0)
      (0.0,5.0)
      (-1.5,5.75)
      
      vnodes : (-11 30 -4 9 -5 6 -6 22 -12 14 )},
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
      'polyg': (5.0,4.0)
      (5.0,5.0)
      (10.0,5.0)
      (10.0,0.0)
      (5.0,0.0)
      (5.0,3.0)
      
      vnodes : (-7 4 -5 9 -4 8 -3 11 -2 5 -8 1 2 3 )},
     6: {'indoor': False,
      'inter': [(8, 6),
       (8, 6, 5),
       (8, 5, 6),
       (30, 6, 4),
       (30, 4, 6),
       (13, 6, 0),
       (13, 0, 6),
       (28, 6, 3),
       (28, 3, 6),
       (-3,),
       (-4,)],
      'isopen': True,
      'polyg': (10.0,0.0)
      (10.0,5.0)
      (11.5,5.75)
      (11.5,-0.75)
      
      vnodes : (-3 8 -4 30 -11 13 -10 28 )}}



.. code:: 

    >>> L=Layout('DLR.lay')

.. code:: 

    >>> f,a=L.showG('s',aw=False)



.. image:: Layout_files/Layout_22_0.png


To check which are the used slabs :

.. code:: 

    >>> L.sl




.. parsed-literal::

    List of Slabs
    -----------------------------
    
    _AIR : AIR | [0.02]
           white 1
           epr :(1+0j)    sigma : 0.0
    FLOOR : REINFORCED_CONCRETE | [0.1]
           grey40 1
           epr :(8.69999980927+0j)    sigma : 3.0
    WALL : BRICK | [0.07]
           grey20 3
           epr :(4.09999990463+0j)    sigma : 0.300000011921
    3D_WINDOW_GLASS : GLASS | AIR | GLASS | [0.005, 0.005, 0.005]
           blue3 1
           epr :(3.79999995232+0j)    sigma : 0.0
           epr :(1+0j)    sigma : 0.0
           epr :(3.79999995232+0j)    sigma : 0.0
    PARTITION : PLASTER | [0.1]
           grey80 4
           epr :(8+0j)    sigma : 0.038
    CEIL : REINFORCED_CONCRETE | [0.1]
           grey20 1
           epr :(8.69999980927+0j)    sigma : 3.0
    AIR : AIR | [0.02]
           white 1
           epr :(1+0j)    sigma : 0.0




Let's load an other layout. This an indoor office where the FP7 WHERE
project UWB impulse radio measuremnts have been performed.

.. code:: 

    >>> L=Layout('WHERE1.lay')

The showG method provides many possible visualization of the layout

.. code:: 

    >>> f,a=L.showG('s',airwalls=False,figsize=(20,10))



.. image:: Layout_files/Layout_28_0.png


.. code:: 

    >>> L=Layout('W2PTIN.lay')

.. code:: 

    >>> f,a = L.showG('s')



.. image:: Layout_files/Layout_30_0.png


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

.. code:: 

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

.. code:: 

    >>> L.build()

The figure below illustrates a Layout and a superimposition of the graph
of cycles :math:`\mathcal{G}_c`. Those cycles are automatically
extracted from a well defined layout. This concept of **cycles** is
central in the ray determination algorithm which is implemented in
PyLayers. Notice that the exterior region is the cycle indexed by 0. All
the rooms which have a common frontier with the exterior cycle are here
connected to the origin (corresponding to exterior cycle).

.. code:: 

    >>> f,a = L.showG('s')



.. image:: Layout_files/Layout_36_0.png


.. code:: 

    >>> nx.draw_networkx_nodes(L.Gi,L.Gi.pos,node_color='blue',node_size=1)
    >>> nx.draw_networkx_edges(L.Gi,L.Gi.pos,node_color='blue',node_size=1)




.. parsed-literal::

    <matplotlib.collections.LineCollection at 0x7f2acd643a50>




.. image:: Layout_files/Layout_37_1.png


``tgs`` : trancodage from graph indexing to numpy array indexing
----------------------------------------------------------------

``tgs`` is an array with length :math:`N_s`\ +1. The index 0 is not used
because none segment has 0 as an index.

.. code:: 

    >>> ns = 5
    >>> utahe = L.tgs[ns]

.. code:: 

    >>> tahe =  L.tahe[:,utahe]

.. code:: 

    >>> ptail = L.pt[:,tahe[0]]
    >>> phead = L.pt[:,tahe[1]]

.. code:: 

    >>> print ptail


.. parsed-literal::

    [ 29.785   6.822]


.. code:: 

    >>> print phead


.. parsed-literal::

    [ 27.414   6.822]


.. code:: 

    >>> L.Gs.node[5]




.. parsed-literal::

    {'connect': [-8, -139],
     'iso': [5, 435],
     'name': 'PARTITION',
     'ncycles': [70, 72],
     'norm': array([ 0.,  1.,  0.]),
     'offset': 0,
     'transition': False,
     'z': (0, 3.0)}



.. code:: 

    >>> print L.Gs.pos[-8]


.. parsed-literal::

    (29.785, 6.822)


.. code:: 

    >>> aseg = np.array([4,7,134])

.. code:: 

    >>> print np.shape(aseg)


.. parsed-literal::

    (3,)


.. code:: 

    >>> pt  = L.tahe[:,L.tgs[aseg]][0,:]
    >>> ph = L.tahe[:,L.tgs[aseg]][1,:]
    >>> pth = np.vstack((pt,ph))
