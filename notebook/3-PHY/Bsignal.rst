
Handling time and frequency domain signals : ``Bsignal`` Class
==============================================================

This section presents some features of the classes implemented in the
```pylayers.signal.bsignal.py`` <http://pylayers.github.io/pylayers/modules/pylayers.signal.bsignal.html>`__
module.

.. code:: python

    >>> %matplotlib inline

The ``Bsignal`` class is a container for a signal with a base which can
be either in time domain or frequency domain.

.. code:: python

    >>> from pylayers.signal.bsignal import *
    >>> from matplotlib.pyplot import *

As a first example, let construct an impulse signal normalized in
energy. To do so there exist a specialized function :
```EnImpulse`` <http://pylayers.github.io/pylayers/modules/generated/pylayers.signal.bsignal.EnImpulse.demo.html#pylayers.signal.bsignal.EnImpulse.demo>`__

.. code:: python

    >>> E=TUsignal()
    >>> E.EnImpulse(feGHz=40)

.. code:: python

    >>> E.plot(typ='v')
    (<matplotlib.figure.Figure at 0x7f8b08493810>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8ad8a32b10>]], dtype=object))


::


      File "<ipython-input-4-b8188bec7e2d>", line 2
        (<matplotlib.figure.Figure at 0x7f8b08493810>,
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> E.energy()
    array([ 1.00000008])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-5-174dc6ac1499> in <module>()
          1 E.energy()
    ----> 2 array([ 1.00000008])
    

    NameError: name 'array' is not defined


The Fourier transform of this signal exhibits the Hermitian Symmetry.

.. code:: python

    >>> F = E.fft()
    >>> F.plot(typ='m')
    (<matplotlib.figure.Figure at 0x7f8ad89e0c50>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8ad8a05e90>]], dtype=object))


::


      File "<ipython-input-6-1b3eb1d96d0c>", line 3
        (<matplotlib.figure.Figure at 0x7f8ad89e0c50>,
         ^
    SyntaxError: invalid syntax



We then extract the non redundant part of the signal with the ``ft``
method

.. code:: python

    >>> G=E.ft()

.. code:: python

    >>> GH=G.symHz(100,scale='extract')

.. code:: python

    >>> print GH.y[0,1]
    >>> print GH.y[0,-1]
    (-0.0014441784194-4.88037298122e-05j)
    (-0.0014441784194+4.88037298122e-05j)


.. parsed-literal::

    (-0.0014441784194-4.88037298122e-05j)
    (-0.0014441784194+4.88037298122e-05j)




.. parsed-literal::

    (-0.0014441784194+4.88037298122e-05j)



.. code:: python

    >>> ip = F.ifft()
    >>> ip2= GH.ifft()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-10-ae009e105e46> in <module>()
    ----> 1 ip = F.ifft()
          2 ip2= GH.ifft()


    NameError: name 'F' is not defined


.. code:: python

    >>> f,a=E.plot(typ='v',labels=['original'])
    >>> f,a=ip.plot(typ='v',fig=f,ax=a[0][0],labels=['no zero padding'])
    >>> f,a=ip2.plot(typ='v',fig=f,ax=a[0][0],labels=['zero padding'])
    >>> title('extract mode')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-11-883c18d72357> in <module>()
          1 f,a=E.plot(typ='v',labels=['original'])
    ----> 2 f,a=ip.plot(typ='v',fig=f,ax=a[0][0],labels=['no zero padding'])
          3 f,a=ip2.plot(typ='v',fig=f,ax=a[0][0],labels=['zero padding'])
          4 title('extract mode')


    NameError: name 'ip' is not defined



.. image:: Bsignal_files/Bsignal_15_1.png


.. code:: python

    >>> ip.energy()
    array([ 1.00000008])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-12-e6e568d2f2a7> in <module>()
    ----> 1 ip.energy()
          2 array([ 1.00000008])


    NameError: name 'ip' is not defined


.. code:: python

    >>> ip2.energy()
    array([ 3.18478273])


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-4359c1b169c8> in <module>()
    ----> 1 ip2.energy()
          2 array([ 3.18478273])


    NameError: name 'ip2' is not defined


.. code:: python

    >>> Y=E.esd()

FHsignal in CIR mode
--------------------

We create a Fusignal which corresponds to the signal

.. math:: X_u(f) = \alpha e^{-2j\pi f \tau}

.. math:: f\in [f_{min},f_{max}]

.. code:: python

    >>> fGHz = np.arange(2,10,0.01)
    >>> tau = 20
    >>> y = 2*np.ones(len(fGHz))*np.exp(-2*1j*np.pi*fGHz*tau)
    >>> Hu = FUsignal(fGHz,y)

.. code:: python

    >>> Hu.plot(typ='m')
    >>> Hu.plot(typ='r')
    (<matplotlib.figure.Figure at 0x7f8ad84b6050>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8ad84630d0>]], dtype=object))


