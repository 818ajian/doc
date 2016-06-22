# Algebraic Localization Class

For localization in the plane, it is important not to specify the z coordinates. Otherwise a singularity problem arises.

```python
>>> import numpy as np
>>> from pylayers.location.algebraic.algebraic  import *
>>> %matplotlib inline
```

```python
>>> nodes={}
>>> ldp={}
>>> p1 = np.array([-1,-1])
>>> p2 = np.array([1,-1])
>>> p3 = np.array([0,1])
>>> nodes['BN'] = np.array([[0],[0]])
>>> nodes['RN_TOA']=np.vstack((p1,p2,p3)).T
>>> ldp['TOA']=np.array([np.sqrt(2),np.sqrt(2),1])
>>> ldp['TOA_std']=np.array([1,1,1])
>>> Alg = algloc(nodes,ldp)
```

```python
>>> print ldp
>>> f,a = Alg.plot()
```

```python
>>> pest = Alg.ls_locate(toa=True,tdoa=False,rss=False)
```

```python
>>> pest
```

```python
>>> Alg
```
