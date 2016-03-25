
Effect of Modyfiying the Nature of Sub-Segments
===============================================

This notebook illustrates a simple ray tracing simulation with diffeent
material properties for a single segment separating 2 rooms which
contains multi-subsegments. The noteboook illustrates in details the
whole steps.

.. code:: python

    from pylayers.simul.link import *
    from pylayers.antprop.rays import *
    from pylayers.antprop.aarray import *
    from pylayers.antprop.channel import *
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

    L=Layout('defstr.ini')
    f,a=L.showG('s',subseg=True,figsize=(10,10))


::


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-2-ba9e7d1397c8> in <module>()
    ----> 1 L=Layout('defstr.ini')
          2 f,a=L.showG('s',subseg=True,figsize=(10,10))


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in __init__(self, _filename, _filematini, _fileslabini, _filefur, force, check)
        410         # check layout integrity (default)
        411         if check:
    --> 412             self.check()
        413         #self.boundary()
        414 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in check(self, level)
        719             deg0 = filter(lambda x: nx.degree(self.Gs,x)==0,upnt)
        720             deg1 = filter(lambda x: nx.degree(self.Gs,x)==1,upnt)
    --> 721             assert (len(deg0)==0), "It exists degree 0 points :  %r" % deg0
        722             assert (len(deg1)==0), "It exists degree 1 points : %r" % deg1
        723 


    AssertionError: It exists degree 0 points :  [-18, -17, -16, -15, -14]


The studied configuration is composed of a simple 2 rooms building
separated by a subsegment which has a multi subsegment attribute. The
attribute of the subsegment can be changed with the method
```chgmss`` <http://pylayers.github.io/pylayers/modules/generated/pylayers.gis.layout.Layout.chgmss.html>`__
(change multisubsegment). In the example WOOD in the lower part then
10cm of AIR then wood again until the ceiling.

.. code:: python

    L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-5d060b38fe5b> in <module>()
    ----> 1 L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])
    

    NameError: name 'L' is not defined


As the Layout structure has been modified it is required to rebuild the
structure.

.. code:: python

    L.build()
    L.save()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-de0401164687> in <module>()
    ----> 1 L.build()
          2 L.save()


    NameError: name 'L' is not defined


The :math:`\mathcal{G}_s` graph dictionnary has the following structure

.. code:: python

    L.Gs.node


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-ef5d55244e1c> in <module>()
    ----> 1 L.Gs.node
    

    NameError: name 'L' is not defined


We define now two points which are the termination of a radio link.

.. code:: python

    #tx=np.array([759,1114,1.5])
    #rx=np.array([767,1114,1.5])
    tx=np.array([759,1114,1.5])
    rx=np.array([767,1114,1.5])

.. code:: python

    L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])
    L.save()
    fGHz=np.linspace(1,11,100)
    #Aa = Antenna('S1R1.vsh3')
    #Ab = Antenna('S1R1.vsh3')
    #Aa = Antenna('Gauss',fGHz=fGHz)
    #Ab = Antenna('Gauss',fGHz=fGHz)
    Aa = AntArray(N=[8,1,1],fGHz=fGHz)
    Ab = AntArray(N=[4,1,1],fGHz=fGHz)
    Lk = DLink(L=L,a=tx,b=rx,Aa=Aa,Ab=Ab,fGHz=np.linspace(1,11,100))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-fd2986e5b29e> in <module>()
    ----> 1 L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])
          2 L.save()
          3 fGHz=np.linspace(1,11,100)
          4 #Aa = Antenna('S1R1.vsh3')
          5 #Ab = Antenna('S1R1.vsh3')


    NameError: name 'L' is not defined


A link is the set of a layout and 2 termination points.

.. code:: python

    Aa.plotG()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-5cb5df1cbc48> in <module>()
    ----> 1 Aa.plotG()
    

    NameError: name 'Aa' is not defined


.. code:: python

    #f,a=Lk.show(rays=True)
    f,a=Lk.show(rays=True)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-7ecd8f980a4c> in <module>()
          1 #f,a=Lk.show(rays=True)
    ----> 2 f,a=Lk.show(rays=True)
    

    NameError: name 'Lk' is not defined


On the figure above, we can see the Tx and Rx each placed in a different
room appart from a wall with a subsegement placed in the middle. Then
for evaluating the radio link, simply type:


