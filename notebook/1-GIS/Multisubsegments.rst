
Effect of Modyfiying the Nature of Sub-Segments
===============================================

This notebook illustrtates a simple ray tracing simulation with
diffecent material properties for a single segment separating 2 rooms
which contains multi-subsegments. The noteboook illustrates in details
the whole steps.

.. code:: python

    from pylayers.simul.link import *
    from pylayers.antprop.rays import *
    from pylayers.gis.layout import *
    from pylayers.antprop.signature import *
    import pylayers.signal.bsignal as bs
    import pylayers.signal.waveform as wvf
    from pylayers.simul.simulem import *
    import matplotlib.pyplot as plt
    %matplotlib inline


.. parsed-literal::

    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


Let start by loading a simple layout with 2 single rooms. The multi
subsegment appears in the middle with the red vertical lines. Each
subsegment is materialized by a segment.

.. code:: python

    L=Layout('defstr3.ini')
    f,a=L.showG('s',subseg=True,figsize=(10,10))



.. image:: Multisubsegments_files/Multisubsegments_4_0.png


The studied configuration is composed of a simple 2 rooms building
separated by a subsegment which has a multi subsegment attribute. The
attribute of the subsegment can be changed with the method
```chgmss`` <http://pylayers.github.io/pylayers/modules/generated/pylayers.gis.layout.Layout.chgmss.html>`__
(change multisubsegment). In the example WOOD in the lower part then
10cm of AIR then wood again until the ceiling.

.. code:: python

    L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])

As the Layout structure has been modified it is required to rebuild the
structure.

.. code:: python

    L.build()
    L.save()


.. parsed-literal::

    structure saved in  defstr3.str2
    structure saved in  defstr3.ini


The :math:`\mathcal{G}_s` graph dictionnary has the following structure

.. code:: python

    L.Gs.node




