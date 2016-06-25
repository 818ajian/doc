
Ray Signatures
==============

Signature are calculated from a cycle to an other cycle of the Layout.
They are used for the determination of rays once the transmitter and
receiver are known. The best algorithmic manner to get a signature is
not stabilized yet, a lot of approaches have been implemented so far,
with very different performances. It is expected that the signature is
delivering all its utility when dealing with mobile trajectories.

The evaluation of a signature from one cycle to another is implemented
in the ``pylayers.simul.Link.DLink`` class.

.. code:: python

    >>> import time
    >>> from pylayers.gis.layout import *
    >>> from pylayers.antprop.signature import *
    >>> from pylayers.antprop.rays import *
    >>> %matplotlib inline
    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


::


      File "<ipython-input-1-e2cf2ca1f64d>", line 6
        WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.
               ^
    SyntaxError: invalid syntax



.. code:: python

    >>> L = Layout('defstr3.ini')
    >>> L.build()
    >>> L.dumpw()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-2-1b28416d0633> in <module>()
    ----> 1 L = Layout('defstr3.ini')
          2 L.build()
          3 L.dumpw()


    NameError: name 'Layout' is not defined


Showing the graph of rooms with 2 rooms separated by a DOOR segment

.. code:: python

    >>> L.showG('sv',figsize=(8,8))
    >>> a=plt.axis('off')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-3-69f89247822d> in <module>()
    ----> 1 L.showG('sv',figsize=(8,8))
          2 a=plt.axis('off')


    NameError: name 'L' is not defined


The graph of interactions is shown below.

.. code:: python

    >>> L.showG('si',figsize=(10,5))
    >>> a=plt.axis('off')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-4-5c11869b119b> in <module>()
    ----> 1 L.showG('si',figsize=(10,5))
          2 a=plt.axis('off')


    NameError: name 'L' is not defined


All the interactions of a given cycle are stored as meta information in
nodes of ``Gt``

.. code:: python

    >>> L.Gi.node
    {(1, 1): {},
     (1, 1, 2): {},
     (1, 2): {},
     (1, 2, 1): {},
     (2, 1): {},
     (2, 1, 2): {},
     (2, 2): {},
     (2, 2, 1): {},
     (3, 1): {},
     (3, 1, 2): {},
     (3, 2): {},
     (3, 2, 1): {},
     (4, 0): {},
     (4, 0, 2): {},
     (4, 2): {},
     (4, 2, 0): {},
     (5, 0): {},
     (5, 0, 2): {},
     (5, 2): {},
     (5, 2, 0): {},
     (6, 0): {},
     (6, 0, 1): {},
     (6, 1): {},
     (6, 1, 0): {},
     (7, 0): {},
     (7, 0, 1): {},
     (7, 1): {},
     (7, 1, 0): {},
     (8, 0): {},
     (8, 0, 1): {},
     (8, 1): {},
     (8, 1, 0): {},
     (9, 0): {},
     (9, 0, 2): {},
     (9, 2): {},
     (9, 2, 0): {}}


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-5-475bc72d06f6> in <module>()
    ----> 1 L.Gi.node
          2 {(1, 1): {},
          3  (1, 1, 2): {},
          4  (1, 2): {},
          5  (1, 2, 1): {},


    NameError: name 'L' is not defined


.. code:: python

    >>> L.Gt.node[0]['inter']
    [(6, 0),
     (6, 0, 1),
     (6, 1, 0),
     (7, 0),
     (7, 0, 1),
     (7, 1, 0),
     (8, 0),
     (8, 0, 1),
     (8, 1, 0),
     (9, 0),
     (9, 0, 2),
     (9, 2, 0),
     (4, 0),
     (4, 0, 2),
     (4, 2, 0),
     (5, 0),
     (5, 0, 2),
     (5, 2, 0),
     (-4,),
     (-3,),
     (-1,),
     (-6,)]


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-6-81223cded9eb> in <module>()
    ----> 1 L.Gt.node[0]['inter']
          2 [(6, 0),
          3  (6, 0, 1),
          4  (6, 1, 0),
          5  (7, 0),


    NameError: name 'L' is not defined


The signature is calculated with as parameters the Layout object and two
cycle numbers. In example below it is 0 and 1.

.. code:: python

    >>> Si = Signatures(L,0,1)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-7-e66f0bac9490> in <module>()
    ----> 1 Si = Signatures(L,0,1)
    

    NameError: name 'Signatures' is not defined


The cold start determination of the signature is done with a ``run``
function. The code is not in its final shape here and there is room for
significant acceleration in incorporating propagation based heuristics.
The mitigation of graph exploration depth is done in setting a
``cutoff`` value which limits the exploration in the interaction graph.

.. code:: python

    >>> Si.run5(cutoff=5,diffraction=False,algo='old')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-8-d547d93e7556> in <module>()
    ----> 1 Si.run5(cutoff=5,diffraction=False,algo='old')
    

    NameError: name 'Si' is not defined


The representation method of a signature gives informations about the
different signatures. Signatures are grouped by number of interactions.

.. code:: python

    >>> L.Gt.pos
    {0: (758.49, 1111.9),
     1: (766.00300113353387, 1113.947479109665),
     2: (761.00289669547806, 1113.915769812613)}


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-9-e1ae3d494b8e> in <module>()
    ----> 1 L.Gt.pos
          2 {0: (758.49, 1111.9),
          3  1: (766.00300113353387, 1113.947479109665),
          4  2: (761.00289669547806, 1113.915769812613)}


    NameError: name 'L' is not defined


.. code:: python

    >>> ptx = np.array(L.Gt.pos[0])+np.random.rand(2)
    >>> prx = np.array(L.Gt.pos[1])+np.random.rand(2)
    >>> print ptx
    >>> print prx
    [  759.3213136   1112.39386191]
    [  766.8885467   1113.98892221]


::


      File "<ipython-input-10-c94cbc15cbec>", line 5
        [  759.3213136   1112.39386191]
                                     ^
    SyntaxError: invalid syntax


