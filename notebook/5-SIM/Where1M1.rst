
WHERE1-M1 UWB measurement campaign
==================================

.. code:: python

    %matplotlib inline

.. code:: python

    from pylayers.simul.simulem import *
    from pylayers.antprop.rays import *
    from pylayers.antprop.channel import *
    from pylayers.antprop.antenna import *
    from pylayers.antprop.signature import *
    from pylayers.measures.mesuwb import *
    import pylayers.util.pyutil as pyu
    import pylayers.signal.bsignal as bs


.. parsed-literal::

    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b8fd7a9bb90>


The deliverable describing the FP7 WHERE1 measurement campaign M1 can be
found @ `WHERE1 D4.1 Measurements of location-dependent channel
features <http://www.kn-s.dlr.de/where/documents/Deliverable41.pdf>`__

Simulation Creation
-------------------

A ray-tracing simulation is controlled via a configuration file which is
stored in the ``ini`` directory of the project directory. By default,
there is a default configuration file named ``default.ini``.

A first step consists in loading a layout associated with the
simulation. Here the ``WHERE1.ini`` layout is chosen along with the
corresponding slabs and materials.

This layout corresponds to the office building where the first WHERE1
UWB measurement campaign has been conducted.

The layout method loads those in a member layout object **L** of the
simulation object **S**.

If not already available, the layout associated graphs are built.

.. code:: python

    S = Simul()
    # loading a layout
    filestr = 'WHERE1'
    S.layout(filestr+'.ini','matDB.ini','slabDB.ini')
    try:
        S.L.dumpr()
    except:
        S.L.build()
        S.L.dumpw()


.. parsed-literal::

    new file WHERE1.str


.. code:: python

    f,a=S.L.showG('s',figsize=(16,8),nodes=False)


.. parsed-literal::

    /home/uguen/anaconda/lib/python2.7/site-packages/matplotlib/collections.py:650: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      if self._edgecolors_original != str('face'):
    /home/uguen/anaconda/lib/python2.7/site-packages/matplotlib/collections.py:590: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      if self._edgecolors == str('face'):



.. image:: Where1M1_files/Where1M1_11_1.png


.. code:: python

    S.L._showGi(en=17)
    plt.axis('off')


.. parsed-literal::

    int0 :  (220, 58, 61)
    int1 :  (216, 61)
     output  {(223, 61): 4.631245566616953e-05, (189, 61): 0.52059781654978099, (213, 61): 0.99999999999997502, (222, 61): 0.42854915043759029, (207, 61, 60): 0.015898410593098666, (213, 61, 59): 0.99999999999997502, (207, 61): 0.015898410593098666, (223, 61, 57): 4.631245566616953e-05, (205, 61): 0.074214608852340755, (189, 61, 70): 0.52059781654978099, (205, 61, 60): 0.074214608852340755}




.. parsed-literal::

    (-31.123950000000001, 34.74295, 3.6289500000000001, 24.594305147086835)




.. image:: Where1M1_files/Where1M1_12_2.png


The layout display is fully parameterized via the embedded **display**
dictionnary member of the Layout object.

.. code:: python

    fig = plt.figure(figsize=(10,5))
    S.L.display['ednodes']=False
    S.L.display['nodes']=False
    S.L.display['title']='WHERE1 Project Office Measurement Site'
    fig,ax=S.L.showGs(fig=fig)



.. image:: Where1M1_files/Where1M1_14_0.png


.. code:: python

    S.L.Gi.edges()[0]




.. parsed-literal::

    ((274, 55, 54), (286, 52, 55))



Adding coordinates of transmiting and receiving points
------------------------------------------------------

Transmitters and receivers coordinates for the simulation are stored in
**.ini** files. Transmitter and Receiver are instances of the class
``RadioNode`` which offers different methods for specifying nodes
positions. The stucture of this **.ini** file presented below. The node
Id is associated with the 3 coordinates :math:`x,y,z` separated by white
spaces.

::

    [coordinates]
    1 = -12.2724 7.76319999993 1.2
    2 = -18.7747 15.1779999998 1.2
    3 = -4.14179999998 8.86029999983 1.2
    4 = -9.09139999998 15.1899000001 1.2

