
Indoor Coverage with the PyLayers Multi Wall model
==================================================

A Multi wall model accounts only for the attenuation along the direct
path between Tx and Rx.

This approach do not provide information about delay spread or multi
paths but it can nevertheless be useful in different contexts, as i.e
optimization of an indoor radio network. The MultiWall approach provides
a fast rough indication about the propagation losses.

A ray tracing approach is much more accurate, but also is much more time
consuming and depending on the purpose, it is relevant to proceed with a
simpler and faster site-specific approach as the Multiwall model.

**``PyLayers``** provides a multiwall module which heavily relies on the
core class **``Slab``**. Notice that, the same core **``Slab``** module
is used for Ray tracing and MultiWall model approaches.

Let's see, how it works. First let's import the ``coverage`` module. And
the ``time`` module for performance evaluation.

.. code:: python

    >>> from pylayers.antprop.coverage import *
    >>> from matplotlib.pyplot import *
    >>> %matplotlib inline
    >>> import time

Instantiate a coverage object. By defaut the ``TA-Office.ini`` layout is
loaded.

The coverage information is placed in the **coverage.ini** file in the
project directory.

Below is an example such a configuration file.

.. code:: python

    >>> !cat $BASENAME/ini/coverage.ini
    [grid]
    nx = 40
    ny = 20
    boundary = [20,0,30,20]
    mode = full ; file, zone , full 
    file = 'points.ini'
    
    [layout]
    filename = TA-Office.ini ; 0 40 0 15
    ;filename = W2PTIN.ini
    ;filename = Lstruc.str
    
    [ap]
    0 = {'name':'room1','wstd':'ieee80211b','p':(1,12,1.2),'PtdBm':0,'chan':[11],'on':True} 
    1 = {'name':'room2','wstd':'ieee80211b','p':(10,2,1.2),'PtdBm':0,'chan':[11],'on':True} 
    2 = {'name':'room3','wstd':'ieee80211b','p':(20,1,1.2),'PtdBm':0,'chan':[11],'on':True} 
    3 = {'name':'room4','wstd':'ieee80211b','p':(36.5,1.5,1.2),'PtdBm':0,'chan':[11],'on':True} 
    4 = {'name':'room5','wstd':'ieee80211b','p':(25,12,1.2),'PtdBm':0,'chan':[11],'on':True} 
    
    [rx]
    temperaturek = 300
    noisefactordb = 0 
    
    [show]
    show = True


::


      File "<ipython-input-2-0545b412e6f3>", line 10
        filename = TA-Office.ini ; 0 40 0 15
                                      ^
    SyntaxError: invalid syntax



The ini file contains 5 sections.

-  [grid] section This section precises the size of the grid. By default
   the grid is placed over the whole region of the Layout. A selected
   region can also be defined whith the ``boundary`` list
-  [layout] section The name of the layout file (filename = )
-  [ap] section A dictionnary of access points precising the standard,
   the used channel, the emitted power and the position of the access
   point.

-  [show] section

.. code:: python

    >>> # Create a Coverage object from coverag.ini file
    ... C = Coverage('coverage.ini')


.. parsed-literal::

    building Layout ...


::


    

    MultipleInstanceErrorTraceback (most recent call last)

    <ipython-input-3-33376351d131> in <module>()
          1 # Create a Coverage object from coverag.ini file
    ----> 2 C = Coverage('coverage.ini')
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/coverage.pyc in __init__(self, _fileini)
        110         if filename.endswith('ini'):
        111             self.typ = 'indoor'
    --> 112             self.L = Layout(filename)
        113 
        114             # get the receiving grid


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in __init__(self, _filename, _filematini, _fileslabini, _filefur, force, check, build, verbose)
        422 
        423 
    --> 424         self.load(_filename,build=build)
        425 
        426 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in load(self, _filename, build)
       1624                     # if ans.lower()=='y':
       1625 
    -> 1626                     self.build()
       1627                     self.lbltg.append('s')
       1628                     self.dumpw()


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4786             if verbose:
       4787                 print "Gv"
    -> 4788             self.buildGv()
       4789             self.lbltg.extend('v')
       4790 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGv(self, show)
       7065                 for idiff in ndiffvalid:
       7066 
    -> 7067                     import ipdb
       7068                     # ipdb.set_trace()
       7069                     # if (icycle==2) & (idiff==-2399):


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__init__.py in <module>()
          5 # https://opensource.org/licenses/BSD-3-Clause
          6 
    ----> 7 from ipdb.__main__ import set_trace, post_mortem, pm, run             # noqa
          8 from ipdb.__main__ import runcall, runeval, launch_ipdb_on_exception  # noqa
          9 


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__main__.py in <module>()
         56     # the instance method will create a new one without loading the config.
         57     # i.e: if we are in an embed instance we do not want to load the config.
    ---> 58     ipapp = TerminalIPythonApp.instance()
         59     shell = get_ipython()
         60     def_colors = shell.colors


    /home/uguen/anaconda2/lib/python2.7/site-packages/traitlets/config/configurable.pyc in instance(cls, *args, **kwargs)
        414             raise MultipleInstanceError(
        415                 'Multiple incompatible subclass instances of '
    --> 416                 '%s are being created.' % cls.__name__
        417             )
        418 


    MultipleInstanceError: Multiple incompatible subclass instances of TerminalIPythonApp are being created.