::


      File "<ipython-input-16-657abc9f240b>", line 3
        (<matplotlib.figure.Figure at 0x7f8ad84b6050>,
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> hu = Hu.ifft()

The inverse Fourier transform allows to recover perfectly the amplitude
:math:`\alpha` and the delay :math:`\tau` of the channel

.. code:: python

    >>> hu.plot(typ='m')
    (<matplotlib.figure.Figure at 0x7f8ad838ec90>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8ad84b6c90>]], dtype=object))


::


      File "<ipython-input-18-b15cd1d053cd>", line 2
        (<matplotlib.figure.Figure at 0x7f8ad838ec90>,
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> real=np.imag(hu.y)
    >>> u = np.where(hu.y==max(hu.y))[0]
    >>> tau = hu.x[u]
    >>> alpha = abs(hu.y[u])

.. code:: python

    >>> H = Hu.symHz(100,scale='cir')

.. code:: python

    >>> H.plot(typ='m')
    (<matplotlib.figure.Figure at 0x7f8ad8282450>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8ad8312f10>]], dtype=object))


::


      File "<ipython-input-21-4831ff917ddd>", line 2
        (<matplotlib.figure.Figure at 0x7f8ad8282450>,
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> h = H.ifft()

.. code:: python

    >>> h.plot(typ='v')
    (<matplotlib.figure.Figure at 0x7f8ad81c6890>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8ad83565d0>]], dtype=object))


::


      File "<ipython-input-23-dcd459f2597c>", line 2
        (<matplotlib.figure.Figure at 0x7f8ad81c6890>,
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> real=np.imag(h.y)
    >>> u = np.where(h.y==max(h.y))[0]
    >>> tau = h.x[u]
    >>> alpha = abs(h.y[u])

.. code:: python

    >>> fft.ifft(H.y)
    array([[ -1.50593859e-15 -6.41964563e-20j,
              1.22745263e-04 -1.36427337e-19j,
              8.94216494e-05 -1.03247967e-19j, ...,
              1.05839739e-05 +7.80645228e-20j,
             -1.37135712e-04 -1.94405223e-19j,
              8.17123442e-05 +3.02799103e-19j]])


::


      File "<ipython-input-25-36e1760b7cc0>", line 4
        8.94216494e-05 -1.03247967e-19j, ...,
                                         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> print H.y[...,203]
    >>> print H.y[...,-203]
    >>> len(H.y)
    [-0.10108118-0.07343977j]
    [-0.10108118+0.07343977j]
    1


.. parsed-literal::

    [-0.10108118-0.07343977j]
    [-0.10108118+0.07343977j]




.. parsed-literal::

    1



.. code:: python

    >>> Y=h.fft()

.. code:: python

    >>> Y.plot(typ='m')
    (<matplotlib.figure.Figure at 0x7f8ad836ec90>,
     array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f8ad8491590>]], dtype=object))


::


      File "<ipython-input-28-4130b11ec3d3>", line 2
        (<matplotlib.figure.Figure at 0x7f8ad836ec90>,
         ^
    SyntaxError: invalid syntax