.. code:: python

    S.tx = RadioNode(_fileini='w2m1rx.ini',_fileant='defant.vsh3')
    S.rx = RadioNode(_fileini='w2m1tx.ini',_fileant='defant.vsh3')

The whole simulation setup can then be displayed using the **show**
method of the Simulation object

.. code:: python

    fig = plt.figure(figsize=(10,5))
    fig,ax = S.show()


.. parsed-literal::

    Warning : no furniture file loaded



.. image:: Where1M1_files/Where1M1_21_1.png


Select Tx and Rx positions

.. code:: python

    map={1: 1,2: 2, 3: 3, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10,
    10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20,
    20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27,
    27: 28, 28: 29, 29: 30, 30: 32, 31: 33, 32: 34, 33: 35, 34: 36, 35: 37, 36: 38,
          37: 39, 38: 40, 39: 41, 40: 42, 41: 43, 42: 44, 43: 45, 44: 46, 45: 47,
          46: 48, 47: 49, 48: 50, 49: 51, 50: 52, 51: 53, 52: 54, 53: 55, 54: 56,
          55: 57, 56: 58, 57: 59, 58: 60, 59: 61, 60: 62, 61: 63, 62: 64, 63: 65,
          64: 66, 65: 67, 66: 68, 67: 69, 68: 70, 69: 71, 70: 72, 71: 73, 72: 74,
          73: 75, 74: 76, 75: 77, 76: 78, 77: 79, 78: 80, 79: 81, 80: 82, 81: 83,
          82: 84, 83: 85, 84: 89, 85: 90, 86: 91, 87: 92, 88: 93, 89: 94, 90: 95,
          91: 96, 92: 97, 93: 98, 94: 99, 95: 100, 96: 101, 97: 103, 98: 104, 99:
          105, 100: 106, 101: 107, 102: 108, 103: 109, 104: 110, 105: 111, 106:
          113, 107: 114, 108: 116, 109: 117, 110: 119, 111: 120, 112: 122, 113:
          123, 114: 124, 115: 125, 116: 126, 117: 127, 118: 128, 119: 129, 120:
          133, 121: 134, 122: 136, 123: 137, 124: 138, 125: 139, 126: 140, 127:
          141, 128: 142, 129: 143, 130: 144, 131: 145, 132: 146, 133: 147, 134:
          162, 135: 163, 136: 164, 137: 165, 138: 166, 139: 167, 140: 168, 141:
          169, 142: 170, 143: 171, 144: 172, 145: 173, 146: 174, 147: 175, 148:
          176, 149: 177, 150: 179, 151: 180, 152: 181, 153: 182, 154: 183, 155:
          184, 156: 185, 157: 186, 158: 188, 159: 189, 160: 199, 161: 200, 162:
          201, 163: 202, 164: 203, 165: 204, 166: 205, 167: 206, 168: 207, 169:
          208, 170: 209, 171: 210, 172: 211, 173: 212, 174: 213, 175: 214, 176:
          215, 177: 216, 178: 217, 179: 218, 180: 219, 181: 220, 182: 221, 183:
          222, 184: 223, 185: 227, 186: 228, 187: 229, 188: 230, 189: 231, 190:
          232, 191: 233, 192: 234, 193: 235, 194: 236, 195: 237, 196: 238, 197:
          239, 198: 240, 199: 241, 200: 242, 201: 243, 202: 244, 203: 245, 204:
          246, 205: 247, 206: 248, 207: 249, 208: 250, 209: 251, 210: 252, 211:
          253, 212: 258, 213: 259, 214: 266, 215: 267, 216: 268, 217: 269, 218:
          270, 219: 271, 220: 272, 221: 273, 222: 274, 223: 275, 224: 276, 225:
          277, 226: 278, 227: 279, 228: 297, 229: 298, 230: 299, 231: 300, 232:
          301, 233: 302, 234: 303, 235: 304, 236: 305, 237: 306, 238: 307, 239:
          308, 240: 309, 241: 310, 242: 311, 243: 312, 244: 313, 245: 314, 246:
          315, 247: 316, 248: 317, 249: 318, 250: 319, 251: 320, 252: 321, 253:
          322, 254: 323, 255: 324, 256: 325, 257: 326, 258: 327, 259: 328, 260:
          329, 261: 330, 262: 332, 263: 333, 264: 334, 265: 335, 266: 336, 267:
          337, 268: 338, 269: 339, 270: 340, 271: 341, 272: 342, 273: 343, 274:
          344, 275: 345, 276: 346, 277: 347, 278: 348, 279: 349, 280: 350, 281:
          351, 282: 352, 283: 353, 284: 354, 285: 355, 286: 356, 287: 360, 288:
          361, 289: 362, 290: 363, 291: 364, 292: 365, 293: 366, 294: 367, 295:
          368, 296: 369, 297: 370, 298: 371, 299: 372, 300: 373, 301: 374, 302:
          375}

