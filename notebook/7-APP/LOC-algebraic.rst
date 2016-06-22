
Algebraic Localization Class
============================

For localization in the plane, it is important not to specify the z
coordinates. Otherwise a singularity problem arises.

.. code:: python

    >>> import numpy as np
    >>> from pylayers.location.algebraic.algebraic  import *
    >>> %matplotlib inline

.. code:: python

    >>> nodes={}
    >>> ldp={}
    >>> p1 = np.array([-1,-1])
    >>> p2 = np.array([1,-1])
    >>> p3 = np.array([0,1])
    >>> nodes['BN'] = np.array([[0],[0]])
    >>> nodes['RN_TOA']=np.vstack((p1,p2,p3)).T
    >>> ldp['TOA']=np.array([np.sqrt(2),np.sqrt(2),1])
    >>> ldp['TOA_std']=np.array([1,1,1])
    >>> Alg = algloc(nodes,ldp)

.. code:: python

    >>> print ldp
    >>> f,a = Alg.plot()


.. parsed-literal::

    {'TOA_std': array([1, 1, 1]), 'TOA': array([ 1.41421356,  1.41421356,  1.        ])}



.. image:: LOC-algebraic_files/LOC-algebraic_3_1.png


.. code:: python

    >>> pest = Alg.ls_locate(toa=True,tdoa=False,rss=False)

.. code:: python

    >>> pest




.. parsed-literal::

    array([[ 0.        ],
           [-0.22753112]])



.. code:: python

    >>> Alg




.. parsed-literal::

    Nodes : {'BN': array([[0],
           [0]]), 'RN_TOA': array([[-1,  1,  0],
           [-1, -1,  1]])}
    LDPs :{'TOA_std': array([1, 1, 1]), 'TOA': array([ 1.41421356,  1.41421356,  1.        ])}