``C`` has a dictionnary ``dap`` (dictionnary of access points) which
gathers information about each access points of the scene.

.. code:: python

    >>> C.dap[1]
    name : room2
    p : (10, 2, 1.2)
    PtdBm : 0
    channels  : [11]   2.462 : [2.451,2.473]
    sensdBm : -94
    nant : 1
    On : True


::


      File "<ipython-input-4-9dba40a6bb5a>", line 2
        name : room2
             ^
    SyntaxError: invalid syntax



The coverage object has a ``__repr__`` method which summarizes different
parameters of the current coverage object

.. code:: python

    >>> C
    Layout file : TA-Office.ini
    
    -----list of Access Points ------
    name : room1
    p : (1, 12, 1.2)
    PtdBm : 0
    channels  : [11]   2.462 : [2.451,2.473]
    sensdBm : -94
    nant : 1
    On : True
    
    name : room2
    p : (10, 2, 1.2)
    PtdBm : 0
    channels  : [11]   2.462 : [2.451,2.473]
    sensdBm : -94
    nant : 1
    On : True
    
    name : room3
    p : (20, 1, 1.2)
    PtdBm : 0
    channels  : [11]   2.462 : [2.451,2.473]
    sensdBm : -94
    nant : 1
    On : True
    
    name : room4
    p : (36.5, 1.5, 1.2)
    PtdBm : 0
    channels  : [11]   2.462 : [2.451,2.473]
    sensdBm : -94
    nant : 1
    On : True
    
    name : room5
    p : (25, 12, 1.2)
    PtdBm : 0
    channels  : [11]   2.462 : [2.451,2.473]
    sensdBm : -94
    nant : 1
    On : True
    
    -----Rx------
    temperature (K) : 300
    noisefactor (dB) : 0
    
    --- Grid ----
    mode : full
    nx : 40
    ny : 20


::


      File "<ipython-input-5-cb35b139978f>", line 2
        Layout file : TA-Office.ini
                  ^
    SyntaxError: invalid syntax



.. code:: python

    >>> C.cover()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-6-0e75a4f1a346> in <module>()
    ----> 1 C.cover()
    

    NameError: name 'C' is not defined


Let display the current Layout with hidding nodes.

.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> C.L.display['nodes']=False
    >>> C.L.display['ednodes']=False
    >>> f,a = C.show(fig=fig)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-7-d7bbaf68c62a> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 C.L.display['nodes']=False
          3 C.L.display['ednodes']=False
          4 f,a = C.show(fig=fig)


    NameError: name 'C' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f0768650>


The shadowing map coverage results can be displayed by invoquing various
functions.

.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> f,a=C.show(fig=fig,typ='pr')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-8-e2637ddfd59f> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 f,a=C.show(fig=fig,typ='pr')
    

    NameError: name 'C' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f2beac10>


.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> f,a=C.show(fig=fig,typ='pr',f=4)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-9-387b085bdc21> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 f,a=C.show(fig=fig,typ='pr',f=4)
    

    NameError: name 'C' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f2b6b590>


.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> f,a=C.show(fig=fig,typ='pr',f=10)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-10-acaa5ae5e147> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 f,a=C.show(fig=fig,typ='pr',f=10)
    

    NameError: name 'C' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f0753790>


.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> f,a=C.show(fig=fig,typ='best',f=1)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-11-6eca5a6da0b8> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 f,a=C.show(fig=fig,typ='best',f=1)
    

    NameError: name 'C' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f07539d0>


.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> f,a=C.show(fig=fig,typ='best',f=10)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-12-7fabaad1dbb9> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 f,a=C.show(fig=fig,typ='best',f=10)
    

    NameError: name 'C' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f04fb390>


