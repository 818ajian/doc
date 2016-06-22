```python
>>> from pylayers.location.algebraic.algebraic import *
>>> from pylayers.util.geomutil import dist
```

## Example of TDOA

First, it is necessary to define Anchor nodes and associated Reference Anchor Nodes. This is important to be very specific about what exactly the TDOA is. In the example the Blin node is draw randomly as well as anchor nodes.

```python
>>> nodes = {}
>>> N = 5
>>> AN_TDOA = np.random.rand(2,N)
>>> #AN_TDOA1=np.array([[0, 0, 1, 1],[0,1,1,0]])
... #AN_TDOAr1 = np.roll(AN_TDOA,1,axis=1)
... AN_TDOAr1 = np.zeros((2,1))
>>> AN_TDOAr2 = AN_TDOA[:,-1][:,newaxis]
>>> BN = np.array([[0.2],[0.3]])
```

```python
>>> AN_TDOA
```

```python
>>> AN_TDOAr1
```

```python
>>> AN_TDOAr2
```

The figure below illustrates the situation, in red the anchor nodes, the blue star is the blind node.

```python
>>> plot(AN_TDOA[0,:],AN_TDOA[1,:],'or')
>>> plot(AN_TDOAr2[0,:],AN_TDOAr2[1,:],'ok')
>>> plot(BN[0,:],BN[1,:],'*b')
>>> axis([-1,2,-1,2])
```

```python
>>> d = dist(AN_TDOA,BN,0)
>>> dr1= dist(AN_TDOAr1,BN,0)
>>> dr2= dist(AN_TDOAr2,BN,0)
```

```python
>>> tdoa1 = (d-dr1)/0.3
>>> tdoa2 = (d-dr2)/0.3
>>> tdoa0 = (d-roll(d,1))/0.3
>>> 
>>> print cumsum(tdoa0)
>>> print tdoa1
>>> print tdoa2
```

```python
>>> node={}
>>> nodes['BN']=BN
>>> nodes['RN_TDOA']=AN_TDOA
>>> nodes['RNr_TDOA']=AN_TDOAr2
>>> ldp = {}
>>> ldp['TDOA']=cumsum(tdoa0)
>>> ldp['TDOA_std']=np.ones(N)
```

```python
>>> S=algloc(nodes,ldp)
```

```python
>>> S.info()
```

```python
>>> S = algloc(nodes,ldp)
```

```python
>>> S.ls_locate(tdoa=True,toa=False,rss=False)
```

```python
>>> nodes['BN']
```
