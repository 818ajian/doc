
.. code:: python

    !date


.. parsed-literal::

    vendredi 24 juin 2016, 09:02:50 (UTC+0200)


Effect of Modifying the Nature of Sub-Segments
==============================================

This notebook illustrates a simple ray tracing simulation with different
material properties for a single segment separating 2 rooms which
contains multi subsegments. The notebook illustrates in details the
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


::


    

    MultipleInstanceErrorTraceback (most recent call last)

    <ipython-input-2-fb5ed322f1e7> in <module>()
          1 from pylayers.simul.link import *
          2 from pylayers.antprop.rays import *
    ----> 3 from pylayers.antprop.aarray import *
          4 from pylayers.antprop.channel import *
          5 from pylayers.gis.layout import *


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/aarray.py in <module>()
          4 import matplotlib.pyplot as plt
          5 import doctest
    ----> 6 import ipdb
          7 
          8 r"""


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__init__.py in <module>()
          5 # https://opensource.org/licenses/BSD-3-Clause
          6 
    ----> 7 from ipdb.__main__ import set_trace, post_mortem, pm, run             # noqa
          8 from ipdb.__main__ import runcall, runeval, launch_ipdb_on_exception  # noqa
          9 


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__main__.py in <module>()
         56     # the instance method will create a new one without loading the config.
         57     # i.e: if we are in an embed instance we do not want to load the config.
    ---> 58     ipapp = TerminalIPythonApp.instance()
         59     shell = get_ipython()
         60     def_colors = shell.colors


    /home/uguen/anaconda2/lib/python2.7/site-packages/traitlets/config/configurable.pyc in instance(cls, *args, **kwargs)
        414             raise MultipleInstanceError(
        415                 'Multiple incompatible subclass instances of '
    --> 416                 '%s are being created.' % cls.__name__
        417             )
        418 


    MultipleInstanceError: Multiple incompatible subclass instances of TerminalIPythonApp are being created.


Let's start by loading a simple layout with 2 single rooms. The multi
subsegment appears in the middle with the red vertical lines. Each
subsegment is materialized by a segment.

.. code:: python

    L=Layout('defstr.ini')
    f,a=L.showG('s',subseg=True,figsize=(10,10))

The studied configuration is composed of a simple 2 rooms building
separated by a subsegment which has a multi subsegment attribute. The
attribute of the subsegment can be changed with the method
```chgmss`` <http://pylayers.github.io/%20pylayers/modules/generated/pylayers.gis.layout.Layout.chgmss.html>`__
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

    building Layout ...


::


    

    MultipleInstanceErrorTraceback (most recent call last)

    <ipython-input-5-de0401164687> in <module>()
    ----> 1 L.build()
          2 L.save()


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4786             if verbose:
       4787                 print "Gv"
    -> 4788             self.buildGv()
       4789             self.lbltg.extend('v')
       4790 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGv(self, show)
       7065                 for idiff in ndiffvalid:
       7066 
    -> 7067                     import ipdb
       7068                     # ipdb.set_trace()
       7069                     # if (icycle==2) & (idiff==-2399):


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__init__.py in <module>()
          5 # https://opensource.org/licenses/BSD-3-Clause
          6 
    ----> 7 from ipdb.__main__ import set_trace, post_mortem, pm, run             # noqa
          8 from ipdb.__main__ import runcall, runeval, launch_ipdb_on_exception  # noqa
          9 


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__main__.py in <module>()
         56     # the instance method will create a new one without loading the config.
         57     # i.e: if we are in an embed instance we do not want to load the config.
    ---> 58     ipapp = TerminalIPythonApp.instance()
         59     shell = get_ipython()
         60     def_colors = shell.colors


    /home/uguen/anaconda2/lib/python2.7/site-packages/traitlets/config/configurable.pyc in instance(cls, *args, **kwargs)
        414             raise MultipleInstanceError(
        415                 'Multiple incompatible subclass instances of '
    --> 416                 '%s are being created.' % cls.__name__
        417             )
        418 


    MultipleInstanceError: Multiple incompatible subclass instances of TerminalIPythonApp are being created.


The :math:`\mathcal{G}_s` graph dictionary has the following structure

.. code:: python

    L.Gs.node




.. parsed-literal::

    {-12: {'ncycles': [5, 6]},
     -11: {'ncycles': [4, 5]},
     -10: {'ncycles': [3, 4]},
     -9: {'ncycles': [3, 6]},
     -8: {'ncycles': [1, 2]},
     -7: {'ncycles': [1, 2]},
     -6: {'ncycles': [2, 5, 6]},
     -5: {'ncycles': [1, 2, 5]},
     -4: {'ncycles': [1, 4, 5]},
     -3: {'ncycles': [1, 3, 4]},
     -2: {'ncycles': [1, 2, 3]},
     -1: {'ncycles': [2, 3, 6]},
     1: {'connect': [-8, -7],
      'name': 'PARTITION',
      'ncycles': [1, 2],
      'norm': array([-1.,  0.,  0.]),
      'offset': 0,
      'ss_name': ['WOOD', 'AIR', 'WOOD'],
      'ss_offset': [0, 0, 0],
      'ss_z': [(0.0, 2.7), (2.7, 2.8), (2.8, 3)],
      'transition': True,
      'z': (0.0, 3.0)},
     2: {'connect': [-8, -2],
      'name': 'WALL',
      'ncycles': [1, 2],
      'norm': array([ 1.,  0.,  0.]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     3: {'connect': [-7, -5],
      'name': 'WALL',
      'ncycles': [1, 2],
      'norm': array([-1.,  0.,  0.]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     4: {'connect': [-6, -1],
      'name': 'WALL',
      'ncycles': [2, 6],
      'norm': array([ 1.,  0.,  0.]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     5: {'connect': [-6, -5],
      'name': 'WALL',
      'ncycles': [2, 5],
      'norm': array([ 0.,  1.,  0.]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     6: {'connect': [-5, -4],
      'name': 'WALL',
      'ncycles': [1, 5],
      'norm': array([ 0.,  1.,  0.]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     7: {'connect': [-4, -3],
      'name': 'WALL',
      'ncycles': [1, 4],
      'norm': array([ 1.,  0.,  0.]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     8: {'connect': [-3, -2],
      'name': 'WALL',
      'ncycles': [1, 3],
      'norm': array([ 0., -1.,  0.]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     9: {'connect': [-1, -2],
      'name': 'WALL',
      'ncycles': [2, 3],
      'norm': array([ 0.05989229, -0.99820485,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': (0.0, 3.0)},
     10: {'connect': [-9, -10],
      'name': '_AIR',
      'ncycles': [3, 0],
      'norm': array([ 0., -1.,  0.]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]},
     11: {'connect': [-10, -11],
      'name': '_AIR',
      'ncycles': [4, 0],
      'norm': array([ 1.,  0.,  0.]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]},
     12: {'connect': [-11, -12],
      'name': '_AIR',
      'ncycles': [5, 0],
      'norm': array([ 0.,  1.,  0.]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]},
     13: {'connect': [-12, -9],
      'name': '_AIR',
      'ncycles': [6, 0],
      'norm': array([ 1.,  0.,  0.]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]},
     16: {'connect': [-1, -9],
      'name': '_AIR',
      'ncycles': [3, 6],
      'norm': array([ 0.70710678, -0.70710678,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]},
     18: {'connect': [-3, -10],
      'name': '_AIR',
      'ncycles': [3, 4],
      'norm': array([ 0.71747829,  0.69658087,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]},
     21: {'connect': [-12, -6],
      'name': '_AIR',
      'ncycles': [5, 6],
      'norm': array([-0.70710678, -0.70710678,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]},
     22: {'connect': [-11, -4],
      'name': '_AIR',
      'ncycles': [4, 5],
      'norm': array([-0.70710678,  0.70710678,  0.        ]),
      'offset': 0,
      'transition': False,
      'z': [0.0, 3.0]}}



We define now two points which are the termination of a radio link.

.. code:: python

    #tx=np.array([759,1114,1.5])
    #rx=np.array([767,1114,1.5])
    tx=np.array([759,1114,1.5])
    rx=np.array([767,1114,1.5])

.. code:: python

    L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])
    L.save()


.. parsed-literal::

    structure saved in  defstr.ini


.. code:: python

    fGHz=np.linspace(1,11,100)
    #Aa = Antenna('S1R1.vsh3')
    #Ab = Antenna('S1R1.vsh3')
    Aa = Antenna('Gauss',fGHz=fGHz)
    Ab = Antenna('Gauss',fGHz=fGHz)
    Ab.eval()
    Aa.eval()
    #Aa = AntArray(N=[8,1,1],fGHz=fGHz)
    #Ab = AntArray(N=[4,1,1],fGHz=fGHz)
    Lk = DLink(L=L,a=tx,b=rx,Aa=Aa,Ab=Ab,fGHz=fGHz,cutoff=5)
    ak,tauk=Lk.eval(force=True,verbose=False)


.. parsed-literal::

    building Layout ...


::


    

    MultipleInstanceErrorTraceback (most recent call last)

    <ipython-input-9-aa04b6c9fa2a> in <module>()
          8 #Aa = AntArray(N=[8,1,1],fGHz=fGHz)
          9 #Ab = AntArray(N=[4,1,1],fGHz=fGHz)
    ---> 10 Lk = DLink(L=L,a=tx,b=rx,Aa=Aa,Ab=Ab,fGHz=fGHz,cutoff=5)
         11 ak,tauk=Lk.eval(force=True,verbose=False)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/simul/link.pyc in __init__(self, **kwargs)
        348         Link.__init__(self)
        349 
    --> 350         defaults={ 'L':Layout(),
        351                    'a':np.array(()),
        352                    'b':np.array(()),


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in __init__(self, _filename, _filematini, _fileslabini, _filefur, force, check, build, verbose)
        422 
        423 
    --> 424         self.load(_filename,build=build)
        425 
        426 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in load(self, _filename, build)
       1624                     # if ans.lower()=='y':
       1625 
    -> 1626                     self.build()
       1627                     self.lbltg.append('s')
       1628                     self.dumpw()


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4786             if verbose:
       4787                 print "Gv"
    -> 4788             self.buildGv()
       4789             self.lbltg.extend('v')
       4790 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGv(self, show)
       7065                 for idiff in ndiffvalid:
       7066 
    -> 7067                     import ipdb
       7068                     # ipdb.set_trace()
       7069                     # if (icycle==2) & (idiff==-2399):


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__init__.py in <module>()
          5 # https://opensource.org/licenses/BSD-3-Clause
          6 
    ----> 7 from ipdb.__main__ import set_trace, post_mortem, pm, run             # noqa
          8 from ipdb.__main__ import runcall, runeval, launch_ipdb_on_exception  # noqa
          9 


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__main__.py in <module>()
         56     # the instance method will create a new one without loading the config.
         57     # i.e: if we are in an embed instance we do not want to load the config.
    ---> 58     ipapp = TerminalIPythonApp.instance()
         59     shell = get_ipython()
         60     def_colors = shell.colors


    /home/uguen/anaconda2/lib/python2.7/site-packages/traitlets/config/configurable.pyc in instance(cls, *args, **kwargs)
        414             raise MultipleInstanceError(
        415                 'Multiple incompatible subclass instances of '
    --> 416                 '%s are being created.' % cls.__name__
        417             )
        418 


    MultipleInstanceError: Multiple incompatible subclass instances of TerminalIPythonApp are being created.


.. code:: python

    ak.shape


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-10-00240c0c276b> in <module>()
    ----> 1 ak.shape
    

    NameError: name 'ak' is not defined


.. code:: python

    plt.stem(tauk,ak[:,0,0])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-11-5c6f3e4c6c80> in <module>()
    ----> 1 plt.stem(tauk,ak[:,0,0])
    

    NameError: name 'tauk' is not defined


A link is the set of a layout and 2 termination points.

.. code:: python

    Aa.eval()
    Aa.plotG()




.. parsed-literal::

    (<matplotlib.figure.Figure at 0x7fcd43bf0bd0>,
     <matplotlib.projections.polar.PolarAxes at 0x7fcd43c77bd0>)



.. code:: python

    Lk.C.Ctt


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-0b62f36fc912> in <module>()
    ----> 1 Lk.C.Ctt
    

    NameError: name 'Lk' is not defined


.. code:: python

    #f,a=Lk.show(rays=True)
    f,a=Lk.show(rays=True,aw=0)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-14-2b2ee2f3162d> in <module>()
          1 #f,a=Lk.show(rays=True)
    ----> 2 f,a=Lk.show(rays=True,aw=0)
    

    NameError: name 'Lk' is not defined


On the figure above, we can see the Tx and Rx each placed in a different
room apart from a wall with a subsegment placed in the middle. Then for
evaluating the radio link, simply type:

.. code:: python

    ak,tauk=Lk.eval(force=True,a=tx,b=rx,applywav=True)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-15-d9efa0c5005d> in <module>()
    ----> 1 ak,tauk=Lk.eval(force=True,a=tx,b=rx,applywav=True)
    

    NameError: name 'Lk' is not defined


.. code:: python

    Lk.C


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-16-08f49e889d34> in <module>()
    ----> 1 Lk.C
    

    NameError: name 'Lk' is not defined


.. code:: python

    f = plt.figure(figsize=(10,10))
    f,a=Lk.C.show(cmap='jet',fig=f,typ='l20',vmin=-120,vmax=-10)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-17-ef1e84aff51a> in <module>()
          1 f = plt.figure(figsize=(10,10))
    ----> 2 f,a=Lk.C.show(cmap='jet',fig=f,typ='l20',vmin=-120,vmax=-10)
    

    NameError: name 'Lk' is not defined


.. code:: python

    fGHz=np.arange(2,6,0.1)
    wav = wvf.Waveform(fcGHz=4,bandGHz=1.5)
    wav.show()

.. code:: python

    Lk = DLink(L=L,a=tx,b=rx,fGHz=fGHz)


.. parsed-literal::

    building Layout ...


::


    

    MultipleInstanceErrorTraceback (most recent call last)

    <ipython-input-19-2f11f76fac43> in <module>()
    ----> 1 Lk = DLink(L=L,a=tx,b=rx,fGHz=fGHz)
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/simul/link.pyc in __init__(self, **kwargs)
        348         Link.__init__(self)
        349 
    --> 350         defaults={ 'L':Layout(),
        351                    'a':np.array(()),
        352                    'b':np.array(()),


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in __init__(self, _filename, _filematini, _fileslabini, _filefur, force, check, build, verbose)
        422 
        423 
    --> 424         self.load(_filename,build=build)
        425 
        426 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in load(self, _filename, build)
       1624                     # if ans.lower()=='y':
       1625 
    -> 1626                     self.build()
       1627                     self.lbltg.append('s')
       1628                     self.dumpw()


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4786             if verbose:
       4787                 print "Gv"
    -> 4788             self.buildGv()
       4789             self.lbltg.extend('v')
       4790 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGv(self, show)
       7065                 for idiff in ndiffvalid:
       7066 
    -> 7067                     import ipdb
       7068                     # ipdb.set_trace()
       7069                     # if (icycle==2) & (idiff==-2399):


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__init__.py in <module>()
          5 # https://opensource.org/licenses/BSD-3-Clause
          6 
    ----> 7 from ipdb.__main__ import set_trace, post_mortem, pm, run             # noqa
          8 from ipdb.__main__ import runcall, runeval, launch_ipdb_on_exception  # noqa
          9 


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__main__.py in <module>()
         56     # the instance method will create a new one without loading the config.
         57     # i.e: if we are in an embed instance we do not want to load the config.
    ---> 58     ipapp = TerminalIPythonApp.instance()
         59     shell = get_ipython()
         60     def_colors = shell.colors


    /home/uguen/anaconda2/lib/python2.7/site-packages/traitlets/config/configurable.pyc in instance(cls, *args, **kwargs)
        414             raise MultipleInstanceError(
        415                 'Multiple incompatible subclass instances of '
    --> 416                 '%s are being created.' % cls.__name__
        417             )
        418 


    MultipleInstanceError: Multiple incompatible subclass instances of TerminalIPythonApp are being created.


.. code:: python

    Lk.a


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-20-7f012f925fcc> in <module>()
    ----> 1 Lk.a
    

    NameError: name 'Lk' is not defined


.. code:: python

    Lk.b


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-21-6142b9bad81d> in <module>()
    ----> 1 Lk.b
    

    NameError: name 'Lk' is not defined


.. code:: python

    cir = Lk.H.applywavB(wav.sf)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-22-74e87499760f> in <module>()
    ----> 1 cir = Lk.H.applywavB(wav.sf)
    

    NameError: name 'Lk' is not defined


.. code:: python

    layer = ['AIR','AIR','AIR']
    Lk.L.chgmss(1,ss_name=layer)
    Lk.L.Gs.node[1]['ss_name']=layer
    Lk.L.g2npy()
    Lk.L.save()
    #Aa = Antenna('Omni',fGHz=fGHz)
    #Aa = Antenna('Omni',fGHz=fGHz)
    ak,tauk=Lk.eval(force=True,verbose=0,fGHz=fGHz)
    #plt.stem(Lk.H.taud,Lk.H.ak)
    #plt.stem(Lk.H.taud,Lk.H.ak[:,0,50])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-23-bd8f84143198> in <module>()
          1 layer = ['AIR','AIR','AIR']
    ----> 2 Lk.L.chgmss(1,ss_name=layer)
          3 Lk.L.Gs.node[1]['ss_name']=layer
          4 Lk.L.g2npy()
          5 Lk.L.save()


    NameError: name 'Lk' is not defined


.. code:: python

    Lk.H.ak.shape


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-24-1ef58d341060> in <module>()
    ----> 1 Lk.H.ak.shape
    

    NameError: name 'Lk' is not defined


.. code:: python

    cirair = Lk.H.applywavB(wav.sf)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-25-c6ef9fd0c1d5> in <module>()
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
    cirmet.plot(typ=['v'],xmin=20,xmax=180)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-26-56144135b207> in <module>()
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
    f,a=cirmet.plot(typ=['l20'],color='r')
    plt.axis([0,120,-120,-40])
    plt.legend(['metal'])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-27-b1089494013d> in <module>()
          1 #fig2=plt.figure()
    ----> 2 f,a=cirair.plot(typ=['l20'],color='b')
          3 plt.axis([0,120,-120,-40])
          4 plt.title('A simple illustration of shadowing effect')
          5 plt.legend(['air'])


    NameError: name 'cirair' is not defined


We have modified successively the nature of the 3 surfaces in the sub
segment placed in the separation partition. The first was AIR, the
second WOOD and the third METAL. As the subsegment is placed on the LOS
path the blockage effect is clearly visible. The chosen antennas were
omni directional ``Antenna('Omni')``

.. code:: python

    Lk.ir.plot(typ='v')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-28-ab27beb5072b> in <module>()
    ----> 1 Lk.ir.plot(typ='v')
    

    NameError: name 'Lk' is not defined

