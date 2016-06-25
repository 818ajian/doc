
Vector Spherical Harmonics Representation of Antennas
=====================================================

.. code:: python

    >>> from pylayers.antprop.antenna import *
    >>> from pylayers.antprop.antvsh import *
    >>> %matplotlib inline
    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


::


      File "<ipython-input-1-ebe886ecb0a6>", line 4
        WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.
               ^
    SyntaxError: invalid syntax



Loading an Antenna from a Matlab file

.. code:: python

    >>> A = Antenna('S2R2.mat',directory='ant/UWBAN/Matfile')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-2-806a96154428> in <module>()
    ----> 1 A = Antenna('S2R2.mat',directory='ant/UWBAN/Matfile')
    

    NameError: name 'Antenna' is not defined


The shape of the :math:`F_{\phi}` functions indicates :

-  :math:`N_{\theta} = 91`
-  :math:`N_{\phi} = 180 `
-  :math:`N_f= 104`

.. code:: python

    >>> np.shape(A.Fp)
    (91, 180, 104)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-3-a3080c48ba8c> in <module>()
    ----> 1 np.shape(A.Fp)
          2 (91, 180, 104)


    NameError: name 'np' is not defined


The frequency array is expressed in :math:`GHz` and delays are expressed
in :math:`ns`

.. code:: python

    >>> fGHz = A.fGHz


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-4-7837d8426b1a> in <module>()
    ----> 1 fGHz = A.fGHz
    

    NameError: name 'A' is not defined


.. code:: python

    >>> fGHz.shape
    (104,)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-5-eff372d2becb> in <module>()
    ----> 1 fGHz.shape
          2 (104,)


    NameError: name 'fGHz' is not defined


Then an electrical delay of :math:`4.185ns` is applied on the
:math:`F_{\theta}`

.. code:: python

    >>> I = A.Ft[:,:,:]


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-6-c10f1b8c978a> in <module>()
    ----> 1 I = A.Ft[:,:,:]
    

    NameError: name 'A' is not defined


.. code:: python

    >>> I.shape
    (91, 180, 104)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-7-417a8641729a> in <module>()
    ----> 1 I.shape
          2 (91, 180, 104)


    NameError: name 'I' is not defined


.. code:: python

    >>> plt.figure(figsize=(10,8))
    >>> plt.imshow(np.unwrap(np.angle(I[:,45,:])))
    >>> plt.title(r'Unwrapped phase of $F_{\theta}$ w.r.t frequency and phi for $\theta=\frac{pi}{2}$')
    >>> plt.ylabel('f index')
    >>> plt.colorbar()
    >>> plt.figure()
    >>> plt.plot(fGHz,np.unwrap(np.angle(I[45,85,:])))
    >>> plt.xlabel('f index')
    
    /home/uguen/anaconda/lib/python2.7/site-packages/matplotlib/collections.py:590: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      if self._edgecolors == str('face'):


::


      File "<ipython-input-8-714df3a8331e>", line 10
        home(/uguen/anaconda/lib/python2.7/site-packages/matplotlib/collections.py:590:, FutureWarning:, elementwise, comparison, failed;, returning, scalar, instead,, but, in, the, future, will, perform, elementwise, comparison)
             ^
    SyntaxError: invalid syntax



.. code:: python

    >>> tau=4.185
    >>> I = A.Ft[:,:,:]*np.exp(-2*1j*np.pi*fGHz[None,None,:]*tau)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-9-24216f96e669> in <module>()
          1 tau=4.185
    ----> 2 I = A.Ft[:,:,:]*np.exp(-2*1j*np.pi*fGHz[None,None,:]*tau)
    

    NameError: name 'A' is not defined


.. code:: python

    >>> plt.imshow(np.unwrap(np.angle(I[:,45,:])))
    >>> plt.title(r'Unwrapped phase of $F_{\theta}$ w.r.t frequency and phi for $\theta=\frac{pi}{2}$')
    >>> plt.ylabel('f index')
    >>> plt.colorbar()
    >>> plt.figure()
    >>> plt.plot(fGHz,np.unwrap(np.angle(I[45,85,:])))
    [<matplotlib.lines.Line2D at 0x7f2a328d7190>]


::


      File "<ipython-input-10-07b6b2e40f77>", line 7
        [<matplotlib.lines.Line2D at 0x7f2a328d7190>]
         ^
    SyntaxError: invalid syntax



Display of the radiation pattern for all frequencies
''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: python

    >>> plt.figure(figsize=(10,10))
    >>> for nf in range(104):
    ...     plt.polar(A.phi,abs(A.Ft[45,:,nf]))


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-11-f991f6d8f1a6> in <module>()
    ----> 1 plt.figure(figsize=(10,10))
          2 for nf in range(104):
          3     plt.polar(A.phi,abs(A.Ft[45,:,nf]))


    NameError: name 'plt' is not defined


.. code:: python

    >>> A.info()
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


::


      File "<ipython-input-12-837bfeceeb4d>", line 3
        type :  mat
             ^
    SyntaxError: invalid syntax



Evaluation of Vector Spherical Harmonics Coefficients
=====================================================

At that stage we compute the Vector Spherical Harmonics coefficients

.. code:: python

    >>> A=vsh(A)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-aab26d118494> in <module>()
    ----> 1 A=vsh(A)
    

    NameError: name 'vsh' is not defined


.. code:: python

    >>> A.info()
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


::


      File "<ipython-input-14-837bfeceeb4d>", line 3
        type :  mat
             ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.C.s1tos2(30)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-15-98aa5dfbfef3> in <module>()
    ----> 1 A.C.s1tos2(30)
    

    NameError: name 'A' is not defined


.. code:: python

    >>> A.C
    Br
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495
    
    Bi
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495
    
    Cr
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495
    
    Ci
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495


::


      File "<ipython-input-16-aa32a992ae2e>", line 3
        -------------
                     ^
    SyntaxError: invalid syntax



.. code:: python

    >>> fig = plt.figure(figsize=(8,8))
    >>> A.C.show('s2',k=300)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-17-a2dac715dfe4> in <module>()
    ----> 1 fig = plt.figure(figsize=(8,8))
          2 A.C.show('s2',k=300)


    NameError: name 'plt' is not defined


.. code:: python

    >>> A.C.s2tos3()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-18-34ddad199ddd> in <module>()
    ----> 1 A.C.s2tos3()
    

    NameError: name 'A' is not defined


.. code:: python

    >>> A.C
    Br
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495
    Ncoeff s3 : 145
    
    Bi
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495
    Ncoeff s3 : 145
    
    Cr
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495
    Ncoeff s3 : 145
    
    Ci
    -------------
    L1  : 90
    M1  : 89
    Ncoeff s1 8010
    NCoeff s2  : 495
    Ncoeff s3 : 145


::


      File "<ipython-input-19-e5635a621117>", line 3
        -------------
                     ^
    SyntaxError: invalid syntax



.. code:: python

    >>> fig = plt.figure(figsize=(8,8))
    >>> A.C.show('s3')
    >>> plt.tight_layout()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-20-627adf1c1577> in <module>()
    ----> 1 fig = plt.figure(figsize=(8,8))
          2 A.C.show('s3')
          3 plt.tight_layout()


    NameError: name 'plt' is not defined

