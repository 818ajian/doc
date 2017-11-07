```
!date 
```

# Ray Signatures

Signatures are calculated from a cycle to an other cycle of the Layout. They are used for the determination of rays once the transmitter and receiver are known.

The evaluation of a signature from one cycle to another is implemented in the `pylayers.simul.antprop.signature.Signature` class.

```python
import time
from pylayers.gis.layout import *
from pylayers.antprop.signature import *
from pylayers.antprop.rays import *
%matplotlib inline
```


Let load a simple Layout 

```python
L = Layout('defstr.lay')
L.build()
```

Showing the graph of visibilty

```python
L.showG('sv',figsize=(8,8))
plt.axis('off')
```

The graph of interactions is shown below : 

```python
L._showGi()
```

The node of Gi are interactions. A transmission is noted Python_

.. \_Python: http://www.python.org/


```python
L.Gi.node
```

All the interactions of a given cycle are stored as meta information in nodes of `Gt`

```python
L.Gt.node[1]['inter']
```

The signature is calculated with as parameters the  Layout object and two cycle numbers.
In example below it is 0 and 1.

```python
Si = Signatures(L,1,2)
```

The cold start determination of the signature is done with a `run` function. The code is not in its final shape here and there is room for significant acceleration in incorporating propagation based heuristics. The mitigation of graph exploration depth is done in setting a `cutoff` value which limits the exploration in the interaction graph.

```python

Si.run(cutoff=5,diffraction=False)
```

The representation method of a signature gives informations about the different signatures. Signatures are grouped by number of interactions.

```python

L.Gt.pos
```

```python

ptx = np.array(L.Gt.pos[1])+np.random.rand(2)
prx = np.array(L.Gt.pos[2])+np.random.rand(2)
print ptx
print prx
```
