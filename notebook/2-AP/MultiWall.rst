
Multi-wall model
================

.. code:: python

    >>> import time
    >>> from pylayers.util.project import *
    >>> import pylayers.util.pyutil as pyu
    >>> from pylayers.util.utilnet import str2bool
    >>> from pylayers.gis.layout import Layout
    >>> from pylayers.antprop.loss import *
    >>> from pylayers.antprop.coverage import *
    >>> from pylayers.network.model import *
    >>> %matplotlib inline
    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


::


      File "<ipython-input-1-e3331cb5497f>", line 10
        WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.
               ^
    SyntaxError: invalid syntax



The layout is loaded from an ini file. If the graphs are not available,
they are built.

.. code:: python

    >>> L=Layout('TA-Office.ini')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-2-8fe0893dc7d7> in <module>()
    ----> 1 L=Layout('TA-Office.ini')
    

    NameError: name 'Layout' is not defined


Defining a radio link
---------------------

The 2 extremities of the radio link (transmitter and receiver) have
coordinates described as 1x2 ``numpy.array`` .

-  A a radio node

-  B a radio node

.. code:: python

    >>> A=np.array((4,1)) # defining transmitter position
    >>> B=np.array((30,12)) # defining receiver position


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-3-25cc59217f06> in <module>()
    ----> 1 A=np.array((4,1)) # defining transmitter position
          2 B=np.array((30,12)) # defining receiver position


    NameError: name 'np' is not defined


Ploting the scene
-----------------

The scene is plotted with the ``showG`` method of the Layout

.. code:: python

    >>> # figure instanciation
    ... f = plt.figure(figsize=(10,5))
    >>> ax = f.add_subplot(111)
    >>> r = np.array((A,B))
    >>> # plotting the Layout
    ... f,ax = L.showG(fig=f,ax=ax,graph='s',nodes=False)
    >>> # plotting the Tx and Rx
    ... ax.plot(A[0],A[1],'ob')
    >>> ax.plot(B[0],B[1],'or')
    >>> # plotting the LOS
    ... ax.plot(r[:,0],r[:,1])
    >>> a = plt.axis('off')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-4-5cfa9ca06c88> in <module>()
          1 # figure instanciation
    ----> 2 f = plt.figure(figsize=(10,5))
          3 ax = f.add_subplot(111)
          4 r = np.array((A,B))
          5 # plotting the Layout


    NameError: name 'plt' is not defined


Finding the intersection between the "direct" path and the walls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The function ``angleonlink`` returns the list of intersected segments
and the corresponding incidence angles (in radians) with respect to the
segment normal.