.. code:: python

    print 'number of Tx :',len(S.tx.points.keys())
    print 'number of rx :',len(S.rx.points.keys())


.. parsed-literal::

    number of Tx : 302
    number of rx : 4


Choose measurement points

.. code:: python

    # Chose used points here
    itx=10
    irx=2
    # check points
    tx= S.tx.points[itx]
    rx= S.rx.points[irx]
    M = UWBMeasure(map[itx])
    txm = M.tx
    rxm = M.rx[irx]
    print tx,txm
    print rx,rxm
    v = np.sum((tx-rx)*(tx-rx))
    
    
    if (tx[0] - txm[0] > 0.001) or (tx[1] - txm[1] > 0.001):
        print 'Tx and Txm are not the same !'
    else :
        print 'Txs OK'
    if (rx[0] - rxm[0] > 0.001) or (rx[1] - rxm[1] > 0.001):
        print 'Rx and Rxm are not the same !'
    else :
        print 'Rxs OK'


.. parsed-literal::

    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong
    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong
    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong
    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong
    [-24.867   12.3097   1.2   ] [-24.867   12.3097   1.2   ]
    [-18.7747  15.178    1.2   ] [-18.7747  15.178    1.2   ]
    Txs OK
    Rxs OK


.. parsed-literal::

    /home/uguen/Documents/rch/devel/pylayers/pylayers/measures/mesuwb.py:993: FutureWarning: elementwise != comparison failed and returning scalar instead; this will raise an error or perform elementwise comparison in the future.
      if d != []:


.. code:: python

    M.tdd.ch1.y.shape




.. parsed-literal::

    (1, 40000)



.. code:: python

    fig =plt.figure(figsize=(16,8))
    fig,ax=S.L.showG('s',fig=fig)
    ax.plot(M.tx[0],M.tx[1],'or',label='tx')
    ax.plot(M.rx[irx][0],M.rx[irx][1],'ob',label='rx')
    ax.legend()




.. parsed-literal::

    <matplotlib.legend.Legend at 0x2b8fd85783d0>




.. image:: Where1M1_files/Where1M1_28_1.png


Signatures, Rays and Radio Channel
----------------------------------

A signature is a sequence of layout objects (points and segments) which
are involved in a given optical ray joint the transmiter and the
receiver. The signatutre is calculated from a layout cycle to an other
layout cycle. This means that is is required first to retrieve the cycle
number from point coordinates. This is done thanks to the **pt2cy**,
point to cycle function.

.. code:: python

    ctx=S.L.pt2cy(tx)
    crx=S.L.pt2cy(rx)
    print 'tx point belongs to cycle ',ctx
    print 'rx point belongs to cycle ',crx


.. parsed-literal::

    tx point belongs to cycle  7
    rx point belongs to cycle  4


Then the signature between 2 given cycle can be calculated. This is done
by instantiating a Signature object with a given layout and the 2 cycle
number.

The representaion of a signature objet

.. code:: python

    Si = Signatures(S.L,ctx,crx)
    Si.run5(cutoff=3)

.. code:: python

    tx[2]=1.5