.. code:: python

    ak,tauk=Lk.eval(force=True,a=tx,b=rx,applywav=True)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-d9efa0c5005d> in <module>()
    ----> 1 ak,tauk=Lk.eval(force=True,a=tx,b=rx,applywav=True)
    

    NameError: name 'Lk' is not defined


.. code:: python

    Lk.C


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-08f49e889d34> in <module>()
    ----> 1 Lk.C
    

    NameError: name 'Lk' is not defined


.. code:: python

    f = plt.figure(figsize=(10,10))
    f,a=Lk.C.show(cmap='jet',fig=f,typ='l20',vmin=-120,vmax=-10)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-ef1e84aff51a> in <module>()
          1 f = plt.figure(figsize=(10,10))
    ----> 2 f,a=Lk.C.show(cmap='jet',fig=f,typ='l20',vmin=-120,vmax=-10)
    

    NameError: name 'Lk' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b33fec56690>


.. code:: python

    fGHz=np.arange(2,6,0.5)
    wav = wvf.Waveform(fcGHz=4,bandGHz=1.5)
    wav.show()



.. image:: Multisubsegments_files/Multisubsegments_22_0.png


.. code:: python

    wav.st.y.shape




.. parsed-literal::

    (1, 251)



.. code:: python

    len(Lk.fGHz)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-00ef4b2c8627> in <module>()
    ----> 1 len(Lk.fGHz)
    

    NameError: name 'Lk' is not defined


.. code:: python

    Lk = DLink(L=L,a=tx,b=rx)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-8ec0715e9a54> in <module>()
    ----> 1 Lk = DLink(L=L,a=tx,b=rx)
    

    NameError: name 'L' is not defined


.. code:: python

    Lk.a


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-7f012f925fcc> in <module>()
    ----> 1 Lk.a
    

    NameError: name 'Lk' is not defined


.. code:: python

    Lk.b


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-6142b9bad81d> in <module>()
    ----> 1 Lk.b
    

    NameError: name 'Lk' is not defined


.. code:: python

    cir = Lk.H.applywavB(wav.sf)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-74e87499760f> in <module>()
    ----> 1 cir = Lk.H.applywavB(wav.sf)
    

    NameError: name 'Lk' is not defined


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
    plt.stem(Lk.H.taud,Lk.H.ak[:,0,50])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-ae5fc4f64f59> in <module>()
          1 layer = ['AIR','AIR','AIR']
    ----> 2 Lk.L.chgmss(1,ss_name=layer)
          3 Lk.L.Gs.node[1]['ss_name']=layer
          4 Lk.L.g2npy()
          5 Lk.L.save()


    NameError: name 'Lk' is not defined


.. code:: python

    Lk.H.ak.shape


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-21-1ef58d341060> in <module>()
    ----> 1 Lk.H.ak.shape
    

    NameError: name 'Lk' is not defined


.. code:: python

    cirair = Lk.H.applywavB(wav.sf)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-22-c6ef9fd0c1d5> in <module>()
    ----> 1 cirair = Lk.H.applywavB(wav.sf)
    

    NameError: name 'Lk' is not defined


.. code:: python

    layer = ['METAL','METAL','METAL']
    Lk.L.chgmss(1,ss_name=layer)
    Lk.L.Gs.node[1]['ss_name']=layer
    Lk.L.g2npy()
    Lk.L.save()
    Lk.eval(force=True)
    cirmet = Lk.H.applywavB(wav.sf)
    cirmet.plot(typ=['v'],xmin=20,xmax=80)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-02ef6687144f> in <module>()
          1 layer = ['METAL','METAL','METAL']
    ----> 2 Lk.L.chgmss(1,ss_name=layer)
          3 Lk.L.Gs.node[1]['ss_name']=layer
          4 Lk.L.g2npy()
          5 Lk.L.save()


    NameError: name 'Lk' is not defined


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


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-24-e1d90729636b> in <module>()
          1 #fig2=plt.figure()
    ----> 2 f,a=cirair.plot(typ=['l20'],color='b')
          3 plt.axis([0,120,-120,-40])
          4 plt.title('A simple illustration of shadowing effect')
          5 plt.legend(['air'])


    NameError: name 'cirair' is not defined


We have modified successively the nature of the 3 surfaces in the sub
segment placed in the sepataion partition. The first was AIR, the second
WOOD and the third METAL. As the subsegment is placed on the LOS path
the blockage effect is clearly visible. The chosen antennas were
omnidirectional ``Antenna('Omni')``
