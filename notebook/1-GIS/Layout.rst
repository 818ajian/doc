
.. code:: python

    >>> !date 


.. parsed-literal::

    mardi 10 mai 2016, 21:55:44 (UTC+0200)


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


.. parsed-literal::

    Layout:Mayavi is not installed


Getting the list of all available Layouts : the ``ls()`` method
---------------------------------------------------------------

Creating a default Layout is as simple as :

.. code:: python

    >>> L=Layout()
    >>> L




.. parsed-literal::

    
    ----------------
    defstr.ini
    ----------------
    
    Number of points  : 12
    Number of segments  : 17
    Number of sub segments  : 3
    Number of cycles  : 7
    Number of rooms  : 2
    degree 0 : [-12 -11 -10  -9]
    degree 1 : []
    number of node point of degree 2 : 6
    number of node point of degree 3 : 2
    
    xrange :(748.5, 778.5)
    yrange :(1101.9, 1125.9)
    
    Useful dictionnaries
    ----------------
    dca {cycle : []} cycle with an airwall
    sl {slab name : slab dictionary}
    name :  {slab :seglist} 
    
    Useful arrays
    ----------------
    pt : numpy array of points 
    normal : numpy array of normal 
    offset : numpy array of offset 
    tsg : get segment index in Gs from tahe
    isss :  sub-segment index above Nsmax
    tgs : get segment index in tahe from self.Gs
    upnt : get point id index from self.pt
    iupnt : get point index in self.pt from point id  
    lsss : list of segments with sub-segment
    sla : list of all slab names (Nsmax+Nss+1)
    degree : degree of nodes 



Querying the file name associated with the Layout

.. code:: python

    >>> L.filename




.. parsed-literal::

    'defstr.ini'



The Layout is described in an ``.ini`` file.

The ``ls()`` method lists the layout files which are available in the
``struc`` directory of your current project, which is set up via the
$BASENAME environment variable which should be defined in order PyLayers
find the good directories.

.. code:: python

    >>> L.ls('ini')




.. parsed-literal::

    ['11Dbibli.ini',
     'CORM1.ini',
     'DLR-bug.ini',
     'DLR.ini',
     'DLR2.ini',
     'Jimmy.ini',
     'Luebbers.ini',
     'MOCAP-small.ini',
     'MOCAP-small2.ini',
     'MOCAP.ini',
     'MOCAPext.ini',
     'NYU.ini',
     'Scene.ini',
     'TA-Office.ini',
     'TA-Office_sauv.ini',
     'TC1_METIS.ini',
     'W2PTIN.ini',
     'WHERE1.ini',
     'WHERE1_sauv.ini',
     'convexity.ini',
     'defdiff.ini',
     'defsthdiff.ini',
     'defstr.ini',
     'defstr3.ini',
     'edge.ini',
     'klepal.ini',
     'nonconvex.ini',
     'scattering.ini',
     'square.ini',
     'test.ini']



.. code:: python

    >>> L=Layout('defstr.ini')

.. code:: python

    >>> L




.. parsed-literal::

    
    ----------------
    defstr.ini
    ----------------
    
    Number of points  : 12
    Number of segments  : 17
    Number of sub segments  : 3
    Number of cycles  : 7
    Number of rooms  : 2
    degree 0 : [-12 -11 -10  -9]
    degree 1 : []
    number of node point of degree 2 : 6
    number of node point of degree 3 : 2
    
    xrange :(748.5, 778.5)
    yrange :(1101.9, 1125.9)
    
    Useful dictionnaries
    ----------------
    dca {cycle : []} cycle with an airwall
    sl {slab name : slab dictionary}
    name :  {slab :seglist} 
    
    Useful arrays
    ----------------
    pt : numpy array of points 
    normal : numpy array of normal 
    offset : numpy array of offset 
    tsg : get segment index in Gs from tahe
    isss :  sub-segment index above Nsmax
    tgs : get segment index in tahe from self.Gs
    upnt : get point id index from self.pt
    iupnt : get point index in self.pt from point id  
    lsss : list of segments with sub-segment
    sla : list of all slab names (Nsmax+Nss+1)
    degree : degree of nodes 



.. code:: python

    >>> f,a=L.showG('s',nodes=True,slab=True,subseg=True,figsize=(10,10),labels=True)



.. image:: Layout_files/Layout_11_0.png


L.ax provides the boundary of the layout with the following format :
(xmin,xmax,ymin,ymax)

.. code:: python

    >>> L.ax




.. parsed-literal::

    (748.5, 778.5, 1101.9, 1125.9)



.. code:: python

    >>> L.build()

L.ma is the polygon mask of the layout

.. code:: python

    >>> L.ma




.. image:: Layout_files/Layout_16_0.svg



This Layout has several convex cycles which are stored in the Gt graph.
The diffraction points are stored in a dictionnary L.ddiff. The keys of
this diction-nary are the diffraction points and the values are both the
list of output cycles and the corresponding wedge angles.

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
     16: {},
     17: {},
     20: {},
     21: {}}