.. code:: python

    r2d = Si.rays(tx,rx)
    r3d = r2d.to3D(S.L)


::


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-18-ef07e5b83169> in <module>()
    ----> 1 r2d = Si.rays(tx,rx)
          2 r3d = r2d.to3D(S.L)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/signature.pyc in rays(self, ptx, prx)
       4623                     # --> sig2ray
       4624 
    -> 4625                     isray,Yi  = s.sig2ray(self.L, ptx[:2], prx[:2])
       4626 
       4627                     if isray:


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/signature.pyc in sig2ray(self, L, pTx, pRx, mode)
       5881         self.ev(L)
       5882         # calculates images from pTx
    -> 5883         M = self.image(pTx)
       5884         #print self
       5885         #if np.array_equal(self.seq,np.array([5,7,4])):


    AttributeError: 'Signature' object has no attribute 'image'


.. code:: python

    fig = plt.figure(figsize=(10,10))
    r2d.show(L=S.L,fig=fig)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-7a057e2d7c22> in <module>()
          1 fig = plt.figure(figsize=(10,10))
    ----> 2 r2d.show(L=S.L,fig=fig)
    

    NameError: name 'r2d' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b8fd88a0090>


.. code:: python

    r3d.locbas(S.L)
    r3d.fillinter(S.L)
    r3d


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-ca9247e523cf> in <module>()
    ----> 1 r3d.locbas(S.L)
          2 r3d.fillinter(S.L)
          3 r3d


    NameError: name 'r3d' is not defined


.. code:: python

    S.freq()[0:10]




.. parsed-literal::

    array([ 2.  ,  2.05,  2.1 ,  2.15,  2.2 ,  2.25,  2.3 ,  2.35,  2.4 ,  2.45])



.. code:: python

    Ct = r3d.eval(S.freq())


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-22-3d2a58b0e4d6> in <module>()
    ----> 1 Ct = r3d.eval(S.freq())
    

    NameError: name 'r3d' is not defined


The ``energy`` method calculates the energy of each ray

.. code:: python

    Ett,Epp,Etp,Ept = Ct.energy()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-5a542a3e037f> in <module>()
    ----> 1 Ett,Epp,Etp,Ept = Ct.energy()
    

    NameError: name 'Ct' is not defined


.. code:: python

    plt.subplot(121)
    plt.plot(Ct.tauk,10*np.log10(Ett),'ob',label=r'$\theta\theta$')
    plt.plot(Ct.tauk,10*np.log10(Epp),'or',label=r'$\phi\phi$')
    plt.ylim(-160,-60)
    plt.xlabel('delay(ns)')
    plt.ylabel('Ray Energy (dB)')
    plt.legend()
    plt.subplot(122)
    plt.plot(Ct.tauk,10*np.log10(Ept),'og',label =r'$\phi\theta$')
    plt.plot(Ct.tauk,10*np.log10(Etp),'oc',label = r'$\theta\phi$')
    plt.ylim(-160,-60)
    plt.legend()
    plt.xlabel('delay(ns)')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-24-ed03cfaffe60> in <module>()
          1 plt.subplot(121)
    ----> 2 plt.plot(Ct.tauk,10*np.log10(Ett),'ob',label=r'$\theta\theta$')
          3 plt.plot(Ct.tauk,10*np.log10(Epp),'or',label=r'$\phi\phi$')
          4 plt.ylim(-160,-60)
          5 plt.xlabel('delay(ns)')


    NameError: name 'Ct' is not defined



.. image:: Where1M1_files/Where1M1_43_1.png


Apply waveform
--------------

.. code:: python

    Aa= Antenna('defant.vsh3')
    Ab= Antenna('defant.vsh3')

.. code:: python

    Ct.freq = S.freq
    sco= Ct.prop2tran()
    sca= Ct.prop2tran(a=Aa,b=Ab)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-f59dd2910f4c> in <module>()
    ----> 1 Ct.freq = S.freq
          2 sco= Ct.prop2tran()
          3 sca= Ct.prop2tran(a=Aa,b=Ab)


    NameError: name 'Ct' is not defined


