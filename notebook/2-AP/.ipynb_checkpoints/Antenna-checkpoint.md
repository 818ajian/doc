# Description of antennas

PyLayers has a very rich set of tools for handling antenna radiation pattern. Antennas can be described in different manners and read from different specific file formats.

The description goes from a simple antenna gain formula to a full polarization description, compressed or not, using scalar or vector spherical harmonics decomposition.

In the following, some features of the `Antenna` class are illustrated.
The  `Antenna` class is stored in the [antenna.py](http://pylayers.github.io/pylayers/modules/pylayers.antprop.antenna.html) module which is placed in the `antprop` module.

```python
>>> from pylayers.antprop.antenna import *
>>> %pylab inline
Populating the interactive namespace from numpy and matplotlib
WARNING: pylab import has clobbered these variables: ['mlab', 'plt', 'rc']
`%matplotlib` prevents importing * from pylab and numpy
```

An antenna object can not be loaded in specifying an existing antenna file name as argument of the constructor. Lets start by loading an antenna from a `vsh3` file which correspond to a vector spherical harmonics representation of an antenna measured in SATIMO near field chamber.

```python
>>> A = Antenna('S1R1.vsh3')
```

The object antenna can show itself just by typing it's name.

```python
>>> A
Antenna type : vsh3
------------------------
file name : S1R1.vsh3
fmin : 0.80GHz
fmax : 5.95GHz
step : 50.00MHz
Nf : 104
```

We got information about the antenna filename and the frequency band where it has been defined.

At loading time the antenna is not evaluated. It means that there is not internally any instanciation of the pattern for a set of angular and frequency values.

To list all the available antenna files in the dedicated directory of the project it is possible to invoke the `ls()` method.

Antenna files should be stored in the sub-directory `ant` of the current project.
The current project is located with the `$BASENAME` environment variable.

```python
>>> !echo $BASENAME
/home/uguen/Bureau/P1
```

We can use the `ls` method to determine the number of files of different type

```python
>>> lvsh3 = A.ls('vsh3')
>>> lssh3 = A.ls('sh3')
>>> lmat = A.ls('mat')
>>> print "Number of antenna in .vsh3 format : ",len(lvsh3)
>>> print "Number of antenna in .sh3 format : ",len(lssh3)
>>> print lvsh3[0:5]
>>> print lssh3[0:5]
>>> print lmat[0:5]
Number of antenna in .vsh3 format :  66
Number of antenna in .sh3 format :  42
['S1R1.vsh3', 'S1R10.vsh3', 'S1R11.vsh3', 'S1R12.vsh3', 'S1R13.vsh3']
['S17R1.sh3', 'S17R2m.sh3', 'S1R1.sh3', 'S1R10.sh3', 'S1R11.sh3']
[]
```

As already mentionned above, at that point the radiation pattern of the antenna has not yet been evaluated. The method to evaluate the pattern is `Fsynth()` with the `pattern` option set to true. If the `pattern` option is set to False, the antenna is evaluated for only the specified direction. This mode is used in the ray tracing, while the former is used to visualize the whole antenna pattern.

The vector spherical coefficient are strored in `A.C`. This C refers to the coefficients.
Those coefficients are obtained thanks to the [Spherepack Module](http://nldr.library.ucar.edu/repository/assets/technotes/TECH-NOTE-000-000-000-380.pdf).

Adams, J.C., and P.N. Swarztrauber, 1997: Spherepack 2.0: A Model Development Facility. NCAR Technical Note NCAR/TN-436+STR, DOI: 10.5065/D6Z899CF.

We are here using the same notations.
See Formula 4-10- to 4-13 of the above reference document.
Only the vector spherical analysis is done using the `vha` function `Spherepack`, the vector spherical synthesis has been numpyfied in the
[pylayers.antprop.spharm.py](http://pylayers.github.io/pylayers/modules/pylayers.antprop.spharm.html) module.

[Description of Vector Spherical Harmonics](./AntennaVSH.html)

```python
>>> A.C
Br
-------------
Nf   : 104
fmin (GHz) : 0.8
fmax (GHz) : 5.95
Ncoeff s3 : 72

Bi
-------------
Nf   : 104
fmin (GHz) : 0.8
fmax (GHz) : 5.95
Ncoeff s3 : 72

Cr
-------------
Nf   : 104
fmin (GHz) : 0.8
fmax (GHz) : 5.95
Ncoeff s3 : 72

Ci
-------------
Nf   : 104
fmin (GHz) : 0.8
fmax (GHz) : 5.95
Ncoeff s3 : 72
```

## Synthesis of the radiation pattern

The radiation pattern is synthetized with the following call

```python
>>> A.show3()
```

```python
>>> A.Fp/show
array([[[ 0.00104336 +4.33849405e-03j,  0.00101081 +4.47040553e-03j,
          0.00097704 +4.59693052e-03j, ...,  0.00113333 +3.91206140e-03j,
          0.00110466 +4.05915370e-03j,  0.00107466 +4.20135503e-03j],
        [ 0.00143598 -4.82984725e-03j,  0.00150283 -4.84124285e-03j,
          0.00156853 -4.84636471e-03j, ...,  0.00123023 -4.75811573e-03j,
          0.00129949 -4.78826095e-03j,  0.00136814 -4.81218120e-03j],
        [ 0.00148192 -2.89541877e-02j,  0.00177081 -2.94847603e-02j,
          0.00205994 -2.99776016e-02j, ...,  0.00062188 -2.71475586e-02j,
          0.00090693 -2.77843747e-02j,  0.00119378 -2.83869988e-02j],
        ..., 
        [-0.01462579 -1.37860340e-02j, -0.01448360 -1.43245469e-02j,
         -0.01433206 -1.48404038e-02j, ..., -0.01499243 -1.20430430e-02j,
         -0.01488056 -1.26443729e-02j, -0.01475824 -1.32256828e-02j],
        [-0.00557976 +1.02773256e-04j, -0.00559583 -1.37900460e-05j,
         -0.00560941 -1.29139159e-04j, ..., -0.00551712 +4.56249142e-04j,
         -0.00554034 +3.38149329e-04j, -0.00556125 +2.20204280e-04j],
        [ 0.00062951 +4.94953591e-03j,  0.00058658 +5.05045141e-03j,
          0.00054294 +5.14528152e-03j, ...,  0.00075356 +4.61152872e-03j,
          0.00071305 +4.72994227e-03j,  0.00067169 +4.84265660e-03j]],

       [[ 0.00367658 +3.61921843e-03j,  0.00376071 +3.72364339e-03j,
          0.00384031 +3.82358165e-03j, ...,  0.00339802 +3.28030772e-03j,
          0.00349512 +3.39741697e-03j,  0.00358801 +3.51043260e-03j],
        [-0.00317604 +2.53001611e-03j, -0.00319943 +2.67494719e-03j,
         -0.00322048 +2.81687061e-03j, ..., -0.00309132 +2.07978850e-03j,
         -0.00312204 +2.23217806e-03j, -0.00315026 +2.38233968e-03j],
        [-0.01993344 +2.69093441e-04j, -0.02039054 +5.07649361e-04j,
         -0.02082558 +7.45453593e-04j, ..., -0.01843755 -4.45374630e-04j,
         -0.01895615 -2.07979169e-04j, -0.01945505 +3.03617863e-05j],
        ..., 
        [-0.02264692 -7.75899504e-03j, -0.02294596 -8.01722183e-03j,
         -0.02322713 -8.26219231e-03j, ..., -0.02164473 -6.90352339e-03j,
         -0.02199604 -7.20225774e-03j, -0.02233020 -7.48738016e-03j],
        [-0.00663024 -2.25024546e-03j, -0.00669257 -2.33203245e-03j,
         -0.00675243 -2.40981537e-03j, ..., -0.00643042 -1.98008290e-03j,
         -0.00649895 -2.07434730e-03j, -0.00656563 -2.16437623e-03j],
        [ 0.00238922 -1.09675042e-03j,  0.00247795 -1.13317855e-03j,
          0.00256369 -1.16824129e-03j, ...,  0.00210621 -9.79720512e-04j,
          0.00220324 -1.01997515e-03j,  0.00229761 -1.05900079e-03j]],

       [[ 0.00490798 +1.14904938e-03j,  0.00494732 +1.17183721e-03j,
          0.00498070 +1.19321307e-03j, ...,  0.00475470 +1.07249692e-03j,
          0.00481161 +1.09934929e-03j,  0.00486273 +1.12487703e-03j],
        [ 0.00752169 -2.41904373e-03j,  0.00771634 -2.42045373e-03j,
          0.00790296 -2.41938472e-03j, ...,  0.00689488 -2.39979439e-03j,
          0.00711042 -2.40872217e-03j,  0.00731954 -2.41513699e-03j],
        [ 0.01299552 -9.88754082e-03j,  0.01347759 -9.90211660e-03j,
          0.01394481 -9.90600364e-03j, ...,  0.01147218 -9.77734850e-03j,
          0.01199158 -9.82537249e-03j,  0.01249978 -9.86203443e-03j],
        ..., 
        [-0.02713605 -2.74433388e-03j, -0.02699432 -2.82801483e-03j,
         -0.02683298 -2.89720056e-03j, ..., -0.02743134 -2.40841800e-03j,
         -0.02735578 -2.53428210e-03j, -0.02725695 -2.64634565e-03j],
        [-0.01052731 +2.06528624e-03j, -0.01055565 +2.07568178e-03j,
         -0.01057742 +2.08786057e-03j, ..., -0.01040097 +2.04521854e-03j,
         -0.01045016 +2.05001991e-03j, -0.01049221 +2.05671950e-03j],
        [-0.00104965 +1.90704171e-03j, -0.00111900 +1.93183046e-03j,
         -0.00118699 +1.95429151e-03j, ..., -0.00083436 +1.81902170e-03j,
         -0.00090725 +1.85060333e-03j, -0.00097904 +1.87995512e-03j]],

       ..., 
       [[ 0.00555728 +1.15224598e-03j,  0.00543442 +1.19189404e-03j,
          0.00530501 +1.23010597e-03j, ...,  0.00588513 +1.02517098e-03j,
          0.00578277 +1.06883419e-03j,  0.00567344 +1.11120955e-03j],
        [ 0.00611986 -1.20182228e-03j,  0.00601775 -1.20457368e-03j,
          0.00590981 -1.21033162e-03j, ...,  0.00638928 -1.21238805e-03j,
          0.00630581 -1.20565414e-03j,  0.00621595 -1.20215682e-03j],
        [ 0.00406943 -2.12645540e-04j,  0.00406413 -1.82836122e-04j,
          0.00405554 -1.61455225e-04j, ...,  0.00406406 -3.49926505e-04j,
          0.00406953 -2.96468228e-04j,  0.00407127 -2.50614609e-04j],
        ..., 
        [-0.02029901 -3.28112729e-03j, -0.02002517 -3.32482837e-03j,
         -0.01974203 -3.35900295e-03j, ..., -0.02106259 -3.09441532e-03j,
         -0.02081794 -3.16575607e-03j, -0.02056334 -3.22804983e-03j],
        [-0.00832454 -7.40877790e-04j, -0.00825809 -6.84533811e-04j,
         -0.00818874 -6.24294324e-04j, ..., -0.00850583 -8.85163386e-04j,
         -0.00844846 -8.41324366e-04j, -0.00838801 -7.93186213e-04j],
        [-0.00021007 -1.58890044e-03j, -0.00022531 -1.52977558e-03j,
         -0.00024028 -1.46880747e-03j, ..., -0.00016290 -1.75451465e-03j,
         -0.00017885 -1.70133771e-03j, -0.00019458 -1.64611079e-03j]],

       [[ 0.00913898 -9.99186344e-04j,  0.00900933 -8.98078513e-04j,
          0.00886883 -7.95888567e-04j, ...,  0.00946130 -1.29480628e-03j,
          0.00936510 -1.19766980e-03j,  0.00925762 -1.09909023e-03j],
        [ 0.01037026 +6.53824609e-04j,  0.01024892 +8.07321508e-04j,
          0.01011593 +9.58658611e-04j, ...,  0.01066162 +1.81946885e-04j,
          0.01057687 +3.40980888e-04j,  0.01047967 +4.98325468e-04j],
        [ 0.01386034 +8.73546308e-03j,  0.01382047 +9.15476499e-03j,
          0.01376610 +9.56105515e-03j, ...,  0.01388982 +7.40790811e-03j,
          0.01389533 +7.86118635e-03j,  0.01388540 +8.30398820e-03j],
        ..., 
        [-0.01778262 +8.33623860e-03j, -0.01750961 +8.17084142e-03j,
         -0.01722236 +8.00570824e-03j, ..., -0.01851518 +8.83221463e-03j,
         -0.01828548 +8.66710832e-03j, -0.01804127 +8.50172142e-03j],
        [-0.00765205 +2.98207886e-03j, -0.00759866 +2.91944708e-03j,
         -0.00753929 +2.85876495e-03j, ..., -0.00777625 +3.18186575e-03j,
         -0.00774084 +3.11327307e-03j, -0.00769944 +3.04668173e-03j],
        [-0.00157219 -2.13375426e-03j, -0.00160488 -2.18676099e-03j,
         -0.00163562 -2.23713283e-03j, ..., -0.00146295 -1.95957893e-03j,
         -0.00150119 -2.02009476e-03j, -0.00153762 -2.07817653e-03j]],

       [[ 0.00809072 -3.92687999e-03j,  0.00796989 -3.86501352e-03j,
          0.00783946 -3.79849002e-03j, ...,  0.00839418 -4.08382027e-03j,
          0.00830299 -4.03634931e-03j,  0.00820180 -3.98401486e-03j],
        [ 0.01036461 -8.65507122e-03j,  0.01014183 -8.61689202e-03j,
          0.00990812 -8.57699811e-03j, ...,  0.01096344 -8.75897764e-03j,
          0.01077580 -8.72614307e-03j,  0.01057607 -8.69149879e-03j],
        [ 0.01592778 -6.17142865e-03j,  0.01549927 -6.09515543e-03j,
          0.01505565 -6.02757230e-03j, ...,  0.01711518 -6.44807891e-03j,
          0.01673648 -6.34832514e-03j,  0.01634043 -6.25596306e-03j],
        ..., 
        [-0.02252727 +1.41506669e-02j, -0.02244327 +1.40039624e-02j,
         -0.02234650 +1.38511959e-02j, ..., -0.02270397 +1.45538015e-02j,
         -0.02265748 +1.44256419e-02j, -0.02259863 +1.42912461e-02j],
        [-0.01188675 +5.06505193e-03j, -0.01180393 +5.03737446e-03j,
         -0.01171414 +5.00926101e-03j, ..., -0.01209297 +5.14640115e-03j,
         -0.01203130 +5.11947134e-03j, -0.01196255 +5.09238628e-03j],
        [-0.00311243 -2.07602039e-03j, -0.00303710 -2.09179800e-03j,
         -0.00295811 -2.10505515e-03j, ..., -0.00331557 -2.01377000e-03j,
         -0.00325175 -2.03698287e-03j, -0.00318401 -2.05774134e-03j]]])
```

```python
>>> A.Fsynth(pattern=True)
```

The `polar()` method allow to superpose different pattern for a list of frequencies `fGHz`
+ If `phd` (phi in degree) is specified the diagram is given as a function of $\theta$
+ If `thd` (theta in degree) is specified the diagram is given as a function of $\phi$

```python
>>> f = plt.figure(figsize=(15,15))
>>> a1 = f.add_subplot(121,polar=True)
>>> f1,a1 = A.polar(fGHz=[3,4,5],phd=0,GmaxdB=0,fig=f,ax=a1)
>>> a2 = f.add_subplot(122,polar=True)
>>> f2,a2 = A.polar(fGHz=[3,4,5],thd=90,GmaxdB=5,fig=f,ax=a2)
```

The vector spherical coefficients can be dispalayed as follows

```python
>>> fig = plt.figure(figsize=(8,8))
>>> A.C.show(typ='s3')
>>> plt.tight_layout()
```

## Defining Antenna gain from analytic formulas

An antenna can also be defined from closed-form expressions. Available antennas are the following
+ Omni
+ Gauss
+ WirePlate

```python
>>> A = Antenna('Omni')
```

```python
>>> A.Fpatt(pattern=True)
```

```python
>>> A.polar()
```

```python
>>> A = Antenna('Gauss')
>>> A.Fsynth()
>>> A.polar()
```

```python

```