.. code:: python

    >>> L.ddiff




.. parsed-literal::

    {-6: ([3, 4], 4.7123889803846897),
     -4: ([4, 5], 4.7123889803846897),
     -3: ([5, 6], 4.7123889803846897),
     -1: ([3, 6], 4.7123889803846897)}



.. code:: python

    >>> L.Gt.node




.. parsed-literal::

    {0: {'indoor': False},
     1: {'cycle': cycle nstr[-8  2 -2  8 -3  7 -4  6 -5  3 -7  1]
      point number 6
      segment number 6
      area : 20.0
      centroid : [  766.   1113.9],
      'indoor': True,
      'inter': [(1, 1),
       (1, 1, 2),
       (1, 2, 1),
       (3, 1),
       (3, 1, 2),
       (3, 2, 1),
       (6, 1),
       (6, 1, 4),
       (6, 4, 1),
       (7, 1),
       (7, 1, 5),
       (7, 5, 1),
       (8, 1),
       (8, 1, 6),
       (8, 6, 1),
       (2, 1),
       (2, 1, 2),
       (2, 2, 1),
       (-3,),
       (-1,)],
      'isopen': False,
      'polyg': (763.5,1113.432)
      (763.5,1114.432)
      (763.5,1115.9)
      (768.5,1115.9)
      (768.5,1111.9)
      (763.5,1111.9)
      
      vnodes : (-8 1 -7 3 -5 6 -4 7 -3 8 -2 2 )},
     2: {'cycle': cycle nstr[-8  2 -2  9 -1  4 -6  5 -5  3 -7  1]
      point number 6
      segment number 6
      area : -20.0
      centroid : [  761.   1113.9],
      'indoor': True,
      'inter': [(1, 2),
       (1, 2, 1),
       (1, 1, 2),
       (2, 2),
       (2, 2, 1),
       (2, 1, 2),
       (9, 2),
       (9, 2, 6),
       (9, 6, 2),
       (4, 2),
       (4, 2, 3),
       (4, 3, 2),
       (5, 2),
       (5, 2, 4),
       (5, 4, 2),
       (3, 2),
       (3, 2, 1),
       (3, 1, 2),
       (-3,),
       (-1,)],
      'isopen': False,
      'polyg': (763.5,1114.432)
      (763.5,1113.432)
      (763.5,1111.9)
      (758.5,1111.9)
      (758.5,1115.9)
      (763.5,1115.9)
      
      vnodes : (-7 1 -8 2 -2 9 -1 4 -6 5 -5 3 )},
     3: {'cycle': cycle nstr[ -6  20 -12  13  -9  16  -1   4]
      point number 4
      segment number 4
      area : 140.0
      centroid : [  752.30952381  1113.9       ],
      'indoor': False,
      'inter': [(4, 3),
       (4, 3, 2),
       (4, 2, 3),
       (16, 3, 6),
       (16, 6, 3),
       (13, 3, 0),
       (13, 0, 3),
       (20, 3, 4),
       (20, 4, 3),
       (-3,),
       (-1,)],
      'isopen': True,
      'polyg': (758.5,1115.9)
      (758.5,1111.9)
      (748.5,1101.9)
      (748.5,1125.9)
      
      vnodes : (-6 4 -1 16 -9 13 -12 20 )},
     4: {'cycle': cycle nstr[ -6  20 -12  12 -11  21  -4   6  -5   5]
      point number 5
      segment number 5
      area : -200.0
      centroid : [  763.5         1121.73333333],
      'indoor': False,
      'inter': [(5, 4),
       (5, 4, 2),
       (5, 2, 4),
       (20, 4, 3),
       (20, 3, 4),
       (12, 4, 0),
       (12, 0, 4),
       (21, 4, 5),
       (21, 5, 4),
       (6, 4),
       (6, 4, 1),
       (6, 1, 4),
       (-3,),
       (-1,)],
      'isopen': True,
      'polyg': (763.5,1115.9)
      (758.5,1115.9)
      (748.5,1125.9)
      (778.5,1125.9)
      (768.5,1115.9)
      
      vnodes : (-5 5 -6 20 -12 12 -11 21 -4 6 )},
     5: {'cycle': cycle nstr[ -4  21 -11  11 -10  17  -3   7]
      point number 4
      segment number 4
      area : -140.0
      centroid : [  774.69047619  1113.9       ],
      'indoor': False,
      'inter': [(7, 5),
       (7, 5, 1),
       (7, 1, 5),
       (21, 5, 4),
       (21, 4, 5),
       (11, 5, 0),
       (11, 0, 5),
       (17, 5, 6),
       (17, 6, 5),
       (-3,),
       (-1,)],
      'isopen': True,
      'polyg': (768.5,1111.9)
      (768.5,1115.9)
      (778.5,1125.9)
      (778.5,1101.9)
      
      vnodes : (-3 7 -4 21 -11 11 -10 17 )},
     6: {'cycle': cycle nstr[ -3  17 -10  10  -9  16  -1   9  -2   8]
      point number 5
      segment number 5
      area : -200.0
      centroid : [  763.5         1106.06666667],
      'indoor': False,
      'inter': [(8, 6),
       (8, 6, 1),
       (8, 1, 6),
       (17, 6, 5),
       (17, 5, 6),
       (10, 6, 0),
       (10, 0, 6),
       (16, 6, 3),
       (16, 3, 6),
       (9, 6),
       (9, 6, 2),
       (9, 2, 6),
       (-3,),
       (-1,)],
      'isopen': True,
      'polyg': (763.5,1111.9)
      (768.5,1111.9)
      (778.5,1101.9)
      (748.5,1101.9)
      (758.5,1111.9)
      
      vnodes : (-2 8 -3 17 -10 10 -9 16 -1 9 )}}