.. code:: python

    wav = wvf.Waveform(typ='W1offset')
    #wav = wvf.Waveform({'type' : 'generic','band': 0.499,'fc': 4.493, 'fe': 100, 'thresh': 3, 'tw': 30})
    wav.show()


.. parsed-literal::

    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong
    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong
    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong
    DEPRECATION WARNING : geomutil.angular going deprecatd  because wrong



.. image:: Where1M1_files/Where1M1_47_1.png


.. code:: python

    sco.isFriis


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-28-483cb18240de> in <module>()
    ----> 1 sco.isFriis
    

    NameError: name 'sco' is not defined


.. code:: python

    if sco.isFriis:
        ciro = sco.applywavB(wav.sf)
    else:
        ciro = sco.applywavB(wav.sfg)
    if sca.isFriis:
        cira = sca.applywavB(wav.sf)
    else:
         cira = sca.applywavB(wav.sfg)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-29-32aad411a377> in <module>()
    ----> 1 if sco.isFriis:
          2     ciro = sco.applywavB(wav.sf)
          3 else:
          4     ciro = sco.applywavB(wav.sfg)
          5 if sca.isFriis:


    NameError: name 'sco' is not defined


.. code:: python

    ciro.plot(typ='v')
    f=plt.title(u'received waveform without antenna $\\theta\\theta$')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-30-32970dcb6f93> in <module>()
    ----> 1 ciro.plot(typ='v')
          2 f=plt.title(u'received waveform without antenna $\\theta\\theta$')


    NameError: name 'ciro' is not defined


.. code:: python

    cira.plot(typ='v')
    f=plt.title('received waveform with antenna')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-ec3ee7283c4d> in <module>()
    ----> 1 cira.plot(typ='v')
          2 f=plt.title('received waveform with antenna')


    NameError: name 'cira' is not defined


.. code:: python

    #dchan={i:'ch'+str(i) for i in range(1,5)}
    dchan={}
    dchan[1]='ch3'
    dchan[2]='ch4'
    dchan[3]='ch1'
    dchan[4]='ch2'

.. code:: python

    M.show()



.. image:: Where1M1_files/Where1M1_53_0.png




.. parsed-literal::

    (<matplotlib.figure.Figure at 0x2b8fd9318810>,
     <matplotlib.axes._subplots.AxesSubplot at 0x2b8fd8d97c90>)



.. code:: python

    fig = plt.figure(figsize=(10,6))
    ax1 = fig.add_subplot(311,title="Measurements")
    cmd='M.tdd.' + str(dchan[irx]) + '.plot(ax=ax1)'
    eval(cmd)
    plt.title('WHERE1 measurement')
    #M.tdd.ch2.plot()
    # align for plotting
    #ciro.x=ciro.x-ciro.x[0]
    ax2 = fig.add_subplot(312,title="Simulation-with antenna",sharex=ax1, sharey=ax1)
    plt.xlim(20,70)
    plt.ylim(-95,-50)
    u = cira.plot(ax=ax2)
    plt.title('Simulation-with antenna - without noise')
    plt.tight_layout()
    #ax3 = fig.add_subplot(313,title="Simulation-without antenna",sharex=ax1, sharey=ax1)
    #ciro.plot()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-34-7ab773200d86> in <module>()
         10 plt.xlim(20,70)
         11 plt.ylim(-95,-50)
    ---> 12 u = cira.plot(ax=ax2)
         13 plt.title('Simulation-with antenna - without noise')
         14 plt.tight_layout()


    NameError: name 'cira' is not defined



.. image:: Where1M1_files/Where1M1_54_1.png


.. code:: python

    r3d.info(0)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-35-9db4433723d2> in <module>()
    ----> 1 r3d.info(0)
    

    NameError: name 'r3d' is not defined


.. code:: python

    f,a=Ct.doadod(phi=(-180,180),cmap='copper')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-36-deb54e4502f7> in <module>()
    ----> 1 f,a=Ct.doadod(phi=(-180,180),cmap='copper')
    

    NameError: name 'Ct' is not defined

