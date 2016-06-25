
Slabs and Materials
===================

.. code:: python

    >>> %matplotlib inline

A slab is a set ol several layers of materials with specified thickness.
Slabs are used to describe properties of the different constitutive
elements of a building such as wall, windows ,...

In practice when describing a specific building, it is necessary to
specify a set of different slabs with different characteristics.

The structure which gathers this set is ``SlabDB``. If no file argument
is given, this structure is initialized with the default file:
`slabDB.ini <https://github.com/pylayers/pylayers/blob/master/data/ini/slabDB.ini>`__

This section demonstrates some features of the ``pylayers.antprop.slab``
module.

.. code:: python

    >>> from pylayers.antprop.slab import *

The Class ``SlabDB`` contains a dictionnary of all available Slabs. This
information is read in the file ``slabDB.ini`` of the current project
pointed by environment variable ``$BASENAME``

.. code:: python

    >>> S = SlabDB()


::


    

    NoSectionErrorTraceback (most recent call last)

    <ipython-input-3-cb2f70fe64c2> in <module>()
    ----> 1 S = SlabDB()
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in __init__(self, filemat, fileslab, ds, dm)
       1895         self.fileslab = fileslab
       1896         if ds=={}:
    -> 1897             self.mat = MatDB()
       1898             if (filemat != ''):
       1899                 self.mat.load(filemat)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in __init__(self, _fileini, dm)
        865         self.filemat = self.fileini.replace('.ini','.mat')
        866         if dm=={}:
    --> 867             self.load(_fileini)
        868         else:
        869             #self.update(dm)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in load(self, _fileini)
       1110         config.read(fileini)
       1111 
    -> 1112         di = dict(config.items("dict") )
       1113 
       1114         self.di={}


    /home/uguen/anaconda2/lib/python2.7/ConfigParser.pyc in items(self, section, raw, vars)
        640         except KeyError:
        641             if section != DEFAULTSECT:
    --> 642                 raise NoSectionError(section)
        643         # Update with the entry specific variables
        644         if vars:


    NoSectionError: No section: 'dict'


A SlabDB is a dictionnary, the keys are for the current file are shown
below

