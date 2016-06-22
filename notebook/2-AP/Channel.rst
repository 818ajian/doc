
The transmission channel
========================

.. code:: python

    >>> %matplotlib inline

.. code:: python

    >>> from pylayers.antprop.rays import *
    >>> import scipy.fftpack as fft
    >>> from pylayers.gis.layout import *
    >>> from pylayers.antprop.signature import *
    >>> from pylayers.simul.link import *
    >>> import pylayers.signal.bsignal as bs
    >>> import pylayers.signal.waveform as wvf
    >>> from pylayers.simul.simulem import *
    >>> import matplotlib.pyplot as plt
    >>> import time


.. parsed-literal::

    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


We start by constructing a propagation channel with the dedicated class
``DLink``. We specify a Layout as well as the two extremities of the
link. Antennas are also specified. The frequency range is determined by
the frequency range of antennas.

.. code:: python

    >>> L = Layout('defstr3.ini')
    >>> L.Gs.node[1]['ss_name']=['WOOD','AIR','METAL']
    >>> L.build()
    >>> tx=array([759,1114,1.0])
    >>> rx=array([761,1114,1.5])
    >>> fGHz = np.linspace(2,6,401)
    >>> Aa = Antenna('Omni',fGHz=fGHz)
    >>> Ab = Antenna('Omni',fGHz=fGHz)
    >>> Lk = DLink(a=tx,b=rx,Aa=Aa,Ab=Ab)


