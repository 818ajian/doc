```python
>>> !date 
```

# Description of the propagation environment

The `Layout` class contains the data structure for describing a propagation environment. It contains different graphs helping the implementation of the ray tracing. The class is implemented in the 

[layout.py](http://pylayers.github.io/pylayers/modules/pylayers.gis.layout.html)

```python
>>> from pylayers.gis.layout import *
>>> from IPython.display import Image
>>> import os
>>> %matplotlib inline
```

## Getting the list of all available Layouts : the `ls()` method

Creating an empty Layout is as simple as :

```python
>>> L=Layout()
>>> L
```

The different argument of the __init__ function are listed below  

```python
>>> L=Layout(string='',
                 _filematini='matDB.ini',
                 _fileslabini='slabDB.ini',
                 _filefur='',
                 bcheck=True,
                 bbuild=True,
                 bverbose=False,
                 bcartesian=True,
                 dist_m=400,
                 typ='indoor')
```

+ **string** is either an existing layout filename (.ini,.osm,.res) or the coordinates (lat,lon)
+ ** _filematini** is the a material filename
	material ans slab are now described in .lay file
+ ** _fileslabini** is the a slab filename
+ ** _filefur** is the furniture filename
+ ** bcheck** is a boolean which force layout integrity checking 
+ ** bbuild** is a boolean which force rebuilding the layouts graphs 
+ ** bverbose** is a boolean output verbosity
+ ** bcartesian** is a boolean controling the type of coordinates cartesian or (lat,lon)
+ **dist_m** is a float value which indicates the zone radius in meters for openstreet map extraction 
+ **typ** is a string which takes values either 'floorplan' or 'outdoor'

Querying the file name associated with the Layout.

```python
>>> L._filename
```

 The Layout is described in an `.lay` file, a `.osm`file or a `.res` file.

The `ls()` method lists the layout files which are available in the `struc` directory of your current project, which is set up via the $BASENAME environment variable which should be defined in order PyLayers find the good directories.

```python
>>> L.ls('lay')
```

```python
>>> L=Layout('defstr.lay')
```

```python
>>> L
```

```python
>>> f,a=L.showG('s',
             nodes=True,
 	     slab=True,
	     subseg=True,
	     figsize=(10,10),labels=True)
```

L.ax  provides the boundary of the layout with the following tuple format : 
 (xmin,xmax,ymin,ymax)

```python
>>> L.ax
```

```python
>>> L.build()
```

A Layout is decomposed into convex cycles which are stored in the Gt graph. 
The diffraction points are stored in the dictionnary `L.ddiff`. The keys of this dictionnary are the diffraction points number and the values are a zipped list of output cycles and corresponding wedge angles.

```python
>>> L.Gv.node
```

```python
>>> L.ddiff
```

```python
>>> L.Gt.node
```

```python
>>> L=Layout('DLR.lay')
```

```python
>>> f,a=L.showG('s',aw=False)
```

To check which are the used slabs :

```python
>>> L.sl
```

Let's load an other layout. This an indoor office where the FP7 WHERE project UWB impulse radio measuremnts have been performed. 

```python
>>> L=Layout('WHERE1.lay')
```

The showG method provides many possible visualization of the layout

```python
>>> f,a=L.showG('s',airwalls=False,figsize=(20,10))
```

```python
>>> L=Layout('W2PTIN.lay')
```

```python
>>> f,a = L.showG('s')
```

## The useful numpy arrays of the Layout

The layout data structure is a mix between graph and numpy array. 
numpy arrays are used when high performance is required while graph 
structure is convenient when dealing with different specific tasks. 
The tricky thing for the mind is to have to transcode between node index 
excluding 0 and numpy array index including 0. Below are listed various 
useful numpy array which are mostly used internally.

+ tsg : get segment index in Gs from tahe
+ isss :  sub-segment index above Nsmax
+ tgs : get segment index in tahe from Gs
+ lsss : list of segments with sub-segment
+ sla : list of all slab names (Nsmax+Nss+1)
+ degree : degree of nodes

### `pt` the array of points

The point coordinates are stored in two different places

  + L.Gs.pos : in a dictionary form (key is the point negative index)
  + L.pt : in a numpy array

```python
>>> print np.shape(L.pt)
>>> print len(filter(lambda x: x<0,L.Gs.pos))
```

This dual storage is chosen for computational efficiency reason. The priority goes to the graph and the numpy array is calculated at the end of the edition in the `Layout.g2npy` method (graph to numpy) which is in charge of the conversion.

### tahe (tail-head)

`tahe` is a $(2\times N_{s})$  where $N_s$ denotes the number of segment. The first line  is the tail index of the segment $k$ and the second line is the head of the segment $k$. Where $k$ is the index of a given segment (starting in 0).

```python
>>> L.build()
```

The figure below illustrates a Layout and a superimposition of the graph of cycles $\mathcal{G}_c$. Those cycles are automatically extracted from a well defined layout. This concept of **cycles** is central in the ray determination algorithm which is implemented in PyLayers. Notice that the exterior region is the cycle indexed by 0. All the rooms which have a common frontier with the exterior cycle are here connected to the origin (corresponding to exterior cycle).

```python
>>> f,a = L.showG('s')
```

```python
>>> nx.draw_networkx_nodes(L.Gi,L.Gi.pos,node_color='blue',node_size=1)
>>> nx.draw_networkx_edges(L.Gi,L.Gi.pos,node_color='blue',node_size=1)
```

## `tgs` : trancodage from graph indexing to numpy array indexing

`tgs` is an array with length $N_s$+1. The index 0 is not used because none segment has 0 as an index.

```python
>>> ns = 5
>>> utahe = L.tgs[ns]
```

```python
>>> tahe =  L.tahe[:,utahe]
```

```python
>>> ptail = L.pt[:,tahe[0]]
>>> phead = L.pt[:,tahe[1]]
```

```python
>>> print ptail
```

```python
>>> print phead
```

```python
>>> L.Gs.node[5]
```

```python
>>> print L.Gs.pos[-8]
```

```python
>>> aseg = np.array([4,7,134])
```

```python
>>> print np.shape(aseg)
```

```python
>>> pt  = L.tahe[:,L.tgs[aseg]][0,:]
>>> ph = L.tahe[:,L.tgs[aseg]][1,:]
>>> pth = np.vstack((pt,ph))
```