.. code:: python

    >>> L=Layout('DLR.ini')

.. code:: python

    >>> f,a=L.showG('s',aw=False)



.. image:: Layout_files/Layout_22_0.png


To check which are the used slabs :

.. code:: python

    >>> Slabs = np.unique(L.sla)
    >>> for s in Slabs:
    >>>     if s in L.sl:
               print L.sl[s]


.. parsed-literal::

    3D_WINDOW_GLASS : GLASS | AIR | GLASS | [0.005, 0.005, 0.005]
    
    AIR : AIR | [0.02]
    
    DOOR : WOOD | [0.03]
    
    METAL : METAL | [0.1]
    
    PARTITION : PLASTER | [0.1]
    
    WALL : BRICK | [0.07]
    


Let's load an other layout. This an indoor office where the FP7 WHERE
project UWB impulse radio measuremnts have been performed.

.. code:: python

    >>> L=Layout('WHERE1.ini')

The showG method provides many possible visualization of the layout

.. code:: python

    >>> f,a=L.showG('s',airwalls=False,figsize=(20,10))



.. image:: Layout_files/Layout_28_0.png


.. code:: python

    >>> L=Layout('W2PTIN.ini')

.. code:: python

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

.. code:: python

    >>> print np.shape(L.pt)
    >>> print len(filter(lambda x: x<0,L.Gs.pos))


.. parsed-literal::

    (2, 189)
    189


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

The figure below illustrates a Layout and a superimposition of the graph
of cycles :math:`\mathcal{G}_c`. Those cycles are automatically
extracted from a well defined layout. This concept of **cycles** is
central in the ray determination algorithm which is implemented in
PyLayers. Notice that the exterior region is the cycle indexed by 0. All
the rooms which have a common frontier with the exterior cycle are here
connected to the origin (corresponding to exterior cycle).

.. code:: python

    >>> f,a = L.showG('s')



.. image:: Layout_files/Layout_36_0.png


.. code:: python

    >>> nx.draw_networkx_nodes(L.Gi,L.Gi.pos,node_color='blue',node_size=1)
    >>> nx.draw_networkx_edges(L.Gi,L.Gi.pos,node_color='blue',node_size=1)




.. parsed-literal::

    <matplotlib.collections.LineCollection at 0x2b5519c26d90>




.. image:: Layout_files/Layout_37_1.png


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

    [ 29.785   6.822]


.. code:: python

    >>> print phead


.. parsed-literal::

    [ 27.414   6.822]


.. code:: python

    >>> L.Gs.node[5]




.. parsed-literal::

    {'connect': [-8, -139],
     'name': 'PARTITION',
     'ncycles': [8, 9],
     'norm': array([ 0., -1.,  0.]),
     'offset': 0,
     'transition': False,
     'z': (0, 3.0)}



.. code:: python

    >>> print L.Gs.pos[-8]
    >>> print L.Gs.pos[-139]


.. parsed-literal::

    (29.785, 6.822)
    (27.414, 6.822)


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

.. code:: python

    >>> np.shape(pth)




.. parsed-literal::

    (2, 3)



``Layout.seg2pts`` a function for getting points coordinates from segment number array
--------------------------------------------------------------------------------------

.. code:: python

    >>> L.seg2pts(aseg)




.. parsed-literal::

    array([[ 29.785,   0.044,  22.538],
           [  6.822,  23.078,   8.711],
           [ 29.785,  -3.754,  20.326],
           [  8.921,  23.078,   8.693]])



.. code:: python

    >>> aseg = array(filter(lambda x: x>0,L.Gs.nodes()))
    >>> pth = L.seg2pts(aseg)

.. code:: python

    >>> from pylayers.util.plotutil import displot

.. code:: python

    >>> displot(pth[0:2,:],pth[2:,:])
    >>> plt.axis('off')




.. parsed-literal::

    (-20.0, 50.0, -20.0, 50.0)




.. image:: Layout_files/Layout_54_1.png

