# Multi-wall model

```python
import time
from pylayers.util.project import *
import pylayers.util.pyutil as pyu
from pylayers.util.utilnet import str2bool
from pylayers.gis.layout import Layout
from pylayers.antprop.loss import *
from pylayers.antprop.coverage import *
from pylayers.network.model import *
%matplotlib inline
```

The layout is loaded from an ini file. If the graphs are not available, they are built.

```python
L=Layout('TA-Office.ini')
```

## Defining a radio link

The 2 extremities of the radio link (transmitter and receiver) have coordinates described as 1x2 `numpy.array` .

+ A a radio node

+ B a radio node

```python
A=np.array((4,1)) # defining transmitter position
B=np.array((30,12)) # defining receiver position
```

## Ploting the scene

The scene is plotted with the `showG` method of the Layout

```python
# figure instanciation
f = plt.figure(figsize=(10,5))
ax = f.add_subplot(111)
r = np.array((A,B))
# plotting the Layout
f,ax = L.showG(fig=f,ax=ax,graph='s',nodes=False)
# plotting the Tx and Rx
ax.plot(A[0],A[1],'ob')
ax.plot(B[0],B[1],'or')
# plotting the LOS
ax.plot(r[:,0],r[:,1])
a = plt.axis('off')
```

### Finding the intersection between the "direct" path and the walls


The function `angleonlink` returns the list of intersected segments and the corresponding incidence angles (in radians) with respect to the segment normal.

```python
%pdef L.angleonlink
```

```python
data=L.angleonlink(A,B)
```

### Computing the Multi-wall model

The multi-wall model computation returns losses and LOS excess delay for orthogonal and parallel polarization

```python
fGHz = 2.4
# observation grid
r = np.array((B,B))
Lwo,Lwp,Edo,Edp = Losst(L,fGHz,r.T,A)
print 'Losses orthogonal polarization \t %g dB' %(Lwo[0][0])
print 'Losses parallel polarization \t %g  dB' % (Lwp[0][0])
print 'Excess delay orthogonal polarization  \t %g ns' %(Edo[0][0])
print 'Excess delay parallel polarization   \t %g ns' %(Edp[0][0])
```

# Coverage class

By extension, the multi-wall model can also be used to perform a full coverage of a Layout given a transmitter position.

```python
C = Coverage()
C.L  = L # set layout
C.tx = A # set the transmitter
```

```python
C.L
```

```python
C.creategrid()
```

The coverage is performed on a grid. Boundaries of the grid are specified in the [`coverage.ini`](https://github.com/pylayers/pylayers/blob/master/data/ini/coverage.ini) file

### Compute the coverage

```python
t1=time.time()
C.cover()
t2=time.time()
print 'Coverage performed in ', t2-t1, 's'
```

### Coverage Map

For Orthogonal polarization

```python
fig1=plt.figure(figsize=(10,10))
f,a = C.show(typ='pr',fig=fig1,nodes=False)
```

For parallel polarization

```python
C.cover(snr=False,sinr=False)
fig1=plt.figure(figsize=(10,10))
f,a = C.show(typ='pr',fig=fig1)
```
