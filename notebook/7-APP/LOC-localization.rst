
.. code:: python

    >>> from pylayers.location.algebraic.algebraic import *
    >>> from pylayers.util.geomutil import dist

Example of TDOA
---------------

First, it is necessary to define Anchor nodes and associated Reference
Anchor Nodes. This is important to be very specific about what exactly
the TDOA is. In the example the Blin node is draw randomly as well as
anchor nodes.

.. code:: python

    >>> nodes = {}
    >>> N = 5
    >>> AN_TDOA = np.random.rand(2,N)
    >>> #AN_TDOA1=np.array([[0, 0, 1, 1],[0,1,1,0]])
    ... #AN_TDOAr1 = np.roll(AN_TDOA,1,axis=1)
    ... AN_TDOAr1 = np.zeros((2,1))
    >>> AN_TDOAr2 = AN_TDOA[:,-1][:,newaxis]
    >>> BN = np.array([[0.2],[0.3]])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-2-79b4e5964fd9> in <module>()
          5 #AN_TDOAr1 = np.roll(AN_TDOA,1,axis=1)
          6 AN_TDOAr1 = np.zeros((2,1))
    ----> 7 AN_TDOAr2 = AN_TDOA[:,-1][:,newaxis]
          8 BN = np.array([[0.2],[0.3]])


    NameError: name 'newaxis' is not defined


.. code:: python

    >>> AN_TDOA




.. parsed-literal::

    array([[ 0.58292152,  0.35540612,  0.98027353,  0.39872618,  0.25619099],
           [ 0.44256616,  0.9522736 ,  0.17645851,  0.67688177,  0.28602975]])



.. code:: python

    >>> AN_TDOAr1




.. parsed-literal::

    array([[ 0.],
           [ 0.]])



.. code:: python

    >>> AN_TDOAr2


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-5-436f1e4f0ad6> in <module>()
    ----> 1 AN_TDOAr2
    

    NameError: name 'AN_TDOAr2' is not defined


The figure below illustrates the situation, in red the anchor nodes, the
blue star is the blind node.

.. code:: python

    >>> plot(AN_TDOA[0,:],AN_TDOA[1,:],'or')
    >>> plot(AN_TDOAr2[0,:],AN_TDOAr2[1,:],'ok')
    >>> plot(BN[0,:],BN[1,:],'*b')
    >>> axis([-1,2,-1,2])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-6-92be54b6c82d> in <module>()
    ----> 1 plot(AN_TDOA[0,:],AN_TDOA[1,:],'or')
          2 plot(AN_TDOAr2[0,:],AN_TDOAr2[1,:],'ok')
          3 plot(BN[0,:],BN[1,:],'*b')
          4 axis([-1,2,-1,2])


    NameError: name 'plot' is not defined


.. code:: python

    >>> d = dist(AN_TDOA,BN,0)
    >>> dr1= dist(AN_TDOAr1,BN,0)
    >>> dr2= dist(AN_TDOAr2,BN,0)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-7-25d284671896> in <module>()
    ----> 1 d = dist(AN_TDOA,BN,0)
          2 dr1= dist(AN_TDOAr1,BN,0)
          3 dr2= dist(AN_TDOAr2,BN,0)


    NameError: name 'BN' is not defined


.. code:: python

    >>> tdoa1 = (d-dr1)/0.3
    >>> tdoa2 = (d-dr2)/0.3
    >>> tdoa0 = (d-roll(d,1))/0.3
    >>> 
    >>> print cumsum(tdoa0)
    >>> print tdoa1
    >>> print tdoa2


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-8-3d7b60d1ff7d> in <module>()
    ----> 1 tdoa1 = (d-dr1)/0.3
          2 tdoa2 = (d-dr2)/0.3
          3 tdoa0 = (d-roll(d,1))/0.3
          4 
          5 print cumsum(tdoa0)


    NameError: name 'd' is not defined


.. code:: python

    >>> node={}
    >>> nodes['BN']=BN
    >>> nodes['RN_TDOA']=AN_TDOA
    >>> nodes['RNr_TDOA']=AN_TDOAr2
    >>> ldp = {}
    >>> ldp['TDOA']=cumsum(tdoa0)
    >>> ldp['TDOA_std']=np.ones(N)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-9-d6830f92a80e> in <module>()
          1 node={}
    ----> 2 nodes['BN']=BN
          3 nodes['RN_TDOA']=AN_TDOA
          4 nodes['RNr_TDOA']=AN_TDOAr2
          5 ldp = {}


    NameError: name 'BN' is not defined


.. code:: python

    >>> S=algloc(nodes,ldp)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-10-bb0e749f8356> in <module>()
    ----> 1 S=algloc(nodes,ldp)
    

    NameError: name 'ldp' is not defined


.. code:: python

    >>> S.info()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-11-7e129c87000d> in <module>()
    ----> 1 S.info()
    

    NameError: name 'S' is not defined


.. code:: python

    >>> S = algloc(nodes,ldp)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-12-61c872391df3> in <module>()
    ----> 1 S = algloc(nodes,ldp)
    

    NameError: name 'ldp' is not defined


.. code:: python

    >>> S.ls_locate(tdoa=True,toa=False,rss=False)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-4c8efe0f5b1d> in <module>()
    ----> 1 S.ls_locate(tdoa=True,toa=False,rss=False)
    

    NameError: name 'S' is not defined


.. code:: python

    >>> nodes['BN']


::


    

    KeyErrorTraceback (most recent call last)

    <ipython-input-14-406418aaf451> in <module>()
    ----> 1 nodes['BN']
    

    KeyError: 'BN'

