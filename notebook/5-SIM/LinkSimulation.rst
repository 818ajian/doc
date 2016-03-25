
.. code:: python

    from pylayers.simul.link import *
    %matplotlib inline
    import seaborn as sns
    sns.set_style("dark")


.. parsed-literal::

    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


How to do Ray Tracing simulation using DLink
============================================

This section illustrates the
```link`` <http://pylayers.github.io/pylayers/modules/pylayers.simul.link.html>`__
module. A ``Dlink`` object is a deterministic (Single Input Single
Output) SISO link.

.. code:: python

    L=DLink()


::


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-2-8d488aedce1d> in <module>()
    ----> 1 L=DLink()
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/simul/link.pyc in __init__(self, **kwargs)
        344         Link.__init__(self)
        345 
    --> 346         defaults={ 'L':Layout(),
        347                    'a':np.array(()),
        348                    'b':np.array(()),


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in __init__(self, _filename, _filematini, _fileslabini, _filefur, force, check)
        410         # check layout integrity (default)
        411         if check:
    --> 412             self.check()
        413         #self.boundary()
        414 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in check(self, level)
        719             deg0 = filter(lambda x: nx.degree(self.Gs,x)==0,upnt)
        720             deg1 = filter(lambda x: nx.degree(self.Gs,x)==1,upnt)
    --> 721             assert (len(deg0)==0), "It exists degree 0 points :  %r" % deg0
        722             assert (len(deg1)==0), "It exists degree 1 points : %r" % deg1
        723 


    AssertionError: It exists degree 0 points :  [-18, -17, -16, -15, -14]


.. code:: python

    L.show()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-58cf57214d72> in <module>()
    ----> 1 L.show()
    

    NameError: name 'L' is not defined


.. code:: python

    L


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-42f463c84796> in <module>()
    ----> 1 L
    

    NameError: name 'L' is not defined


.. code:: python

    L.eval?


.. parsed-literal::

    Object `L.eval` not found.


To evaluate a link there is the ``eval`` method. This method takes as
argument + a list of the desired outputs, + the type of algorithm being
used, + the ceil heigh + the number of multi reflection between ceil and
floor.

.. code:: python

    L.R.show(L=L.L,figsize=(10,10))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-9af88b4b0cbf> in <module>()
    ----> 1 L.R.show(L=L.L,figsize=(10,10))
    

    NameError: name 'L' is not defined


.. code:: python

    L.H.taud


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-13b539339ef6> in <module>()
    ----> 1 L.H.taud
    

    NameError: name 'L' is not defined


.. code:: python

    aktk=L.eval(force=[], output=['sig','ray','Ct','H'],
                si_algo='old',ra_ceil_height_meter=3,ra_number_mirror_cf=1)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-4725e09794ec> in <module>()
    ----> 1 aktk=L.eval(force=[], output=['sig','ray','Ct','H'],
          2             si_algo='old',ra_ceil_height_meter=3,ra_number_mirror_cf=1)


    NameError: name 'L' is not defined


.. code:: python

    plt.stem(aktk[1],aktk[0])


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-54a8ce6633a9> in <module>()
    ----> 1 plt.stem(aktk[1],aktk[0])
    

    NameError: name 'aktk' is not defined


The propagation channel (without antenna) can be vizualized on a ray by
ray mode.

.. code:: python

    type(L.C)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-6365d47278c3> in <module>()
    ----> 1 type(L.C)
    

    NameError: name 'L' is not defined


.. code:: python

    #L._show3()sns.set_style("dark")

.. code:: python

    fig = plt.figure(figsize=(8,8))
    C = L.C
    f,a = C.show(cmap='jet',fig=fig,typ='l10',vmin=-100,vmax=-10)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-33da1547e63a> in <module>()
          1 fig = plt.figure(figsize=(8,8))
    ----> 2 C = L.C
          3 f,a = C.show(cmap='jet',fig=fig,typ='l10',vmin=-100,vmax=-10)


    NameError: name 'L' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2b2dd5566bd0>


It is possible to look at individual ray transfer function, as
illustrated below.

.. code:: python

    C.Ctt.y.shape


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-692d6a37642f> in <module>()
    ----> 1 C.Ctt.y.shape
    

    NameError: name 'C' is not defined


.. code:: python

    ir = 80
    plt.plot(C.Ctt.x,abs(C.Ctt.y[ir,:]))
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Level (linear)')
    plt.title('Modulus of the ray '+str(ir)+' transfer function')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-b982fe6f7874> in <module>()
          1 ir = 80
    ----> 2 plt.plot(C.Ctt.x,abs(C.Ctt.y[ir,:]))
          3 plt.xlabel('Frequency (GHz)')
          4 plt.ylabel('Level (linear)')
          5 plt.title('Modulus of the ray '+str(ir)+' transfer function')


    NameError: name 'C' is not defined


.. code:: python

    ir = 30
    plt.plot(C.Ctt.x,abs(C.Ctt.y[ir,:]))
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Level (linear)')
    plt.title('Modulus of the ray '+str(ir)+' transfer function')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-cc3e93bb836b> in <module>()
          1 ir = 30
    ----> 2 plt.plot(C.Ctt.x,abs(C.Ctt.y[ir,:]))
          3 plt.xlabel('Frequency (GHz)')
          4 plt.ylabel('Level (linear)')
          5 plt.title('Modulus of the ray '+str(ir)+' transfer function')


    NameError: name 'C' is not defined


In the link we also have the transmission channel accounting for the
effect of antennas and Friis factor. If the ray transfer function is
scaled with :math:`\frac{4\pi f}{c}`

.. code:: python

    plt.plot(L.H.x,L.H.y[0,:]*4*np.pi*L.H.x/0.3)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-68e484174013> in <module>()
    ----> 1 plt.plot(L.H.x,L.H.y[0,:]*4*np.pi*L.H.x/0.3)
    

    NameError: name 'L' is not defined


Notice that in this case the frequency

The infinite bandwidth channel impulse response is plotted below from
the extrated set :math:`\{\alpha_k,\tau_k\}`.

.. code:: python

    plt.stem(aktk[1],aktk[0])
    plt.title('Infinite bandwith Channel Impulse response')
    plt.xlabel('delay (ns)')
    plt.ylabel('amplitude (linear scale')


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-fed48e39015b> in <module>()
    ----> 1 plt.stem(aktk[1],aktk[0])
          2 plt.title('Infinite bandwith Channel Impulse response')
          3 plt.xlabel('delay (ns)')
          4 plt.ylabel('amplitude (linear scale')


    NameError: name 'aktk' is not defined


.. code:: python

    import pylayers.simul.simulnet as sn
    import pylayers.simul.simultraj as st


::


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-18-f6ed6fa7963a> in <module>()
    ----> 1 import pylayers.simul.simulnet as sn
          2 import pylayers.simul.simultraj as st


    /home/uguen/Documents/rch/devel/pylayers/pylayers/simul/simulnet.py in <module>()
         62 import pylayers.util.pyutil as pyu
         63 
    ---> 64 from pylayers.network.network import Network, Node, PNetwork
         65 from pylayers.network.communication import Gcom
         66 from pylayers.network.show import ShowNet, ShowTable


    /home/uguen/Documents/rch/devel/pylayers/pylayers/network/network.py in <module>()
        151 #from PyLayers.Network.Node import Node
        152 import pylayers.util.pyutil as pyu
    --> 153 from pylayers.network.emsolver import EMSolver
        154 from pylayers.network.show import ShowNet,ShowTable
        155 #from pylayers.util.pymysqldb import Database


    /home/uguen/Documents/rch/devel/pylayers/pylayers/network/emsolver.py in <module>()
         42 
         43 
    ---> 44 class EMSolver(object):
         45     """ Invoque an electromagnetic solver
         46 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/network/emsolver.py in EMSolver()
         71     """
         72 
    ---> 73     def __init__(self,L=Layout()):
         74 
         75         self.config  = ConfigParser.ConfigParser()


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in __init__(self, _filename, _filematini, _fileslabini, _filefur, force, check)
        410         # check layout integrity (default)
        411         if check:
    --> 412             self.check()
        413         #self.boundary()
        414 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in check(self, level)
        719             deg0 = filter(lambda x: nx.degree(self.Gs,x)==0,upnt)
        720             deg1 = filter(lambda x: nx.degree(self.Gs,x)==1,upnt)
    --> 721             assert (len(deg0)==0), "It exists degree 0 points :  %r" % deg0
        722             assert (len(deg1)==0), "It exists degree 1 points : %r" % deg1
        723 


    AssertionError: It exists degree 0 points :  [-18, -17, -16, -15, -14]


.. code:: python

    S=sn.Simul()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-550d145b7b04> in <module>()
    ----> 1 S=sn.Simul()
    

    NameError: name 'sn' is not defined


.. code:: python

    S.L


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-225e20c8deb9> in <module>()
    ----> 1 S.L
    

    NameError: name 'S' is not defined


.. code:: python

    S.runsimul()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-21-e96c93b86265> in <module>()
    ----> 1 S.runsimul()
    

    NameError: name 'S' is not defined


.. code:: python

    dB=True
    from pylayers.mobility.trajectory import *

A trajectories object is a list of trajectories. The loadh5 methods by
default loads the file '.h5' generated by
```Simulnet`` <http://pylayers.github.io/pylayers/modules/pylayers.simul.simulnet.html>`__.

.. code:: python

    T=Trajectories()
    T.loadh5()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-c93f9b6c2ae9> in <module>()
          1 T=Trajectories()
    ----> 2 T.loadh5()
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/mobility/trajectory.pyc in loadh5(self, _filename, append)
        143             fil = pd.HDFStore(filename)
        144         else:
    --> 145             raise NameError(filename + ' not found')
        146         if not append:
        147             [self.pop(0) for i in range(len(self))]


    NameError: /home/uguen/Bureau/P1/netsave/simulnet_TA-Office.h5 not found


.. code:: python

    T




.. parsed-literal::

    Issue in Trajectories. Are you sure any Trajectory is loaded ?



A SimulTraj object is derived from a trajectory calculated previously in
simulnet and a body agent description. The Simultraj object get the
trajectories from the ``simultaj.ini`` file.

.. code:: python

    St=st.Simul(verbose=False)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-25-ae27233a0375> in <module>()
    ----> 1 St=st.Simul(verbose=False)
    

    NameError: name 'st' is not defined


.. code:: python

    #St.run(t=list(np.arange(0,1,0.1)),OB=True,B2B=True,B2I=True)

.. code:: python

    #St.data

Information about the simulated network is obtained

.. code:: python

    St.N


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-28-292f54c77c9f> in <module>()
    ----> 1 St.N
    

    NameError: name 'St' is not defined


.. code:: python

    #St._show3()

.. code:: python

    #St.data.head()

.. code:: python

    #ak,tk,ek=St._loadh5(2,'0_Alex','1_Alex','bluetooth-class2')

.. code:: python

    #stem(tk,ak)