.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> f=C.show(fig=fig,f=5,typ='sinr')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-e9aa4be471c9> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 f=C.show(fig=fig,f=5,typ='sinr')
    

    NameError: name 'C' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f04fbe10>


As you have noticed the calculation has been done for all the center
frequencies of the selected standard. This is done in prevision of
further channel optimizations.

Let's consider an other standard

.. code:: python

    >>> C2 = Coverage('coverage2.ini')
    >>> C2.cover()


.. parsed-literal::

    building Layout ...


::


    

    MultipleInstanceErrorTraceback (most recent call last)

    <ipython-input-14-a22e5c85a032> in <module>()
    ----> 1 C2 = Coverage('coverage2.ini')
          2 C2.cover()


    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/coverage.pyc in __init__(self, _fileini)
        110         if filename.endswith('ini'):
        111             self.typ = 'indoor'
    --> 112             self.L = Layout(filename)
        113 
        114             # get the receiving grid


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in __init__(self, _filename, _filematini, _fileslabini, _filefur, force, check, build, verbose)
        422 
        423 
    --> 424         self.load(_filename,build=build)
        425 
        426 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in load(self, _filename, build)
       1624                     # if ans.lower()=='y':
       1625 
    -> 1626                     self.build()
       1627                     self.lbltg.append('s')
       1628                     self.dumpw()


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in build(self, graph, verbose)
       4786             if verbose:
       4787                 print "Gv"
    -> 4788             self.buildGv()
       4789             self.lbltg.extend('v')
       4790 


    /home/uguen/Documents/rch/devel/pylayers/pylayers/gis/layout.pyc in buildGv(self, show)
       7065                 for idiff in ndiffvalid:
       7066 
    -> 7067                     import ipdb
       7068                     # ipdb.set_trace()
       7069                     # if (icycle==2) & (idiff==-2399):


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__init__.py in <module>()
          5 # https://opensource.org/licenses/BSD-3-Clause
          6 
    ----> 7 from ipdb.__main__ import set_trace, post_mortem, pm, run             # noqa
          8 from ipdb.__main__ import runcall, runeval, launch_ipdb_on_exception  # noqa
          9 


    /home/uguen/anaconda2/lib/python2.7/site-packages/ipdb/__main__.py in <module>()
         56     # the instance method will create a new one without loading the config.
         57     # i.e: if we are in an embed instance we do not want to load the config.
    ---> 58     ipapp = TerminalIPythonApp.instance()
         59     shell = get_ipython()
         60     def_colors = shell.colors


    /home/uguen/anaconda2/lib/python2.7/site-packages/traitlets/config/configurable.pyc in instance(cls, *args, **kwargs)
        414             raise MultipleInstanceError(
        415                 'Multiple incompatible subclass instances of '
    --> 416                 '%s are being created.' % cls.__name__
        417             )
        418 


    MultipleInstanceError: Multiple incompatible subclass instances of TerminalIPythonApp are being created.


.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> f=C2.show(ftyp='pr')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-15-82e55d16c1d6> in <module>()
          1 fig=figure(figsize=(10,5))
    ----> 2 f=C2.show(ftyp='pr')
    

    NameError: name 'C2' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x7fc2f0506bd0>


.. code:: python

    >>> C.snro.shape
    (13, 800, 5)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-16-03db730d9be3> in <module>()
    ----> 1 C.snro.shape
          2 (13, 800, 5)


    NameError: name 'C' is not defined


.. code:: python

    >>> fig=figure(figsize=(10,5))
    >>> C.show(fig=fig,f=5,typ='capacity',dB=False)
    (<matplotlib.figure.Figure at 0x7f3ea6200ed0>,
     <matplotlib.axes._subplots.AxesSubplot at 0x7f3e9e473310>)


::


      File "<ipython-input-17-04064cb4f222>", line 3
        (<matplotlib.figure.Figure at 0x7f3ea6200ed0>,
         ^
    SyntaxError: invalid syntax



All simulated quantities are stored in linear scale.

.. code:: python

    >>> C2.Lwo[0,0,0]
    0.078045027166146197


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-18-11161e2f0b4f> in <module>()
    ----> 1 C2.Lwo[0,0,0]
          2 0.078045027166146197


    NameError: name 'C2' is not defined


.. code:: python

    >>> C2.freespace[0,0,0]
    8.520773206944774e-07


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-19-78eefcf9aad5> in <module>()
    ----> 1 C2.freespace[0,0,0]
          2 8.520773206944774e-07


    NameError: name 'C2' is not defined

