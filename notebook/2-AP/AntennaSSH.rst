
Scalar Spherical Harmonics
==========================

.. code:: python

    >>> from pylayers.antprop.antenna import *
    >>> from pylayers.antprop.antssh import *
    >>> %matplotlib inline
    WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.


::


      File "<ipython-input-1-4506c685f97e>", line 4
        WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.
               ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A = Antenna('S1R1.mat',directory='ant/UWBAN/Matfile')


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-2-e9264d69a718> in <module>()
    ----> 1 A = Antenna('S1R1.mat',directory='ant/UWBAN/Matfile')
    

    NameError: name 'Antenna' is not defined


.. code:: python

    >>> A
    Antenna type : mat
    ------------------------
    file name : S1R1.mat
    fmin : 0.80GHz
    fmax : 5.95GHz
    step : 50.00MHz
    Nf : 104
    -----------------------
          evaluated        
    -----------------------
    Ntheta : 91
    Nphi : 180
       f = 5.60 GHz 
       theta = 70.00 (degrees) 
       phi = 272.00  (degrees)


::


      File "<ipython-input-3-e0e13be6d99a>", line 2
        Antenna type : mat
                   ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.nf
    104


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-4-75576ca402f7> in <module>()
    ----> 1 A.nf
          2 104


    NameError: name 'A' is not defined


To calculate scalar spherical harmonics use method ``ssh(A,L)``

.. code:: python

    >>> L = 5
    >>> A = ssh(A,L=5)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-5-711dcc2ce081> in <module>()
          1 L = 5
    ----> 2 A = ssh(A,L=5)
    

    NameError: name 'ssh' is not defined


.. code:: python

    >>> A
    Antenna type : mat
    ------------------------
    file name : S1R1.mat
    fmin : 0.80GHz
    fmax : 5.95GHz
    step : 50.00MHz
    Nf : 104
    -----------------------
          evaluated        
    -----------------------
    Ntheta : 91
    Nphi : 180
       f = 5.60 GHz 
       theta = 70.00 (degrees) 
       phi = 272.00  (degrees)


::


      File "<ipython-input-6-e0e13be6d99a>", line 2
        Antenna type : mat
                   ^
    SyntaxError: invalid syntax



.. code:: python

    >>> plt.plot(abs(A.S.Cx.s2[0]))
    [<matplotlib.lines.Line2D at 0x7fe754161bd0>]


::


      File "<ipython-input-7-a2c9a12f1b70>", line 2
        [<matplotlib.lines.Line2D at 0x7fe754161bd0>]
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.savesh2()
    create  /home/uguen/Bureau/P1/ant/S1R1.sh2  file


::


      File "<ipython-input-8-47020edc7b1d>", line 2
        create  /home/uguen/Bureau/P1/ant/S1R1.sh2  file
                                                       ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.loadsh2()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-9-73bf83d236c0> in <module>()
    ----> 1 A.loadsh2()
    

    NameError: name 'A' is not defined


.. code:: python

    >>> plt.plot(abs(A.S.Cx.s2[0]))
    [<matplotlib.lines.Line2D at 0x7fe7540d0b90>]


::


      File "<ipython-input-10-0f345f1c16aa>", line 2
        [<matplotlib.lines.Line2D at 0x7fe7540d0b90>]
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.S.s2tos3()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-11-889ab716c956> in <module>()
    ----> 1 A.S.s2tos3()
    

    NameError: name 'A' is not defined


.. code:: python

    >>> plt.plot(abs(A.S.Cx.s3[0]))
    [<matplotlib.lines.Line2D at 0x7fe753d11510>]


::


      File "<ipython-input-12-30b0f3bba346>", line 2
        [<matplotlib.lines.Line2D at 0x7fe753d11510>]
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.S.Cx.ind2.shape
    (36, 2)


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-13-df61edd3218d> in <module>()
    ----> 1 A.S.Cx.ind2.shape
          2 (36, 2)


    NameError: name 'A' is not defined


.. code:: python

    >>> A.savesh3()
    /home/uguen/Bureau/P1/ant/S1R1.sh3  already exist


::


      File "<ipython-input-14-90b51d2b8bf5>", line 2
        home(/uguen/Bureau/P1/ant/S1R1.sh3, already, exist)
             ^
    SyntaxError: invalid syntax



.. code:: python

    >>> plt.plot(abs(A.S.Cx.s2[0]))
    [<matplotlib.lines.Line2D at 0x7fe753c51250>]


::


      File "<ipython-input-15-b65a1e28acc5>", line 2
        [<matplotlib.lines.Line2D at 0x7fe753c51250>]
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.loadsh3()


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-16-ac50ca9ac26e> in <module>()
    ----> 1 A.loadsh3()
    

    NameError: name 'A' is not defined


.. code:: python

    >>> plt.plot(abs(A.S.Cx.s3[100]))
    [<matplotlib.lines.Line2D at 0x7fe753b8f150>]


::


      File "<ipython-input-17-062afa886a4a>", line 2
        [<matplotlib.lines.Line2D at 0x7fe753b8f150>]
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> plt.plot(abs(A.S.Cx.s2[100]))
    [<matplotlib.lines.Line2D at 0x7fe753acac90>]


::


      File "<ipython-input-18-0f567cbda363>", line 2
        [<matplotlib.lines.Line2D at 0x7fe753acac90>]
         ^
    SyntaxError: invalid syntax



.. code:: python

    >>> A.__dict__.keys()
    ['tau',
     'PhotoFile',
     'nf',
     'Fp',
     'Run',
     'source',
     '_filename',
     'param',
     'Serie',
     'Date',
     'theta',
     'fromfile',
     'fGHz',
     'phi',
     'nph',
     'Notes',
     'nth',
     'S',
     'AntennaName',
     'grid',
     'Ft',
     'typ',
     'DataFile',
     'evaluated',
     'ext',
     'StartTime',
     'sqG']


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-19-58c1538184d2> in <module>()
    ----> 1 A.__dict__.keys()
          2 ['tau',
          3  'PhotoFile',
          4  'nf',
          5  'Fp',


    NameError: name 'A' is not defined


.. code:: python

    >>> A.S.Cx.__dict__.keys()
    ['k2', 'ind3', 'ind2', 'fmax', 's2', 'Nf', 's3', 'lmax', 'fmin']


::


    

    NameErrorTraceback (most recent call last)

    <ipython-input-20-094ff156e1a3> in <module>()
    ----> 1 A.S.Cx.__dict__.keys()
          2 ['k2', 'ind3', 'ind2', 'fmax', 's2', 'Nf', 's3', 'lmax', 'fmin']


    NameError: name 'A' is not defined


.. code:: python

    >>> A.S.Cx
    Nf   : 104
    fmin (GHz) : 0.8
    fmax (GHz) : 5.95
    NCoeff s2  : 36
    Ncoeff s3 : 143


::


      File "<ipython-input-21-e4f2123c2b01>", line 2
        Nf   : 104
             ^
    SyntaxError: invalid syntax


