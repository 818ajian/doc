
.. code:: python

    >>> %pylab inline


.. parsed-literal::

    Populating the interactive namespace from numpy and matplotlib


Synthesis of Ultra Wide Band Waveforms
--------------------------------------

Once the propagation channel has been evaluated. This is done in the
``pylayers.antprop.channel`` module. The received signal is evaluated in
applying a convolution product of each ray tranfer function with a
specific IR-UWB waveform. The necessary modules are

-  ``pylayers.signal.bsignal``.
-  ``pylayers.signal.waveform``
-  ``pylayers.signal.channel``

The module ``pylayers.simul.simulem`` is for definition of
electromagnetic simulation.

.. code:: python

    >>> from pylayers.signal.bsignal import *
    >>> from pylayers.signal.waveform import *
    >>> from pylayers.antprop.channel import *
    >>> from pylayers.simul.simulem import *

Generation of an Impulse of normalized energy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One possible manner to define an energy normalized short UWB impulse is
as follows using ``bsignal.EnImpulse`` function.

The default waveform is a gaussian windowing of a sine wave of frequency
:math:`f_c`. The normalization term depends on the exponential scaling
factor :math:`\tau`.

:math:`p(t)= \frac{\sqrt{2\sqrt{2}}}{\tau\sqrt{\pi}} \cos(2\pi f_c t) e^{-(\frac{t}{\tau})^2}`

:math:`\tau = \frac{2}{B\pi}\sqrt{\frac{\gamma_{dB}\ln{10}}{20}}`

where :math:`B` is the desired bandwidth defined at :math:`\gamma_{dB}`
below the spectrum maximum and :math:`f_c` is the central frequency of
the pulse.

.. code:: python

    >>> fc     = 4
    >>> band   = 2
    >>> thresh = 10
    >>> fe     = 100
    >>> ip     = EnImpulse([],fc,band,thresh,fe)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-3-eb9e61732349> in <module>()
          3 thresh = 10
          4 fe     = 100
    ----> 5 ip     = EnImpulse([],fc,band,thresh,fe)
    

    NameError: name 'EnImpulse' is not defined


.. code:: python

    >>> ip.info()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-4-f2dd061e0735> in <module>()
    ----> 1 ip.info()
    

    NameError: name 'ip' is not defined


Verification of energy normalization in both domains
----------------------------------------------------

.. code:: python

    >>> E1= sum(ip.y*ip.y)*ip.dx()
    >>> print "Integration in time",E1


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-5-2ff960551bb1> in <module>()
    ----> 1 E1= sum(ip.y*ip.y)*ip.dx()
          2 print "Integration in time",E1


    NameError: name 'ip' is not defined


.. code:: python

    >>> P = ip.esd()
    >>> E2 = sum(P.y)*P.dx()
    >>> print "Integration in frequency domain ",E2


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-6-f88fbaeebaf0> in <module>()
    ----> 1 P = ip.esd()
          2 E2 = sum(P.y)*P.dx()
          3 print "Integration in frequency domain ",E2


    NameError: name 'ip' is not defined


Calculation of UWB channel impulse response
-------------------------------------------

We choose to load a simple floor plan.

.. code:: python

    >>> S = Simul()
    >>> S.L = Layout('defstr3.ini')


.. parsed-literal::

    new file defstr3.ini


A simulation object has an ``info`` method providing a summary of
simulation informations.

.. code:: python

    >>> st = S.wav.st
    >>> sf = S.wav.sf
    >>> S.wav.info()


.. parsed-literal::

    fcGHz  :  4.493
    typ  :  generic
    feGHz  :  100
    Np  :  3000
    twns  :  30
    te  :  0.01
    threshdB  :  3
    bandGHz  :  0.499


The waveform associated with the simulation object is

.. code:: python

    >>> S.wav




.. parsed-literal::

    {'Np': 3000,
     'bandGHz': 0.499,
     'fcGHz': 4.493,
     'feGHz': 100,
     'te': 0.01,
     'threshdB': 3,
     'twns': 30,
     'typ': 'generic'}



.. code:: python

    >>> S.wav.show()



.. image:: Signal_files/Signal_15_0.png