.. parsed-literal::

    new file defstr3.ini


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-3-5fb46505a749> in <module>()
          1 L = Layout('defstr3.ini')
          2 L.Gs.node[1]['ss_name']=['WOOD','AIR','METAL']
    ----> 3 L.build()
          4 tx=array([759,1114,1.0])
          5 rx=array([761,1114,1.5])


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4691             if verbose:
       4692                 print "Gt"
    -> 4693             self.buildGt()
       4694             self.lbltg.extend('t')
       4695 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGt(self, check)
       5462 
       5463 
    -> 5464         self._find_diffractions()
       5465         #
       5466         #   VIII -  Construct the list of interactions associated to each cycle


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in _find_diffractions(self, tol)
       8467 
       8468         """
    -> 8469         dangles = self.get_Gt_angles()
       8470 
       8471         #


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in get_Gt_angles(self)
       1985         dangles = {}
       1986         for cy in self.Gt.nodes():
    -> 1987             uc,ac = self.get_singlGt_angles(cy,inside=True)
       1988             dangles[cy]=np.array(([uc,ac]))
       1989         return dangles


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in get_singlGt_angles(self, cy, unit, inside)
       1927         # rupt=np.roll(upt,1)         # for debug
       1928         # rupt2=np.roll(upt,-1)         # for debug
    -> 1929         pt = self.pt[:,self.iupnt[-upt]]
       1930         if geu.SignedArea(pt)<0:
       1931             upt = upt[::-1]


    AttributeError: 'Layout' object has no attribute 'pt'


The full evaluation and hdf5 storage of the channel is done with the
``eval`` function. The ``force`` option is for forcing a full
reevaluation.

.. code:: python

    >>> ak,tauk=Lk.eval()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-93695eef2a3c> in <module>()
    ----> 1 ak,tauk=Lk.eval()
    

    NameError: name 'Lk' is not defined


.. code:: python

    >>> f = plt.figure(figsize=(15,15))
    >>> f,a=Lk.C.show(cmap='jet',typ='l20',fig=f,vmin=-100,vmax=-20,fontsize=22)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-b4eee5c9d035> in <module>()
          1 f = plt.figure(figsize=(15,15))
    ----> 2 f,a=Lk.C.show(cmap='jet',typ='l20',fig=f,vmin=-100,vmax=-20,fontsize=22)
    

    NameError: name 'Lk' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b22b93ed2d0>


The transmission channel is stored in ``H``

.. code:: python

    >>> Lk.H


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-345dfe201bf5> in <module>()
    ----> 1 Lk.H
    

    NameError: name 'Lk' is not defined


Once the channel has been calculated, we define an Impulse Radio
Waveform.

.. code:: python

    >>> fGHz=np.arange(2,12,.1)
    >>> wav = wvf.Waveform(fcGHz=5,bandGHz=3)

.. code:: python

    >>> wav.show()



.. image:: Channel_files/Channel_12_0.png


is an object which contains all the information about the propagation
channel.

.. code:: python

    >>> f,a=Lk.show()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-5e7aed51dc8f> in <module>()
    ----> 1 f,a=Lk.show()
    

    NameError: name 'Lk' is not defined


The ``Ctilde`` channel can be sorted with respect to delay

.. code:: python

    >>> Lk.H


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-345dfe201bf5> in <module>()
    ----> 1 Lk.H
    

    NameError: name 'Lk' is not defined


.. code:: python

    >>> len(Lk.fGHz)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-00ef4b2c8627> in <module>()
    ----> 1 len(Lk.fGHz)
    

    NameError: name 'Lk' is not defined


.. code:: python

    >>> f = plt.figure(figsize=(20,10))
    >>> f,a =Lk.H.show(fig=f,cmap='jet')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-f5a32547e4dd> in <module>()
          1 f = plt.figure(figsize=(20,10))
    ----> 2 f,a =Lk.H.show(fig=f,cmap='jet')
    

    NameError: name 'Lk' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b22b93dcb10>


The Friis factor
----------------

The Friis factor is :

.. math:: \alpha=\frac{-jc}{4\pi f}

This factor is fundamental and has to be applied only once. By default
the link is evaluated with the Friis factor :  ``isFriis=True``. This
can be checked at the end of the **repr** of ``H``.

.. code:: python

    >>> Lk.H


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-345dfe201bf5> in <module>()
    ----> 1 Lk.H
    

    NameError: name 'Lk' is not defined


.. code:: python

    >>> Emean=Lk.H.energy(mode='mean')
    >>> Eint=Lk.H.energy(mode='integ')
    >>> Ecenter=Lk.H.energy(mode='center')
    >>> Efirst=Lk.H.energy(mode='first')
    >>> Elast=Lk.H.energy(mode='last')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-86decd824c1e> in <module>()
    ----> 1 Emean=Lk.H.energy(mode='mean')
          2 Eint=Lk.H.energy(mode='integ')
          3 Ecenter=Lk.H.energy(mode='center')
          4 Efirst=Lk.H.energy(mode='first')
          5 Elast=Lk.H.energy(mode='last')


    NameError: name 'Lk' is not defined


.. code:: python

    >>> print Efirst[0],Elast[0]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-4b40c4a26243> in <module>()
    ----> 1 print Efirst[0],Elast[0]
    

    NameError: name 'Efirst' is not defined


On the figure below we have selected a LOS situation and we compare the
energy for each path with the LOS values (the straight line). The 3
straight lines coresponds to the Free space path loss formula for 3
frequencies (f = 2GHz,f=6GHz,f=10GHz). For those 3 frequencies the first
path is perfectly on the curve, which is a validation the observed
level.

.. code:: python

    >>> Lk.H.y.shape


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-3fd9ccc926f4> in <module>()
    ----> 1 Lk.H.y.shape
    

    NameError: name 'Lk' is not defined


.. code:: python

    >>> f1 = 2
    >>> f2 = 10
    >>> f3 = 6
    >>> fig = plt.figure(figsize=(10,5))
    >>> a = plt.semilogx(Lk.H.taud,10*np.log10(Efirst[:,0,0]),'.r',label='f=2GHz')
    >>> a = plt.semilogx(Lk.H.taud,10*np.log10(Emean[:,0,0]),'.b',label='mean')
    >>> a = plt.semilogx(Lk.H.taud,10*np.log10(Elast[:,0,0]),'.g',label='f=10GHz')
    >>> a = plt.semilogx(Lk.H.taud,10*np.log10(Eint[:,0,0]),'.k',label='integral')
    >>> a = plt.semilogx(Lk.H.taud,10*np.log10(Ecenter[:,0,0]),'.c',label='6GHz')
    >>> plt.xlabel(r'$\tau$ (ns)')
    >>> plt.ylabel('Path Loss (dB)')
    >>> LOS1 = -32.4-20*np.log10(Lk.H.taud*0.3)-20*np.log10(f1)
    >>> LOS2 = -32.4-20*np.log10(Lk.H.taud*0.3)-20*np.log10(f2)
    >>> LOS3 = -32.4-20*np.log10(Lk.H.taud*0.3)-20*np.log10(f3)
    >>> plt.semilogx(Lk.H.taud,LOS1,'r')
    >>> plt.semilogx(Lk.H.taud,LOS2,'g')
    >>> plt.semilogx(Lk.H.taud,LOS3,'c')
    >>> plt.semilogx(tauk,20*np.log10(ak),'+')
    >>> plt.ylim([-120,0])
    >>> plt.legend()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-22c3e61e964c> in <module>()
          3 f3 = 6
          4 fig = plt.figure(figsize=(10,5))
    ----> 5 a = plt.semilogx(Lk.H.taud,10*np.log10(Efirst[:,0,0]),'.r',label='f=2GHz')
          6 a = plt.semilogx(Lk.H.taud,10*np.log10(Emean[:,0,0]),'.b',label='mean')
          7 a = plt.semilogx(Lk.H.taud,10*np.log10(Elast[:,0,0]),'.g',label='f=10GHz')


    NameError: name 'Lk' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b22bbbba4d0>


.. code:: python

    >>> a = plt.semilogx(Lk.H.taud,10*np.log10(Emean),'.b',label='mean')
    >>> plt.semilogx(tauk,20*np.log10(ak),'+')
    >>> plt.ylim([-120,0])
    >>> plt.legend()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-79fa43f184e0> in <module>()
    ----> 1 a = plt.semilogx(Lk.H.taud,10*np.log10(Emean),'.b',label='mean')
          2 plt.semilogx(tauk,20*np.log10(ak),'+')
          3 plt.ylim([-120,0])
          4 plt.legend()


    NameError: name 'Lk' is not defined


.. code:: python

    >>> CIR=bs.TUsignal(tauk,np.zeros(len(tauk)))
    >>> CIR.aggcir(ak,tauk)
    >>> CIR.stem()
    >>> plt.title('Infinite bandwidth CIR')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-e688100b13ed> in <module>()
    ----> 1 CIR=bs.TUsignal(tauk,np.zeros(len(tauk)))
          2 CIR.aggcir(ak,tauk)
          3 CIR.stem()
          4 plt.title('Infinite bandwidth CIR')


    NameError: name 'tauk' is not defined


.. code:: python

    >>> MeanDelay = CIR.tau_moy()
    >>> DelaySpread = CIR.tau_rms()
    >>> print MeanDelay,DelaySpread
    37.3831958728 18.5606177248


::


      File "<ipython-input-20-239d3c420603>", line 4
        37.3831958728 18.5606177248
                                  ^
    SyntaxError: invalid syntax



.. code:: python

    >>> f = plt.figure(figsize=(20,10))
    >>> f=Lk.H.show(cmap='jet',fig=f)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-21-61834b1cbc3e> in <module>()
          1 f = plt.figure(figsize=(20,10))
    ----> 2 f=Lk.H.show(cmap='jet',fig=f)
    

    NameError: name 'Lk' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b22bbaca490>


The cut method applies an energy thresholding on the transmission
channel.

.. code:: python

    >>> Lk.H.cut()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-22-c50272a814d0> in <module>()
    ----> 1 Lk.H.cut()
    

    NameError: name 'Lk' is not defined


.. code:: python

    >>> f = plt.figure(figsize=(20,10))
    >>> f=Lk.H.show(cmap='jet',fig=f)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-61834b1cbc3e> in <module>()
          1 f = plt.figure(figsize=(20,10))
    ----> 2 f=Lk.H.show(cmap='jet',fig=f)
    

    NameError: name 'Lk' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b22bbaca9d0>


The tap method
--------------

The tap methods takes as parameters : + The system bandwidth :math:`W`
expressed in MHz + The two extremities velocities :math:`V_a` and
:math:`V_b` + The number of taps to be evaluted :math:`N_{tap}` + The
number of time samples :math:`N_m` + The number of spatial realizations
:math:`N_s`

This method returns a Multi Dimensional Array :math:`htap(f,s,m,tap)`

htap has 4 axes.

-  axis 0 is frequency,
-  axis 1 is spatial realization
-  axis 2 is discrete time
-  axis 3 is tap index

.. code:: python

    >>> Va = 10
    >>> Vb = 10
    >>> fcGHz = 4.5
    >>> Nm = 50
    >>> Ns = 10
    >>> WMHz = 20
    >>> Ntap = 10

.. code:: python

    >>> htap,b,c,d = Lk.H.tap(WMHz=WMHz,Ns=Ns,Nm=Nm,Va=Va,Vb=Vb,Ntap=Ntap)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-25-1e46705dbeb0> in <module>()
    ----> 1 htap,b,c,d = Lk.H.tap(WMHz=WMHz,Ns=Ns,Nm=Nm,Va=Va,Vb=Vb,Ntap=Ntap)
    

    NameError: name 'Lk' is not defined


.. code:: python

    >>> np.shape(htap)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-ac45a4e5a814> in <module>()
    ----> 1 np.shape(htap)
    

    NameError: name 'htap' is not defined


The second parameter is the time integration of htap

-  axis 0 i frequency
-  axis 2 is spatial (realization)
-  axis 2 is tap

.. code:: python

    >>> b.shape
    (161, 10, 10)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-27-9be9b775c895> in <module>()
    ----> 1 b.shape
          2 (161, 10, 10)


    NameError: name 'b' is not defined


.. code:: python

    >>> np.shape(c)
    (161, 50, 10)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-28-0e61c3a383ad> in <module>()
    ----> 1 np.shape(c)
          2 (161, 50, 10)


    NameError: name 'c' is not defined


.. code:: python

    >>> d.shape
    (99,)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-29-50f043f5a600> in <module>()
    ----> 1 d.shape
          2 (99,)


    NameError: name 'd' is not defined


The figure below illustrates the joint frequency and spatial fluctuation
for the first channel tap. :exit

.. code:: python

    >>> img = plt.imshow(abs(b[:,:,0]),interpolation='nearest',extent=(0,1000,fGHz[-1],fGHz[0]))
    >>> plt.axis('tight')
    >>> plt.colorbar()
    >>> plt.xlabel('spatial realizations')
    >>> plt.ylabel('Frequency GHz')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-30-0b5eab508be1> in <module>()
    ----> 1 img = plt.imshow(abs(b[:,:,0]),interpolation='nearest',extent=(0,1000,fGHz[-1],fGHz[0]))
          2 plt.axis('tight')
          3 plt.colorbar()
          4 plt.xlabel('spatial realizations')
          5 plt.ylabel('Frequency GHz')


    NameError: name 'b' is not defined


.. code:: python

    >>> f = plt.figure(figsize=(10,4))
    >>> h = plt.hist(np.real(b[0,:,0])*1e5,40,normed=True)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-67e5429df22c> in <module>()
          1 f = plt.figure(figsize=(10,4))
    ----> 2 h = plt.hist(np.real(b[0,:,0])*1e5,40,normed=True)
    

    NameError: name 'b' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b22bbbba150>


.. code:: python

    >>> mmax = 0.3*WMHz*1e6/(2*fcGHz*(Va+Vb))
    >>> tmaxms = 1000*mmax/(WMHz*1e6)
    >>> plt.imshow(abs(c[:,:,1]),interpolation='nearest',extent=(0,tmaxms,fGHz[-1],fGHz[0]))
    >>> plt.axis('tight')
    >>> plt.colorbar()
    >>> plt.xlabel('Discrete Time (ms)')
    >>> plt.ylabel('frequency (GHz)')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-32-b96e2c6d4018> in <module>()
          1 mmax = 0.3*WMHz*1e6/(2*fcGHz*(Va+Vb))
          2 tmaxms = 1000*mmax/(WMHz*1e6)
    ----> 3 plt.imshow(abs(c[:,:,1]),interpolation='nearest',extent=(0,tmaxms,fGHz[-1],fGHz[0]))
          4 plt.axis('tight')
          5 plt.colorbar()


    NameError: name 'c' is not defined


.. code:: python

    >>> plt.plot(abs(c[0,:,0]))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-33-0f4c005a4ee8> in <module>()
    ----> 1 plt.plot(abs(c[0,:,0]))
    

    NameError: name 'c' is not defined


.. code:: python

    >>> h = c[:,:,2]


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-34-45f737fc79d6> in <module>()
    ----> 1 h = c[:,:,2]
    

    NameError: name 'c' is not defined


.. code:: python

    >>> import scipy.fftpack as fft

.. code:: python

    >>> H = fft.fft(h,axis=1)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-36-7416bec9fa83> in <module>()
    ----> 1 H = fft.fft(h,axis=1)
    

    NameError: name 'h' is not defined


.. code:: python

    >>> plt.imshow(fft.fftshift(abs(H)))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-37-6325b7c4882e> in <module>()
    ----> 1 plt.imshow(fft.fftshift(abs(H)))
    

    NameError: name 'H' is not defined


.. code:: python

    >>> #from pylayers.util.mayautil import *
    ... #m=VolumeSlicer(data=abs(htap[:,0,:,:]))
    ... #m.configure_traits()
