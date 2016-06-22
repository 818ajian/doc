
Example of Utilisation of Coverage
==================================

.. code:: python

    >>> %matplotlib inline

.. code:: python

    >>> from pylayers.antprop.coverage import *


.. parsed-literal::

    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


.. code:: python

    >>> C = Coverage('cnes.ini')


::


    ---------------------------------------------------------------------------

    NoSectionError                            Traceback (most recent call last)

    <ipython-input-3-704dc907214d> in <module>()
    ----> 1 C = Coverage('cnes.ini')
    

    /home/uguen/Documents/rch/devel/pylayers/pylayers/antprop/coverage.pyc in __init__(self, _fileini)
        102         self.config.read(pyu.getlong(_fileini,pstruc['DIRSIMUL']))
        103 
    --> 104         self.layoutopt = dict(self.config.items('layout'))
        105         self.gridopt   = dict(self.config.items('grid'))
        106         self.apopt     = dict(self.config.items('ap'))


    /home/uguen/anaconda/lib/python2.7/ConfigParser.pyc in items(self, section, raw, vars)
        640         except KeyError:
        641             if section != DEFAULTSECT:
    --> 642                 raise NoSectionError(section)
        643         # Update with the entry specific variables
        644         if vars:


    NoSectionError: No section: 'layout'


.. code:: python

    >>> C


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-b39bfc0e26a3> in <module>()
    ----> 1 C
    

    NameError: name 'C' is not defined


.. code:: python

    >>> fig=figure(figsize=(10,10))
    >>> f,a=C.L.showGs(fig=fig)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-308e8a4b41f8> in <module>()
    ----> 1 fig=figure(figsize=(10,10))
          2 f,a=C.L.showGs(fig=fig)


    NameError: name 'figure' is not defined


.. code:: python

    >>> C.L.sl.mat


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-5987c1a5e5e0> in <module>()
    ----> 1 C.L.sl.mat
    

    NameError: name 'C' is not defined


.. code:: python

    >>> C.L.sl


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-233cb0e618ea> in <module>()
    ----> 1 C.L.sl
    

    NameError: name 'C' is not defined


.. code:: python

    >>> C.L.sla


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-9941b6287d95> in <module>()
    ----> 1 C.L.sla
    

    NameError: name 'C' is not defined


.. code:: python

    >>> C.cover()


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-0e75a4f1a346> in <module>()
    ----> 1 C.cover()
    

    NameError: name 'C' is not defined


.. code:: python

    >>> fig=plt.figure(figsize=(14,8))
    >>> a1 = fig.add_subplot(121)
    >>> a2 = fig.add_subplot(122)
    >>> f,a = C.show(typ='pr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
    >>> f,a = C.show(typ='pr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-85139ae1f152> in <module>()
          2 a1 = fig.add_subplot(121)
          3 a2 = fig.add_subplot(122)
    ----> 4 f,a = C.show(typ='pr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
          5 f,a = C.show(typ='pr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


    NameError: name 'C' is not defined



.. image:: CNES_files/CNES_10_1.png


.. code:: python

    >>> fig=plt.figure(figsize=(14,8))
    >>> a1 = fig.add_subplot(121)
    >>> a2 = fig.add_subplot(122)
    >>> f,a = C.show(typ='loss',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
    >>> f,a = C.show(typ='loss',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-3e022033b6de> in <module>()
          2 a1 = fig.add_subplot(121)
          3 a2 = fig.add_subplot(122)
    ----> 4 f,a = C.show(typ='loss',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
          5 f,a = C.show(typ='loss',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


    NameError: name 'C' is not defined



.. image:: CNES_files/CNES_11_1.png


.. code:: python

    >>> fig=plt.figure(figsize=(14,8))
    >>> a1 = fig.add_subplot(121)
    >>> a2 = fig.add_subplot(122)
    >>> f,a = C.show(typ='snr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
    >>> f,a = C.show(typ='snr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-2ba6eb5982ea> in <module>()
          2 a1 = fig.add_subplot(121)
          3 a2 = fig.add_subplot(122)
    ----> 4 f,a = C.show(typ='snr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
          5 f,a = C.show(typ='snr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


    NameError: name 'C' is not defined



.. image:: CNES_files/CNES_12_1.png


.. code:: python

    >>> fig=plt.figure(figsize=(14,8))
    >>> a1 = fig.add_subplot(121)
    >>> a2 = fig.add_subplot(122)
    >>> f,a = C.show(typ='sinr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
    >>> f,a = C.show(typ='sinr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-41038f4b7d64> in <module>()
          2 a1 = fig.add_subplot(121)
          3 a2 = fig.add_subplot(122)
    ----> 4 f,a = C.show(typ='sinr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
          5 f,a = C.show(typ='sinr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)


    NameError: name 'C' is not defined



.. image:: CNES_files/CNES_13_1.png


.. code:: python

    >>> fig=plt.figure(figsize=(14,8))
    >>> a1 = fig.add_subplot(121)
    >>> a2 = fig.add_subplot(122)
    >>> f,a = C.show(typ='capacity',best=False,polar='o',vmin=0,fig=fig,ax=a1)
    >>> f,a = C.show(typ='capacity',best=False,polar='p',vmin=0,fig=fig,ax=a2)


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-99eac4ac2ce0> in <module>()
          2 a1 = fig.add_subplot(121)
          3 a2 = fig.add_subplot(122)
    ----> 4 f,a = C.show(typ='capacity',best=False,polar='o',vmin=0,fig=fig,ax=a1)
          5 f,a = C.show(typ='capacity',best=False,polar='p',vmin=0,fig=fig,ax=a2)


    NameError: name 'C' is not defined



.. image:: CNES_files/CNES_14_1.png