Above the waveform is a generic UWB waveform. The interested user can
add easyly any other mathematical expression of UWB waveform for
investigation on pulse waveform modulation for example. The waveform can
also comes from measurement. For now there are two version of this
waveform which has been used during the M1 measurement campaign. One is
not compensated ``W1compensate`` for an extra short delay which can
introduse a bias when interpretating the observed delay in terms of
distance. The non compensated version is ``W1offset`` from the time
origin about 0.7 ns.

The waveform class should grow for incorporating more waveforms,
especially waveforms compliants with the current IEEE 802.15.4a and IEEE
802.15.6 standards.

.. code:: python

    >>> wavmeasured = Waveform(typ='W1compensate')
    >>> wavmeasured.show()


::


    

    IndexErrorTraceback (most recent call last)

    <ipython-input-11-22a822769751> in <module>()
          1 wavmeasured = Waveform(typ='W1compensate')
    ----> 2 wavmeasured.show()
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/signal/waveform.pyc in show(self, fig)
        382         #plt.title(title)
        383         ax1 = fig.add_subplot(2,1,1)
    --> 384         ax1.plot(self.st.x,self.st.y[0,:])
        385         plt.xlabel('time (ns)')
        386         plt.ylabel('level in linear scale')


    IndexError: too many indices for array



.. image:: Signal_files/Signal_17_1.png


.. code:: python

    >>> wavmeasured = Waveform(typ='W1offset')
    >>> wavmeasured.show()



.. image:: Signal_files/Signal_18_0.png


Here the time domain waveform is measured and the anticausal part of the
signal is artificially set to 0.

To handle properly the time domain wavefom in PyLayers, it is required
to center the signal in the middle of the array. The waveform has
embedded in the object its frequency domain and time domain
representation.

-  ``st`` member stands for signal in time domain
-  ``sf`` member stands for signal in frequency domain

.. code:: python

    >>> print type(S.wav.sf)
    >>> print type(S.wav.st)


.. parsed-literal::

    <class 'pylayers.signal.bsignal.FUsignal'>
    <class 'pylayers.signal.bsignal.TUsignal'>


-  ``FUsignal`` Frequency domain uniformly sampled base signal
-  ``TUsignal`` Time domain uniformly sampled base signal

Construction of the propagation channel
---------------------------------------

The following representation shows the spatial spreading of the
propagation channel. On the left are scattered the intensity of rays wrt
to angles of departure (in azimut and elevation). On the right is the
intensity of rays wrt to angles of arrival. It misses the application
between the 2 planes as well as the delay dimension of the propagation
channel.

.. code:: python

    >>> from pylayers.antprop.signature import *
    >>> from pylayers.antprop.channel import *

.. code:: python

    >>> S.L.build()


.. parsed-literal::

    building Layout ...


::


    

    KeyErrorTraceback (most recent call last)

    <ipython-input-15-775c93de59f6> in <module>()
    ----> 1 S.L.build()
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4778             if verbose:
       4779                 print "Gt"
    -> 4780             self.buildGt()
       4781             self.lbltg.extend('t')
       4782 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGt(self, check)
       5451 
       5452             seg = p.vnodes[p.vnodes>0]
    -> 5453             lair = [x in (self.name['AIR']+self.name['_AIR']) for x in seg]
       5454 
       5455             if sum(lair)>0:


    KeyError: 'AIR'


.. code:: python

    >>> S.L




.. parsed-literal::

    
    ----------------
    defstr3.ini
    ----------------
    
    Number of points  : 4
    Number of segments  : 4
    Number of sub segments  : 0
    Number of cycles  : 0
    Number of rooms  : 0
    
    xrange :(-30.0, 30.0)
    yrange :(-20.0, 20.0)
    
    Useful dictionnaries
    ----------------
    name :  {slab :seglist} 
    
    Useful arrays
    ----------------
    
    Useful tip
    ----------------
    Point p in Gs => p_coord:
    p -> u = self.iupnt[-p] -> p_coord = self.pt[:,u]
    
    Segment s in Gs => s_ab coordinates 
    s -> u = self.tgs[s] -> v = self.tahe[:,u] -> s_ab = self.pt[:,v]




.. code:: python

    >>> S.L.Gt.pos




.. parsed-literal::

    {}