.. code:: python

    >>> S.keys()
    ['WINDOW_GLASS',
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
     'ABSORBENT']


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-4-26f2383d1d12> in <module>()
    ----> 1 S.keys()
          2 ['WINDOW_GLASS',
          3  'PLASTERBOARD_7CM',
          4  'WALL',
          5  'AIR',


    NameError: name 'S' is not defined


Defining a new Slab and a new Material
--------------------------------------

.. code:: python

    >>> S.add('slab2',['STONE'],[0.15])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-5-fae06e1f2f1e> in <module>()
    ----> 1 S.add('slab2',['STONE'],[0.15])
    

    NameError: name 'S' is not defined


.. code:: python

    >>> S.mat['STONE']
    {'epr': (8.69999980927+0j),
     'index': 8,
     'mur': (1+0j),
     'name': 'STONE',
     'roughness': 0.0,
     'sigma': 3.0}


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-6-bdc2ac8a5a7c> in <module>()
    ----> 1 S.mat['STONE']
          2 {'epr': (8.69999980927+0j),
          3  'index': 8,
          4  'mur': (1+0j),
          5  'name': 'STONE',


    NameError: name 'S' is not defined


.. code:: python

    >>> S['slab2']['lmatname']
    ['STONE']


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-7-945e339e663d> in <module>()
    ----> 1 S['slab2']['lmatname']
          2 ['STONE']


    NameError: name 'S' is not defined


.. code:: python

    >>> S['slab2']['lthick']
    [0.15]


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-8-915148531a85> in <module>()
    ----> 1 S['slab2']['lthick']
          2 [0.15]


    NameError: name 'S' is not defined


.. code:: python

    >>> fGHz= np.arange(3,5,0.01)
    >>> theta = np.arange(0,np.pi/2,0.01)
    >>> S['slab2'].ev(fGHz,theta)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-9-3c345a0cc4dd> in <module>()
          1 fGHz= np.arange(3,5,0.01)
          2 theta = np.arange(0,np.pi/2,0.01)
    ----> 3 S['slab2'].ev(fGHz,theta)
    

    NameError: name 'S' is not defined


.. code:: python

    >>> fig = plt.figure(figsize=(10,10))
    >>> S['slab2'].pcolor()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-10-6d2006d41c5d> in <module>()
          1 fig = plt.figure(figsize=(10,10))
    ----> 2 S['slab2'].pcolor()
    

    NameError: name 'S' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fac6988e250>


.. code:: python

    >>> A=S['slab2']


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-11-345b32278613> in <module>()
    ----> 1 A=S['slab2']
    

    NameError: name 'S' is not defined


As any PyLayers object there is an help function for remembering which
methods are implemented in the class.

.. code:: python

    >>> A.help()
    clear: D.clear() -> None.  Remove all items from D.
    conv:  build lmat and thick
    copy: D.copy() -> a shallow copy of D
    editgui:  edit a Slab in the DB
    ev:  evaluation of the Slab
    excess_grdelay:  calculate transmission excess delay in ns
    filter:  filtering waveform
    fromkeys: dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
    get: D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    has_key: D.has_key(k) -> True if D has a key k, else False
    help:  generic help
    info:  display Slab Info
    items: D.items() -> list of D's (key, value) pairs, as 2-tuples
    iteritems: D.iteritems() -> an iterator over the (key, value) items of D
    iterkeys: D.iterkeys() -> an iterator over the keys of D
    itervalues: D.itervalues() -> an iterator over the values of D
    keys: D.keys() -> list of D's keys
    loss0:  calculate loss for theta=0 at frequency (fGHz)
    losst:  Calculate loss w.r.t angle and frequency
    pcolor:  display of R & T coefficients wrt frequency an angle
    plotwrt:  plot R & T coefficients with respect to angle or frequency
    pop: D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    popitem: D.popitem() -> (k, v), remove and return some (key, value) pair as a
    setdefault: D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    show:  show slab Reflection and Transmission coefficient
    tocolor:   convert slab properrties into a color
    update: D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    values: D.values() -> list of D's values
    viewitems: D.viewitems() -> a set-like object providing a view on D's items
    viewkeys: D.viewkeys() -> a set-like object providing a view on D's keys
    viewvalues: D.viewvalues() -> an object providing a view on D's values


::


      File "<ipython-input-12-754c57e015f9>", line 2
        clear: D.clear() -> None.  Remove all items from D.
             ^
    SyntaxError: invalid syntax



Information necessary to define a Slab
--------------------------------------

Each slab contains informations about its constitutive materials
electromagnetic properties.

Below an example for a simple slab, constituted with a single material
slab. The slab 'WOOD' is a layer of 4cm 'WOOD' material.

.. code:: python

    >>> S['WOOD']['lmatname']
    ['WOOD']


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-01d0a1d5effb> in <module>()
    ----> 1 S['WOOD']['lmatname']
          2 ['WOOD']


    NameError: name 'S' is not defined


thickness is expressed in meters

.. code:: python

    >>> S['WOOD']['lthick']
    [0.04]


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-14-9c080e318609> in <module>()
    ----> 1 S['WOOD']['lthick']
          2 [0.04]


    NameError: name 'S' is not defined


.. code:: python

    >>> S['WOOD']['color']
    'maroon'


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-15-12f410f1cfa0> in <module>()
    ----> 1 S['WOOD']['color']
          2 'maroon'


    NameError: name 'S' is not defined


.. code:: python

    >>> S['WOOD']['linewidth']
    2


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-16-c8eb7fc48345> in <module>()
    ----> 1 S['WOOD']['linewidth']
          2 2


    NameError: name 'S' is not defined


Multi layers Slab, using different stacks of materials can be easily
defined using the two lists **lmatname** and **lthick**.

    Notice the adopted convention naming lists starting with letter 'l'
    and dictionnaries starting with letter 'd'

.. code:: python

    >>> S['3D_WINDOW_GLASS']['lmatname']
    ['GLASS', 'AIR', 'GLASS']


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-17-11579d70aa70> in <module>()
    ----> 1 S['3D_WINDOW_GLASS']['lmatname']
          2 ['GLASS', 'AIR', 'GLASS']


    NameError: name 'S' is not defined


.. code:: python

    >>> S['3D_WINDOW_GLASS']['lthick']
    [0.005, 0.005, 0.005]


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-18-eb06d9183ef7> in <module>()
    ----> 1 S['3D_WINDOW_GLASS']['lthick']
          2 [0.005, 0.005, 0.005]


    NameError: name 'S' is not defined


For each constitutive material of a slab, their electromagnetic
properties can be obtained as:

.. code:: python

    >>> S['3D_WINDOW_GLASS']['lmat']
    [{'epr': (3.79999995232+0j),
      'index': 4,
      'mur': (1+0j),
      'name': 'GLASS',
      'roughness': 0.0,
      'sigma': 0.0},
     {'epr': (1+0j),
      'index': 1,
      'mur': (1+0j),
      'name': 'AIR',
      'roughness': 0.0,
      'sigma': 0.0},
     {'epr': (3.79999995232+0j),
      'index': 4,
      'mur': (1+0j),
      'name': 'GLASS',
      'roughness': 0.0,
      'sigma': 0.0}]


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-19-b5c81e9090d0> in <module>()
    ----> 1 S['3D_WINDOW_GLASS']['lmat']
          2 [{'epr': (3.79999995232+0j),
          3   'index': 4,
          4   'mur': (1+0j),
          5   'name': 'GLASS',


    NameError: name 'S' is not defined


Evaluation of a Slab
--------------------

Each Slab can be evaluated to obtain the Transmission and Reflexion
coefficients for

-  a given frequency range
-  a given incidence angle range (:math:`0\le\theta<\frac{\pi}{2}`)

.. code:: python

    >>> fGHz = np.arange(3,5,0.01)
    >>> theta = np.arange(0,np.pi/2,0.01)
    >>> 
    >>> S['WOOD'].ev(fGHz,theta,compensate=True)
    >>> sR = np.shape(S['WOOD'].R)
    >>> print '\nHere, slab is evaluted for',sR[0],'frequency(ies)', 'and',sR[1], 'angle(s)\n'
    
    Here, slab is evaluted for 200 frequency(ies) and 158 angle(s)


::


      File "<ipython-input-20-f80213024988>", line 8
        Here, slab is evaluted for 200 frequency(ies) and 158 angle(s)
                                 ^
    SyntaxError: invalid syntax



Transmission and Reflexion coefficients
---------------------------------------

Reflexion and transmission coefficient are computed for the given
frequency range and theta range

.. code:: python

    >>> ifreq=1
    >>> ithet=10
    >>> 
    >>> print '\nReflection coefficient @',fGHz[ifreq],'GHz and theta=',theta[ithet],':\n\n R=',S['WOOD'].R[0,0]
    >>> print '\nTransmission coefficient @',fGHz[ifreq],'GHz and theta=',theta[ithet],':\n\n T=',S['WOOD'].T[0,0],'\n'
    
    Reflection coefficient @ 3.01 GHz and theta= 0.1 :
    
     R= [[-0.39396205-0.17289585j  0.00000000+0.j        ]
     [ 0.00000000+0.j          0.39396205+0.17289585j]]
    
    Transmission coefficient @ 3.01 GHz and theta= 0.1 :
    
     T= [[-0.17594898-0.86927604j -0.00000000+0.j        ]
     [-0.00000000+0.j         -0.17594898-0.86927604j]]


::


      File "<ipython-input-21-0832af7bd288>", line 7
        Reflection coefficient @ 3.01 GHz and theta= 0.1 :
                             ^
    SyntaxError: invalid syntax



Ploting Reflection and Transmission Coefficients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The method ``plotwrt`` can plot the different calculated coefficients
with respect to angle or frequency.

.. code:: python

    >>> S['WOOD']['lthick']=[0.02]
    >>> S['WOOD'].ev()
    >>> S['WOOD'].ev()
    >>> f,a=S['WOOD'].plotwrt()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-22-54d2566bd9cd> in <module>()
    ----> 1 S['WOOD']['lthick']=[0.02]
          2 S['WOOD'].ev()
          3 S['WOOD'].ev()
          4 f,a=S['WOOD'].plotwrt()


    NameError: name 'S' is not defined


.. code:: python

    >>> fGHz = np.arange(1,10,0.01)
    >>> theta = np.arange(0,np.pi/2,0.01)
    >>> 
    >>> S['3D_WINDOW_GLASS']['lthick']=[0.006,0.01,0.006]
    >>> #S['3D_WINDOW_GLASS']['lmatname']=['GLASS','AIR','GLASS']
    ... S['3D_WINDOW_GLASS'].ev(fGHz,theta)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-23-05339df79104> in <module>()
          2 theta = np.arange(0,np.pi/2,0.01)
          3 
    ----> 4 S['3D_WINDOW_GLASS']['lthick']=[0.006,0.01,0.006]
          5 #S['3D_WINDOW_GLASS']['lmatname']=['GLASS','AIR','GLASS']
          6 S['3D_WINDOW_GLASS'].ev(fGHz,theta)


    NameError: name 'S' is not defined


.. code:: python

    >>> fig,ax = S['3D_WINDOW_GLASS'].plotwrt(var='f',coeff='T',polar='o')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-24-cc8035c90c3f> in <module>()
    ----> 1 fig,ax = S['3D_WINDOW_GLASS'].plotwrt(var='f',coeff='T',polar='o')
    

    NameError: name 'S' is not defined


.. code:: python

    >>> fig,ax = S['WOOD'].plotwrt(var='a',coeff='R',polar='p')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-25-ee7c78de1b07> in <module>()
    ----> 1 fig,ax = S['WOOD'].plotwrt(var='a',coeff='R',polar='p')
    

    NameError: name 'S' is not defined


plot with respect to angle

.. code:: python

    >>> fig = plt.figure(figsize=(20,20))
    >>> fGHz= np.array([2.4])
    >>> S['WOOD'].ev(fGHz,theta)
    >>> fig,ax = S['WOOD'].plotwrt(var='a',coeff='R',fig=fig)
    >>> plt.tight_layout()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-26-0685a6d65227> in <module>()
          1 fig = plt.figure(figsize=(20,20))
          2 fGHz= np.array([2.4])
    ----> 3 S['WOOD'].ev(fGHz,theta)
          4 fig,ax = S['WOOD'].plotwrt(var='a',coeff='R',fig=fig)
          5 plt.tight_layout()


    NameError: name 'S' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fac6976d3d0>


wrt to angle and frequency

.. code:: python

    >>> plt.figure(figsize=(10,10))
    >>> fGHz= np.arange(0.7,5.2,0.1)
    >>> S['WOOD'].ev(fGHz,theta)
    >>> S['WOOD'].pcolor()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-27-60f28c086001> in <module>()
          1 plt.figure(figsize=(10,10))
          2 fGHz= np.arange(0.7,5.2,0.1)
    ----> 3 S['WOOD'].ev(fGHz,theta)
          4 S['WOOD'].pcolor()


    NameError: name 'S' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fac697bb150>


.. code:: python

    >>> theta = np.arange(0,np.pi/2,0.01)
    >>> fGHz = np.arange(0.1,10,0.2)
    >>> sl = SlabDB('matDB.ini','slabDB.ini')
    >>> mat   = sl.mat
    >>> lmat  = [mat['AIR'],mat['WOOD']]
    >>> II    = MatInterface(lmat,0,fGHz,theta)
    >>> II.RT()
    >>> fig,ax = II.plotwrt(var='a',kv=10,typ=['m'])
    >>> plt.tight_layout()
    >>> air = mat['AIR']
    >>> brick  = mat['BRICK']
    >>> II  = MatInterface([air,brick],0,fGHz,theta)
    >>> II.RT()
    >>> fig,ax = II.plotwrt(var='f',color='k',typ=['m'])
    >>> plt.tight_layout()


::


    

    NoSectionErrorTraceback (most recent call last)

    <ipython-input-28-49900197fa9a> in <module>()
          1 theta = np.arange(0,np.pi/2,0.01)
          2 fGHz = np.arange(0.1,10,0.2)
    ----> 3 sl = SlabDB('matDB.ini','slabDB.ini')
          4 mat   = sl.mat
          5 lmat  = [mat['AIR'],mat['WOOD']]


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in __init__(self, filemat, fileslab, ds, dm)
       1895         self.fileslab = fileslab
       1896         if ds=={}:
    -> 1897             self.mat = MatDB()
       1898             if (filemat != ''):
       1899                 self.mat.load(filemat)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in __init__(self, _fileini, dm)
        865         self.filemat = self.fileini.replace('.ini','.mat')
        866         if dm=={}:
    --> 867             self.load(_fileini)
        868         else:
        869             #self.update(dm)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in load(self, _fileini)
       1110         config.read(fileini)
       1111 
    -> 1112         di = dict(config.items("dict") )
       1113 
       1114         self.di={}


    /home/uguen/anaconda2/lib/python2.7/ConfigParser.pyc in items(self, section, raw, vars)
        640         except KeyError:
        641             if section != DEFAULTSECT:
    --> 642                 raise NoSectionError(section)
        643         # Update with the entry specific variables
        644         if vars:


    NoSectionError: No section: 'dict'


.. code:: python

    >>> ## Adding new materials

.. code:: python

    >>> theta = np.arange(0,np.pi/2,0.01)
    >>> fGHz = np.arange(0.1,10,0.2)
    >>> sl = SlabDB('matDB.ini','slabDB.ini')
    >>> sl.mat.add(name='AIR2',cval=1.00000001+0j,sigma=0.00,typ='epsr')
    >>> 
    >>> sl.add(name='AIR-5cm',lmatname=['AIR2','AIR2'],lthick=[0.05,0.05])
    >>> sl.add(name='AIR-10cm',lmatname=['AIR2','AIR2'],lthick=[0.10,0.10])
    >>> sl.add(name='AIR-50cm',lmatname=['AIR2','AIR2'],lthick=[0.15,0.15])
    >>> fGHz=4
    >>> theta = np.arange(0,np.pi/2,0.01)
    >>> #figure(figsize=(8,8))
    ... # These Tessereau page 50
    ... 
    >>> sl['AIR-5cm'].ev(fGHz,theta,compensate=True)
    >>> sl['AIR-10cm'].ev(fGHz,theta,compensate=True)
    >>> sl['AIR-50cm'].ev(fGHz,theta,compensate=True)
    >>> 
    >>> # by default var='a' and kv = 0
    ... 
    >>> fig,ax = sl['AIR-5cm'].plotwrt(color='k',labels=['5cm'])
    >>> fig,ax = sl['AIR-10cm'].plotwrt(color='k',labels=['10cm'],linestyle='dashed',fig=fig,ax=ax)
    >>> fig,ax = sl['AIR-50cm'].plotwrt(color='k',labels=['15cm'],linestyle='dashdot',fig=fig,ax=ax)
    >>> plt.tight_layout()


::


    

    NoSectionErrorTraceback (most recent call last)

    <ipython-input-30-92bb85976ba5> in <module>()
          1 theta = np.arange(0,np.pi/2,0.01)
          2 fGHz = np.arange(0.1,10,0.2)
    ----> 3 sl = SlabDB('matDB.ini','slabDB.ini')
          4 sl.mat.add(name='AIR2',cval=1.00000001+0j,sigma=0.00,typ='epsr')
          5 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in __init__(self, filemat, fileslab, ds, dm)
       1895         self.fileslab = fileslab
       1896         if ds=={}:
    -> 1897             self.mat = MatDB()
       1898             if (filemat != ''):
       1899                 self.mat.load(filemat)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in __init__(self, _fileini, dm)
        865         self.filemat = self.fileini.replace('.ini','.mat')
        866         if dm=={}:
    --> 867             self.load(_fileini)
        868         else:
        869             #self.update(dm)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/slab.pyc in load(self, _fileini)
       1110         config.read(fileini)
       1111 
    -> 1112         di = dict(config.items("dict") )
       1113 
       1114         self.di={}


    /home/uguen/anaconda2/lib/python2.7/ConfigParser.pyc in items(self, section, raw, vars)
        640         except KeyError:
        641             if section != DEFAULTSECT:
    --> 642                 raise NoSectionError(section)
        643         # Update with the entry specific variables
        644         if vars:


    NoSectionError: No section: 'dict'


Evaluation without phase compensation
-------------------------------------

.. code:: python

    >>> fGHz = np.arange(2,16,0.1)
    >>> theta = 0
    >>> 
    >>> sl['AIR-5cm'].ev(fGHz,theta,compensate=False)
    >>> sl['AIR-10cm'].ev(fGHz,theta,compensate=False)
    >>> sl['AIR-50cm'].ev(fGHz,theta,compensate=False)
    >>> 
    >>> fig,ax = sl['AIR-5cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='r')
    >>> #print ax
    ... fig,ax = sl['AIR-10cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='g',fig=fig,ax=ax)
    >>> fig,ax = sl['AIR-50cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='b',fig=fig,ax=ax)
    >>> sl['AIR-5cm'].ev(fGHz,theta,compensate=True)
    >>> sl['AIR-10cm'].ev(fGHz,theta,compensate=True)
    >>> sl['AIR-50cm'].ev(fGHz,theta,compensate=True)
    >>> 
    >>> # by default var='a' and kv = 0
    ... 
    >>> fig,ax = sl['AIR-5cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='r',linestyle='dashdot',fig=fig,ax=ax)
    >>> fig,ax = sl['AIR-10cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='g',linestyle='dashed',fig=fig,ax=ax)
    >>> fig,ax = sl['AIR-50cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='b',linestyle='dashdot',fig=fig,ax=ax)
    >>> plt.tight_layout()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-31-c99e7182b882> in <module>()
          2 theta = 0
          3 
    ----> 4 sl['AIR-5cm'].ev(fGHz,theta,compensate=False)
          5 sl['AIR-10cm'].ev(fGHz,theta,compensate=False)
          6 sl['AIR-50cm'].ev(fGHz,theta,compensate=False)


    NameError: name 'sl' is not defined


.. code:: python

    >>> from pylayers.signal.bsignal import *

.. code:: python

    >>> sl['AIR-5cm'].ev(fGHz,theta,compensate=False)
    >>> 
    >>> S = sl['AIR-5cm']
    >>> f=S.fGHz
    >>> y = S.T[:,0,0,0]
    >>> F=FUsignal(f[:,0],y)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-33-da0b07493155> in <module>()
    ----> 1 sl['AIR-5cm'].ev(fGHz,theta,compensate=False)
          2 
          3 S = sl['AIR-5cm']
          4 f=S.fGHz
          5 y = S.T[:,0,0,0]


    NameError: name 'sl' is not defined


.. code:: python

    >>> g=F.ift(ffts=1)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-34-8ee5f6980ebe> in <module>()
    ----> 1 g=F.ift(ffts=1)
    

    NameError: name 'F' is not defined


.. code:: python

    >>> g.plot(typ='v')
    (<matplotlib.figure.Figure at 0x7fccdfd0fe90>,
     array([[<matplotlib.axes.AxesSubplot object at 0x7fccdfd1d510>]], dtype=object))


::


      File "<ipython-input-35-a36be946445c>", line 2
        (<matplotlib.figure.Figure at 0x7fccdfd0fe90>,
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> sl['AIR-5cm'].ev(fGHz,theta,compensate=True)
    >>> sl['AIR-10cm'].ev(fGHz,theta,compensate=True)
    >>> sl['AIR-50cm'].ev(fGHz,theta,compensate=True)
    >>> 
    >>> fig,ax = sl['AIR-5cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='k')
    >>> #print ax
    ... fig,ax = sl['AIR-10cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='k',linestyle='dashed',fig=fig,ax=ax)
    >>> fig,ax = sl['AIR-50cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='k',linestyle='dashdot',fig=fig,ax=ax)
    >>> plt.tight_layout()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-36-b66adc42f3b2> in <module>()
    ----> 1 sl['AIR-5cm'].ev(fGHz,theta,compensate=True)
          2 sl['AIR-10cm'].ev(fGHz,theta,compensate=True)
          3 sl['AIR-50cm'].ev(fGHz,theta,compensate=True)
          4 
          5 fig,ax = sl['AIR-5cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='k')


    NameError: name 'sl' is not defined


.. code:: python

    >>> sl.mat.add(name='ConcreteJc',cval=3.5,alpha_cmm1=1.9,fGHz=120,typ='THz')
    >>> sl.mat.add(name='GlassJc',cval=2.55,alpha_cmm1=2.4,fGHz=120,typ='THz')
    >>> sl.add('ConcreteJc',['ConcreteJc'],[0.049])
    >>> 
    >>> theta = np.linspace(20,60,100)*np.pi/180
    >>> sl['ConcreteJc'].ev(120,theta)
    >>> fig,ax = sl['ConcreteJc'].plotwrt('a')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-37-76050b84c6f2> in <module>()
    ----> 1 sl.mat.add(name='ConcreteJc',cval=3.5,alpha_cmm1=1.9,fGHz=120,typ='THz')
          2 sl.mat.add(name='GlassJc',cval=2.55,alpha_cmm1=2.4,fGHz=120,typ='THz')
          3 sl.add('ConcreteJc',['ConcreteJc'],[0.049])
          4 
          5 theta = np.linspace(20,60,100)*np.pi/180


    NameError: name 'sl' is not defined


.. code:: python

    >>> plt.figure(figsize=(20,10))
    >>> fGHz = np.linspace(110,135,50)
    >>> sl.add('DoubleGlass',['GlassJc','AIR','GlassJc'],[0.0029,0.0102,0.0029])
    >>> sl['DoubleGlass'].ev(fGHz,theta)
    >>> sl['DoubleGlass'].pcolor(dB=True)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-38-1089ffa80239> in <module>()
          1 plt.figure(figsize=(20,10))
          2 fGHz = np.linspace(110,135,50)
    ----> 3 sl.add('DoubleGlass',['GlassJc','AIR','GlassJc'],[0.0029,0.0102,0.0029])
          4 sl['DoubleGlass'].ev(fGHz,theta)
          5 sl['DoubleGlass'].pcolor(dB=True)


    NameError: name 'sl' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fac6988e150>


.. code:: python

    >>> f = plt.figure(figsize=(4,4))
    >>> f = sl['DoubleGlass'].ev(120,theta)
    >>> fig,ax = sl['DoubleGlass'].plotwrt('a',figsize=(10,10))
    >>> plt.tight_layout()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-39-accc30f21d67> in <module>()
          1 f = plt.figure(figsize=(4,4))
    ----> 2 f = sl['DoubleGlass'].ev(120,theta)
          3 fig,ax = sl['DoubleGlass'].plotwrt('a',figsize=(10,10))
          4 plt.tight_layout()


    NameError: name 'sl' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fac697cd510>


.. code:: python

    >>> freq = np.linspace(110,135,50)
    >>> sl['DoubleGlass'].ev(freq,theta)
    >>> fig,ax = sl['DoubleGlass'].plotwrt('f',figsize=(10,10))  # @20
    >>> plt.tight_layout()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-40-38e515fdfb7d> in <module>()
          1 freq = np.linspace(110,135,50)
    ----> 2 sl['DoubleGlass'].ev(freq,theta)
          3 fig,ax = sl['DoubleGlass'].plotwrt('f',figsize=(10,10))  # @20
          4 plt.tight_layout()


    NameError: name 'sl' is not defined


References
----------

[1]. `Jacob, M. ; Kurner, T. ; Geise, R. ; Piesiewicz, R. "Reflection
ant Transmission Properties of Building Materials in D-Band for Modeling
Future mm-Wave Communication Systems" Antennas and Propagation (EuCAP),
2010 Proceedings of the Fourth European Conference
on <http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=5505315&queryText%3DReflection+ant+Transmission+Properties+of+Building+Materials+in+D-Band+for+Modeling+Future+mm-Wave+Communication+Systems.QT.+Antennas+and+Propagation>`__

[2]. `R.Piesiewicz 'Terahertz characterization of building materials'
Electronics .Letters Jan 2005 Vol 41
N18 <https://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CCwQFjAA&url=http%3A%2F%2Fwww-ece.rice.edu%2F~daniel%2Fpapers%2FnormanElecLett.pdf&ei=Tr_eUe6EG-OM0AWA0IAw&usg=AFQjCNHzt9H3RkLAtws51E9EpEgyqh-6LA&sig2=QLZlhoTJtiuHAW5Zzg_xOw&bvm=bv.48705608,d.d2k>`__