.. parsed-literal::

    {-8: {},
     -7: {},
     -6: {},
     -5: {},
     -4: {},
     -3: {},
     -2: {},
     -1: {},
     1: {'connect': [-8, -7],
      'name': 'PARTITION',
      'ncycles': [1, 2],
      'norm': array([-0.999982  , -0.00599989,  0.        ]),
      'offset': 0,
      'ss_name': ['WOOD', 'AIR', 'WOOD'],
      'ss_offset': [0, 0, 0],
      'ss_z': [(0.0, 2.7), (2.7, 2.8), (2.8, 3)],
      'transition': True,
      'z': (0.0, 3.0)},
     2: {'connect': [-8, -2],
      'name': 'WALL',
      'ncycles': [1, 2],
      'norm': array([ 0.99997778,  0.00666652,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     3: {'connect': [-7, -5],
      'name': 'WALL',
      'ncycles': [1, 2],
      'norm': array([-0.99997775, -0.00667097,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     4: {'connect': [-6, -1],
      'name': 'WALL',
      'ncycles': [2, 0],
      'norm': array([ 0.99997888,  0.00649986,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     5: {'connect': [-6, -5],
      'name': 'WALL',
      'ncycles': [2, 0],
      'norm': array([-0.00619988,  0.99998078,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     6: {'connect': [-5, -4],
      'name': 'WALL',
      'ncycles': [1, 0],
      'norm': array([-0.00639987,  0.99997952,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     7: {'connect': [-4, -3],
      'name': 'WALL',
      'ncycles': [1, 0],
      'norm': array([ 0.99997887,  0.00650149,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     8: {'connect': [-3, -2],
      'name': 'WALL',
      'ncycles': [1, 0],
      'norm': array([ 0.00639987, -0.99997952,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     9: {'connect': [-1, -2],
      'name': 'WALL',
      'ncycles': [2, 0],
      'norm': array([-0.00639987,  0.99997952,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)}}



We define now two points which are the termination of a radio link.

.. code:: python

    tx=np.array([759,1114,1.5])
    rx=np.array([767,1114,1.5])

.. code:: python

    L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])
    L.save()
    fGHz=np.linspace(1,11,100)
    #Aa = Antenna('S1R1.vsh3')
    #Ab = Antenna('S1R1.vsh3')
    Aa = Antenna('Omni',fGHz=fGHz)
    Ab = Antenna('Omni',fGHz=fGHz)
    Lk = DLink(L=L,a=tx,b=rx,Aa=Aa,Ab=Ab,fGHz=np.linspace(1,11,100))


.. parsed-literal::

    structure saved in  defstr3.str2
    structure saved in  defstr3.ini


A link is the set of a layout and 2 termination points.

.. code:: python

    f,a=Lk.show()



.. image:: Multisubsegments_files/Multisubsegments_15_0.png


On the figure above, we can see the Tx and Rx each placed in a different
room appart from a wall with a subsegement placed in the middle. Then
for evaluating the radio link, simply type:

.. code:: python

    ak,tauk=Lk.eval(force=True,a=tx,b=rx)


.. parsed-literal::

    checkh5
    Start Signatures
    algo 7
    Signatures'> from 2_1_3 saved
    Stop signature 0.0472140312195
    Start Rays
    Rays'> from 3_2_1 saved
    Stop rays 0.546607017517
    Ctilde'> from 2_1_0 saved
    Tchannel'> from 2_1_0_0_0_0_0 saved


At that point the channel has been evaluated and all the data stored in
an ``hdf5`` file

Link members
------------

The Signature of the radio channel is in ``Lk.Si``, the 3D rays are in
``Lk.R``, the propagation channel is in ``Lk.C`` and the transmission
channel is in ``Lk.H``

.. code:: python

    Lk.R




.. parsed-literal::

    Rays3D
    ----------
    1 / 1 : [0]
    2 / 6 : [1 2 3 4 5 6]
    3 / 19 : [ 7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25]
    4 / 40 : [26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
     51 52 53 54 55 56 57 58 59 60 61 62 63 64 65]
    5 / 46 : [ 66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83
      84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99 100 101
     102 103 104 105 106 107 108 109 110 111]
    6 / 28 : [112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129
     130 131 132 133 134 135 136 137 138 139]
    -----
    ni : 628
    nl : 1396




.. code:: python

    Lk.C




.. parsed-literal::

    Ctilde
    ---------
    (140, 100)
    Nray : 140
    fmin(GHz) : 1.0
    fmax(GHz): 11.0
    Nfreq : 100



.. code:: python

    f = plt.figure(figsize=(10,10))
    f,a=Lk.C.show(cmap='jet',fig=f,typ='l20',vmin=-120,vmax=-10)



.. image:: Multisubsegments_files/Multisubsegments_23_0.png


.. code:: python

    fGHz=np.arange(2,6,0.5)
    wav = wvf.Waveform(fcGHz=4,bandGHz=1.5)
    wav.show()



.. image:: Multisubsegments_files/Multisubsegments_24_0.png


.. code:: python

    wav.st.y.shape




.. parsed-literal::

    (1, 251)



.. code:: python

    len(Lk.fGHz)




.. parsed-literal::

    100



.. code:: python

    Lk = DLink(L=L,a=tx,b=rx)

.. code:: python

    Lk.a




.. parsed-literal::

    array([  759. ,  1114. ,     1.5])



.. code:: python

    Lk.b




.. parsed-literal::

    array([  767. ,  1114. ,     1.5])



.. code:: python

    cir = Lk.H.applywavB(wav.sf)

.. code:: python

    layer = ['AIR','AIR','AIR']
    Lk.L.chgmss(1,ss_name=layer)
    Lk.L.Gs.node[1]['ss_name']=layer
    Lk.L.g2npy()
    Lk.L.save()
    fGHz=np.linspace(2,11,181)
    #Aa = Antenna('Omni',fGHz=fGHz)
    #Aa = Antenna('Omni',fGHz=fGHz)
    ak,tauk=Lk.eval(force=True)
    plt.stem(Lk.H.taud,Lk.H.ak)


.. parsed-literal::

    structure saved in  defstr3.str2
    structure saved in  defstr3.ini
    checkh5
    Start Signatures
    algo 7
    Signatures'> from 2_1_3 saved
    Stop signature 0.0257730484009
    Start Rays
    Rays'> from 3_2_1 saved
    Stop rays 0.311182022095
    Ctilde'> from 2_1_0 saved
    Tchannel'> from 2_1_0_0_0_2_2 saved




.. parsed-literal::

    <Container object of 3 artists>




.. image:: Multisubsegments_files/Multisubsegments_31_2.png


.. code:: python

    cirair = Lk.H.applywavB(wav.sf)

.. code:: python

    cirair.plot(typ=['v'],xmin=20,xmax=80)




.. parsed-literal::

    (<matplotlib.figure.Figure at 0x2b73a37a9950>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x2b73a37b2050>]], dtype=object))




.. image:: Multisubsegments_files/Multisubsegments_33_1.png


.. code:: python

    layer = ['PARTITION','PARTITION','PARTITION']
    Lk.L.chgmss(1,ss_name=layer)
    Lk.L.Gs.node[1]['ss_name']=layer
    Lk.L.g2npy()
    Lk.L.save()
    Lk.eval(force=True)
    cirpart = Lk.H.applywavB(wav.sf)
    cirpart.plot(typ=['v'],xmin=20,xmax=80)


.. parsed-literal::

    structure saved in  defstr3.str2
    structure saved in  defstr3.ini
    checkh5
    Start Signatures
    algo 7
    Signatures'> from 2_1_3 saved
    Stop signature 0.0452868938446
    Start Rays
    Rays'> from 3_2_1 saved
    Stop rays 0.529342889786
    Ctilde'> from 2_1_0 saved
    Tchannel'> from 2_1_0_0_0_2_2 saved




.. parsed-literal::

    (<matplotlib.figure.Figure at 0x2b73a300e150>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x2b73a8818090>]], dtype=object))




.. image:: Multisubsegments_files/Multisubsegments_34_2.png


.. code:: python

    layer = ['METAL','METAL','METAL']
    Lk.L.chgmss(1,ss_name=layer)
    Lk.L.Gs.node[1]['ss_name']=layer
    Lk.L.g2npy()
    Lk.L.save()
    Lk.eval(force=True)
    cirmet = Lk.H.applywavB(wav.sf)
    cirmet.plot(typ=['v'],xmin=20,xmax=80)


.. parsed-literal::

    structure saved in  defstr3.str2
    structure saved in  defstr3.ini
    checkh5
    Start Signatures
    algo 7
    Signatures'> from 2_1_3 saved
    Stop signature 0.0311608314514
    Start Rays
    Rays'> from 3_2_1 saved
    Stop rays 0.318943977356
    Ctilde'> from 2_1_0 saved
    Tchannel'> from 2_1_0_0_0_2_2 saved




.. parsed-literal::

    (<matplotlib.figure.Figure at 0x2b73a876e410>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x2b73a3764b50>]], dtype=object))




.. image:: Multisubsegments_files/Multisubsegments_35_2.png


.. code:: python

    #fig2=plt.figure()
    f,a=cirair.plot(typ=['l20'],color='b')
    plt.axis([0,120,-120,-40])
    plt.title('A simple illustration of shadowing effect')
    plt.legend(['air'])
    f,a=cirpart.plot(typ=['l20'],color='k')
    plt.axis([0,120,-120,-40])
    plt.legend(['wood'])
    f,a=cirmet.plot(typ=['l20'],color='r')
    plt.axis([0,120,-120,-40])
    plt.legend(['metal'])




.. parsed-literal::

    <matplotlib.legend.Legend at 0x2b73a2802510>




.. image:: Multisubsegments_files/Multisubsegments_36_1.png



.. image:: Multisubsegments_files/Multisubsegments_36_2.png



.. image:: Multisubsegments_files/Multisubsegments_36_3.png


We have modified successively the nature of the 3 surfaces in the sub
segment placed in the sepataion partition. The first was AIR, the second
WOOD and the third METAL. As the subsegment is placed on the LOS path
the blockage effect is clearly visible. The chosen antennas were
omnidirectional ``Antenna('Omni')``