.. code:: python

    >>> tx=np.array([759,1114,1.0])
    >>> rx=np.array([767,1114,1.5])
    >>> ctx = S.L.pt2cy(tx)
    >>> crx = S.L.pt2cy(rx)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-18-14f0bff94dac> in <module>()
          1 tx=np.array([759,1114,1.0])
          2 rx=np.array([767,1114,1.5])
    ----> 3 ctx = S.L.pt2cy(tx)
          4 crx = S.L.pt2cy(rx)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in pt2cy(self, pt)
       8381                     return(ncy)
       8382         if not cycle_exists:
    -> 8383             raise NameError(str(pt)+" is not in any cycle")
       8384 
       8385     def cy2pt(self, cy=0, h=1.2):


    NameError: [  7.59000000e+02   1.11400000e+03   1.00000000e+00] is not in any cycle


The sequence of command below :

-  initialize a signature between cycle ctx and cycle crx
-  evaluates the signature with a given cutoff value
-  calculates a set of 2D rays from signature and tx/rx coordinates
-  calculates a set of 3D ray from 2D rays and layout and ceil height
   (default H=3m)
-  calculates local basis and various geometric information out of the
   3D ray and Layout
-  fill and reorganize the interactions object with proper material
   chararcteristics

.. code:: python

    >>> Si = Signatures(S.L,ctx,crx)
    >>> Si.run5(cutoff=5)
    >>> r2d = Si.rays(tx,rx)
    >>> r3d = r2d.to3D(S.L)
    >>> r3d.locbas(S.L)
    >>> r3d.fillinter(S.L)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-19-2b87940b94c6> in <module>()
    ----> 1 Si = Signatures(S.L,ctx,crx)
          2 Si.run5(cutoff=5)
          3 r2d = Si.rays(tx,rx)
          4 r3d = r2d.to3D(S.L)
          5 r3d.locbas(S.L)


    NameError: name 'ctx' is not defined


Define a frequency base in GHz.

.. code:: python

    >>> fGHz = np.arange(2,10,0.01)

Evaluate the propagation channel :math:`\tilde{\mathbf{C}}`. Here the
meaning of tilde is that the complex value of the channel do not include
the phase term due to delay along the ray.

.. code:: python

    >>> C = r3d.eval(fGHz)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-21-6de7eb6ea340> in <module>()
    ----> 1 C = r3d.eval(fGHz)
    

    NameError: name 'r3d' is not defined


Construction of the transmission channel
----------------------------------------

The transmission channel is obtained from the combination of the
propagation channel :math:`\tilde{\mathbf{C}}` and the vector antenna
pattern at both side of the radio link. This operation is implemented in
the ``prop2tran`` method of the ``Ctilde`` class.

.. code:: python

    >>> sc = C.prop2tran()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-22-b1508994e444> in <module>()
    ----> 1 sc = C.prop2tran()
    

    NameError: name 'C' is not defined


The transmission channel is obtained by applying a vector radiation
pattern using an antenna file.

In the presented case, it comes from a real antenna which has been used
during the **FP7 project WHERE1** measurement campaign M1.

.. code:: python

    >>> sc




.. parsed-literal::

    ''



The antenna radiation pattern is stored in a very compact way thanks to
Vector Spherical Harmonics decomposition. The following gives
information about the content of the antenna object.

.. code:: python

    >>> S.tx.A.info()


::


    

    AttributeErrorTraceback (most recent call last)

    <ipython-input-24-405e831617c9> in <module>()
    ----> 1 S.tx.A.info()
    

    AttributeError: 'RadioNode' object has no attribute 'A'


The figure below plot on a same graph all the tansfer function in
modulus and phase of the ray transfer function.

If a realistic antenna is applied it gives

.. code:: python

    >>> sca = C.prop2tran(S.tx.A,S.rx.A)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-25-a14d4505d552> in <module>()
    ----> 1 sca = C.prop2tran(S.tx.A,S.rx.A)
    

    NameError: name 'C' is not defined


Calculate UWB Channel Impulse Response
--------------------------------------

Once the transmission channel has been evaluated on can convolved the
waveform with the channel impulse response to get the received waveform.

.. code:: python

    >>> r = sca.applywavB(S.wav.sfg)


::


    

    AttributeErrorTraceback (most recent call last)

    <ipython-input-26-d44add68b43a> in <module>()
    ----> 1 r = sca.applywavB(S.wav.sfg)
    

    AttributeError: 'function' object has no attribute 'applywavB'


