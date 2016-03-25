# Scalar Spherical Harmonics

```python
>>> from pylayers.antprop.antenna import *
>>> from pylayers.antprop.antssh import *
>>> %matplotlib inline
WARNING:traits.has_traits:DEPRECATED: traits.has_traits.wrapped_class, 'the 'implements' class advisor has been deprecated. Use the 'provides' class decorator.
```

```python
>>> A = Antenna('S1R1.mat',directory='ant/UWBAN/Matfile')
```

```python
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
```

```python
>>> A.nf
104
```

To calculate scalar spherical harmonics use method `ssh(A,L)`

```python
>>> L = 5
>>> A = ssh(A,L=5)
```

```python
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
```

```python
>>> plt.plot(abs(A.S.Cx.s2[0]))
[<matplotlib.lines.Line2D at 0x7fe754161bd0>]
```

```python
>>> A.savesh2()
create  /home/uguen/Bureau/P1/ant/S1R1.sh2  file
```

```python
>>> A.loadsh2()
```

```python
>>> plt.plot(abs(A.S.Cx.s2[0]))
[<matplotlib.lines.Line2D at 0x7fe7540d0b90>]
```

```python
>>> A.S.s2tos3()
```

```python
>>> plt.plot(abs(A.S.Cx.s3[0]))
[<matplotlib.lines.Line2D at 0x7fe753d11510>]
```

```python
>>> A.S.Cx.ind2.shape
(36, 2)
```

```python
>>> A.savesh3()
/home/uguen/Bureau/P1/ant/S1R1.sh3  already exist
```

```python
>>> plt.plot(abs(A.S.Cx.s2[0]))
[<matplotlib.lines.Line2D at 0x7fe753c51250>]
```

```python
>>> A.loadsh3()
```

```python
>>> plt.plot(abs(A.S.Cx.s3[100]))
[<matplotlib.lines.Line2D at 0x7fe753b8f150>]
```

```python
>>> plt.plot(abs(A.S.Cx.s2[100]))
[<matplotlib.lines.Line2D at 0x7fe753acac90>]
```

```python
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
```

```python
>>> A.S.Cx.__dict__.keys()
['k2', 'ind3', 'ind2', 'fmax', 's2', 'Nf', 's3', 'lmax', 'fmin']
```

```python
>>> A.S.Cx
Nf   : 104
fmin (GHz) : 0.8
fmax (GHz) : 5.95
NCoeff s2  : 36
Ncoeff s3 : 143
```