.. code:: python

    >>> %pdef L.angleonlink
     [0mL[0m[1;33m.[0m[0mangleonlink[0m[1;33m([0m[0mp1[0m[1;33m=[0m[0marray[0m[1;33m([0m[1;33m[[0m[1;36m0[0m[1;33m,[0m [1;36m0[0m[1;33m][0m[1;33m)[0m[1;33m,[0m [0mp2[0m[1;33m=[0m[0marray[0m[1;33m([0m[1;33m[[0m[1;36m10[0m[1;33m,[0m  [1;36m3[0m[1;33m][0m[1;33m)[0m[1;33m)[0m[1;33m[0m[0m


::


      File "<ipython-input-5-e81e63b4c346>", line 2
        L.angleonlink(p1=array([0, 0]), p2=array([10,  3]))
        ^
    IndentationError: unexpected indent



.. code:: python

    >>> data=L.angleonlink(A,B)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-6-39f90e3e3d7a> in <module>()
    ----> 1 data=L.angleonlink(A,B)
    

    NameError: name 'L' is not defined


Computing the Multi-wall model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The multi-wall model computation returns losses and LOS excess delay for
orthogonal and parallel polarization

.. code:: python

    >>> fGHz = 2.4
    >>> # observation grid
    ... 
    >>> r = np.array((B,B))
    >>> 
    >>> Lwo,Lwp,Edo,Edp = Losst(L,fGHz,r.T,A)
    >>> 
    >>> print 'Losses orthogonal polarization \t %g dB' %(Lwo[0][0])
    >>> print 'Losses parallel polarization \t %g  dB' % (Lwp[0][0])
    >>> print 'Excess delay orthogonal polarization  \t %g ns' %(Edo[0][0])
    >>> print 'Excess delay parallel polarization   \t %g ns' %(Edp[0][0])
    Losses orthogonal polarization 	 27.7333 dB
    Losses parallel polarization 	 16.0573  dB
    Excess delay orthogonal polarization  	 2.23113 ns
    Excess delay parallel polarization   	 2.12364 ns


::


      File "<ipython-input-7-df769759dd7e>", line 12
        Losses orthogonal polarization 	 27.7333 dB
                        ^
    SyntaxError: invalid syntax



Coverage class
==============

By extension, the multi-wall model can also be used to perform a full
coverage of a Layout given a transmitter position.

.. code:: python

    >>> C = Coverage()
    >>> C.L  = L # set layout
    >>> C.tx = A # set the transmitter


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-8-76566dcea2a0> in <module>()
    ----> 1 C = Coverage()
          2 C.L  = L # set layout
          3 C.tx = A # set the transmitter


    NameError: name 'Coverage' is not defined


.. code:: python

    >>> C.L
    
    ----------------
    TA-Office.ini
    Image('/home/uguen/Bureau/P1/struc/images/DLR4991.png')
    ----------------
    
    Number of points  : 71
    Number of segments  : 94
    Number of sub segments  : 16
    Number of cycles  : 25
    Number of rooms  : 24
    degree 0 : []
    degree 1 : []
    degree 2 : 39
    degree 3 : 32
    
    xrange :(0.0, 40.0)
    yrange :(0.0, 15.0)
    
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
    tgs : get segment index in tahe from Gs
    lsss : list of segments with sub-segment
    sla : list of all slab names (Nsmax+Nss+1)
    degree : degree of nodes


::


      File "<ipython-input-9-7e69ca5592c5>", line 3
        ----------------
                        ^
    SyntaxError: invalid syntax



.. code:: python

    >>> C.creategrid()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-10-73806d2fb195> in <module>()
    ----> 1 C.creategrid()
    

    NameError: name 'C' is not defined


The coverage is performed on a grid. Boundaries of the grid are
specified in the
```coverage.ini`` <https://github.com/pylayers/pylayers/blob/master/data/ini/coverage.ini>`__
file

Compute the coverage
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> t1=time.time()
    >>> C.cover()
    >>> t2=time.time()
    >>> print 'Coverage performed in ', t2-t1, 's'
    Coverage performed in  3.23957109451 s


::


      File "<ipython-input-11-efd44dc9bce8>", line 5
        Coverage performed in  3.23957109451 s
                         ^
    SyntaxError: invalid syntax



Coverage Map
~~~~~~~~~~~~

For Orthogonal polarization

.. code:: python

    >>> fig1=plt.figure(figsize=(10,10))
    >>> f,a = C.show(typ='pr',fig=fig1,nodes=False)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-12-5d2b3b06a7b1> in <module>()
    ----> 1 fig1=plt.figure(figsize=(10,10))
          2 f,a = C.show(typ='pr',fig=fig1,nodes=False)


    NameError: name 'plt' is not defined


For parallel polarization

.. code:: python

    >>> C.cover(snr=False,sinr=False)
    >>> fig1=plt.figure(figsize=(10,10))
    >>> f,a = C.show(typ='pr',fig=fig1)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-05b14cbbec00> in <module>()
    ----> 1 C.cover(snr=False,sinr=False)
          2 fig1=plt.figure(figsize=(10,10))
          3 f,a = C.show(typ='pr',fig=fig1)


    NameError: name 'C' is not defined