.. code:: python

    >>> r.y


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-27-4953123faa92> in <module>()
    ----> 1 r.y
    

    NameError: name 'r' is not defined


.. code:: python

    >>> fig,ax = r.plot(typ=['l20'])
    >>> plt.axis([15,90,-120,-60])
    >>> plt.title(u'Received Waveform $r(t)$')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-28-59cb5c50134a> in <module>()
    ----> 1 fig,ax = r.plot(typ=['l20'])
          2 plt.axis([15,90,-120,-60])
          3 plt.title(u'Received Waveform $r(t)$')


    NameError: name 'r' is not defined


.. code:: python

    >>> r.plot(typ=['v'])
    >>> #plt.axis([15,60,-0.3,0.3])
    ... plt.title(u'Received Waveform $r(t)$')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-29-dec00a202aac> in <module>()
    ----> 1 r.plot(typ=['v'])
          2 #plt.axis([15,60,-0.3,0.3])
          3 plt.title(u'Received Waveform $r(t)$')


    NameError: name 'r' is not defined


Hermitian symetry enforcment
----------------------------

If the number of point for the transmission channel and the waveform
were the same the mathematical operation is an Hadamrd-Shur product
between :math:`\mathbf{Y}` and :math:`\mathbf{W}`.

:math:`\mathbf{Y} = \mathbf{S} \odot \mathbf{W}`

In practice this is what is done after a resampling of the time base
with a reinterpolated time step.

The process which consists in going from time domain to frequency domain
is delegated to a specialized class ``pylayers.signal.bsignal.Bsignal``
which maintains the proper binding between signal samples and their
indexation either in time or in frequency domain.

.. code:: python

    >>> wgam = S.wav.sfg
    >>> Y    = sc.apply(wgam)
    >>> tau  = Y.taud
    >>> dod = Y.dod
    >>> doa = Y.doa


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-30-3c9fdd777ddd> in <module>()
          1 wgam = S.wav.sfg
    ----> 2 Y    = sc.apply(wgam)
          3 tau  = Y.taud
          4 dod = Y.dod
          5 doa = Y.doa


    NameError: name 'sc' is not defined


The transmission channel has a member data which is the time delay of
each path in nano seconds. Notice that by default those delay are not
sorted.

.. code:: python

    >>> print 'tau =', tau[0:20]


.. parsed-literal::

    tau =

::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-31-b39f17c8cbc1> in <module>()
    ----> 1 print 'tau =', tau[0:20]
    

    NameError: name 'tau' is not defined


.. code:: python

    >>> h = plt.hist(tau,20)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-32-daaa7a3adee0> in <module>()
    ----> 1 h = plt.hist(tau,20)
    

    NameError: name 'tau' is not defined


Direction of arrival :math:`(\theta_r,\phi_r)` in radians

.. code:: python

    >>> print "doa = ", doa[1:10,:]


.. parsed-literal::

     doa = 

::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-33-70fae1c8afa3> in <module>()
    ----> 1 print "doa = ", doa[1:10,:]
    

    NameError: name 'doa' is not defined


.. code:: python

    >>> plt.subplot(221)
    >>> ht = plt.hist(doa[:,0],20)
    >>> plt.xlabel(u'$\\theta_r$')
    >>> plt.ylabel('#')
    >>> plt.subplot(222)
    >>> hp = plt.hist(doa[:,1],20)
    >>> plt.xlabel(u'$\phi_r$')
    >>> plt.ylabel('#')
    >>> plt.subplot(223)
    >>> ht = plt.hist(dod[:,0],20)
    >>> plt.xlabel(u'$\\theta_t$')
    >>> plt.ylabel('#')
    >>> plt.subplot(224)
    >>> hp = plt.hist(dod[:,1],20)
    >>> plt.xlabel(u'$\phi_t$')
    >>> plt.ylabel('#')
    >>> plt.tight_layout()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-34-cfe931a2177d> in <module>()
          1 plt.subplot(221)
    ----> 2 ht = plt.hist(doa[:,0],20)
          3 plt.xlabel(u'$\\theta_r$')
          4 plt.ylabel('#')
          5 plt.subplot(222)


    NameError: name 'doa' is not defined



.. image:: Signal_files/Signal_53_1.png

