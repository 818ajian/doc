#  Indoor Coverage with the PyLayers Multi Wall model


A Multi wall model accounts only for the attenuation along the direct path between Tx and Rx.


This approach do not provide information about delay spread or multi paths but it can nevertheless be useful in different contexts, as i.e optimization of an indoor radio network. The MultiWall approach provides a fast rough indication about the propagation losses.


A ray tracing approach is much more accurate, but  also is much more time consuming and depending on the purpose, it is relevant
to proceed with a simpler and faster site-specific approach as the Multiwall model.

**`PyLayers`** provides a multiwall module which heavily relies on the core class **`Slab`**. Notice that, the same core **`Slab`** module is used for Ray tracing and MultiWall model approaches.


Let's see, how it works.
First let's import the `coverage` module. And the `time` module for performance evaluation.

```python
from pylayers.antprop.coverage import *
from matplotlib.pyplot import *
%matplotlib inline
import time
```


Instantiate a coverage object.
By defaut the `TA-Office.ini` layout is loaded.

The coverage information is placed in the **coverage.ini** file in the project directory.

Below is an example such a configuration file.

```python
!cat $BASENAME/ini/coverage.ini
```

The ini file contains 5 sections.

+ [grid] section
    This section precises the size of the grid. By default the grid is placed over the whole region of the Layout.
    A selected region can also be defined whith the `boundary` list
+ [layout] section
    The name of the layout file (filename = )
+ [ap] section
    A dictionnary of access points precising the standard, the used channel, the emitted power and the position
    of the access point.

+ [show] section

```python
# Create a Coverage object from coverag.ini file
C = Coverage('coverage.ini')
```

`C` has a dictionnary `dap` (dictionnary of access points) which gathers information about each access points of the scene.

```python
C.dap[1]
```


The coverage object has a `__repr__` method which summarizes different parameters of the current coverage object

```python
C
```

```python
C.cover()
```

Let display the current Layout with hidding nodes.

```python
fig=figure(figsize=(10,5))
C.L.display['nodes']=False
C.L.display['ednodes']=False
f,a = C.show(fig=fig)
```

The shadowing map coverage results can be displayed by invoquing various functions.

```python
fig=figure(figsize=(10,5))
f,a=C.show(fig=fig,typ='pr')
```

```python
fig=figure(figsize=(10,5))
f,a=C.show(fig=fig,typ='pr',f=4)
```

```python
fig=figure(figsize=(10,5))
f,a=C.show(fig=fig,typ='pr',f=10)
```

```python
fig=figure(figsize=(10,5))
f,a=C.show(fig=fig,typ='best',f=1)
```

```python
fig=figure(figsize=(10,5))
f,a=C.show(fig=fig,typ='best',f=10)
```

```python
fig=figure(figsize=(10,5))
f=C.show(fig=fig,f=5,typ='sinr')
```

As you have noticed the calculation has been done for all the center frequencies of the selected standard.
This is done in prevision of further channel optimizations.

Let's consider an other layout

```python
C2 = Coverage('coverage2.ini')
C2.cover()
```

```python
fig=figure(figsize=(10,5))
f=C2.show(ftyp='pr')
```

```python
C.snro.shape
```

```python
fig=figure(figsize=(10,5))
C.show(fig=fig,f=5,typ='capacity',dB=False)
```

All simulated quantities are stored in linear scale.

```python
C2.Lwo[0,0,0]
```

```python
C2.freespace[0,0,0]
```
