
Vector Spherical Harmonics Representation of Antennas
=====================================================

.. code:: python

    from pylayers.antprop.antenna import *
    from pylayers.antprop.antvsh import *
    %matplotlib inline


.. parsed-literal::

    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


::


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-8b1bd9b086f4> in <module>()
          1 from pylayers.antprop.antenna import *
    ----> 2 from pylayers.antprop.antvsh import *
          3 get_ipython().magic(u'matplotlib inline')


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/antvsh.py in <module>()
         12 import pylayers.antprop.antenna as ant
         13 from pylayers.antprop.spharm import *
    ---> 14 from sphere import spherepack, Wrapec, mathtogeo
         15 import numpy as np
         16 


    ImportError: No module named sphere


Loading an Antenna from a Matlab file

.. code:: python

    A = Antenna('S2R2.mat',directory='ant/UWBAN/Matfile')

The shape of the :math:`F_{\phi}` functions indicates :

-  :math:`N_{\theta} = 91`
-  :math:`N_{\phi} = 180 `
-  :math:`N_f= 104`

.. code:: python

    np.shape(A.Fp)




.. parsed-literal::

    (91, 180, 104)



The frequency array is expressed in :math:`GHz` and delays are expressed
in :math:`ns`

.. code:: python

    fGHz = A.fGHz

.. code:: python

    fGHz.shape




.. parsed-literal::

    (104,)



Then an electrical delay of :math:`4.185ns` is applied on the
:math:`F_{\theta}`

.. code:: python

    I = A.Ft[:,:,:]

.. code:: python

    I.shape




.. parsed-literal::

    (91, 180, 104)



.. code:: python

    plt.figure(figsize=(10,8))
    plt.imshow(np.unwrap(np.angle(I[:,45,:])))
    plt.title(r'Unwrapped phase of $F_{\theta}$ w.r.t frequency and phi for $\theta=\frac{pi}{2}$')
    plt.ylabel('f index')
    plt.colorbar()
    plt.figure()
    plt.plot(fGHz,np.unwrap(np.angle(I[45,85,:])))
    plt.xlabel('f index')




.. parsed-literal::

    <matplotlib.text.Text at 0x2b4a0af26250>



.. code:: python

    tau=4.185
    I = A.Ft[:,:,:]*np.exp(-2*1j*np.pi*fGHz[None,None,:]*tau)

.. code:: python

    plt.imshow(np.unwrap(np.angle(I[:,45,:])))
    plt.title(r'Unwrapped phase of $F_{\theta}$ w.r.t frequency and phi for $\theta=\frac{pi}{2}$')
    plt.ylabel('f index')
    plt.colorbar()
    plt.figure()
    plt.plot(fGHz,np.unwrap(np.angle(I[45,85,:])))




.. parsed-literal::

    [<matplotlib.lines.Line2D at 0x2b4a0b0d4790>]



Display of the radiation pattern for all frequencies
''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    plt.figure(figsize=(10,10))
    for nf in range(104):
        plt.polar(A.phi,abs(A.Ft[45,:,nf]))

.. code:: python

    A.info()


.. parsed-literal::

    S2R2.mat
    type :  mat
    S2R2
    Th1
    04/13/12
    09:59
    
    
    2
    2
    Nb theta (lat) : 91
    Nb phi (lon) : 180
    No vsh coefficient calculated yet


Evaluation of Vector Spherical Harmonics Coefficients
=====================================================

At that stage we compute the Vector Spherical Harmonics coefficients

.. code:: python

    A=vsh(A)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-aab26d118494> in <module>()
    ----> 1 A=vsh(A)
    

    NameError: name 'vsh' is not defined


.. code:: python

    A.info()


.. parsed-literal::

    S2R2.mat
    type :  mat
    S2R2
    Th1
    04/13/12
    09:59
    
    
    2
    2
    Nb theta (lat) : 91
    Nb phi (lon) : 180
    No vsh coefficient calculated yet


.. code:: python

    A.C.s1tos2(30)


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-15-98aa5dfbfef3> in <module>()
    ----> 1 A.C.s1tos2(30)
    

    AttributeError: 'Antenna' object has no attribute 'C'


.. code:: python

    A.C


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-16-ea02b37ef526> in <module>()
    ----> 1 A.C
    

    AttributeError: 'Antenna' object has no attribute 'C'


.. code:: python

    fig = plt.figure(figsize=(8,8))
    A.C.show('s2',k=300)


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-17-a2dac715dfe4> in <module>()
          1 fig = plt.figure(figsize=(8,8))
    ----> 2 A.C.show('s2',k=300)
    

    AttributeError: 'Antenna' object has no attribute 'C'


.. code:: python

    A.C.s2tos3()


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-18-34ddad199ddd> in <module>()
    ----> 1 A.C.s2tos3()
    

    AttributeError: 'Antenna' object has no attribute 'C'


.. code:: python

    A.C


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-19-ea02b37ef526> in <module>()
    ----> 1 A.C
    

    AttributeError: 'Antenna' object has no attribute 'C'


.. code:: python

    fig = plt.figure(figsize=(8,8))
    A.C.show('s3')
    plt.tight_layout()


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-20-627adf1c1577> in <module>()
          1 fig = plt.figure(figsize=(8,8))
    ----> 2 A.C.show('s3')
          3 plt.tight_layout()


    AttributeError: 'Antenna' object has no attribute 'C'

