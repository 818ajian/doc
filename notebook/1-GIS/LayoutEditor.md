## The Layout class

### Introduction

This section explains the main features of the  **Layout** class.

A Layout is a representation of a floorplan, it is handled by the module **pylayers.gis.layout**.

This module recognizes different file formats including geo-referenced files in open street map format `.osm`.

Using osm allows to take advantage
of a mature floor plan editor *JOSM* with the plugin *PicLayer*. This is well described in http://wiki.openstreetmap.org/wiki/IndoorOSM

The `pylayers.gis.osmparser` module parses `osm` files.

See the following methods of the layout object

+ `loadosm()`
+ `saveosm()`

### Structure of a Layout

At first a Layout is described by a set of points (negative index) and a set of segments (positive index).

Points and segments are nodes of the $\mathcal{G}_s$ graph.

It is required to respect a strict non overlapping rule. **No segments can recover partially or totally an other segment**.

This rule allows to capture topological relations of the network which are exploited for further analysis.

### Subsegments

To describe doors and windows, the concept of `subsegment` is introduced.

A `segment` has attributes :

+ `name` : slab name
+ `z` : tuple of minimum and maximum heights with respect to ground (meters)
+ `transition` : a boolean indicating if a human can cross this segment. For example, segments associated with a door are transition segments but we will see later that it may be judicious to split space with transparent segments which have the name 'AIR'. Those segments are also `transition=True`

A `subsegment` belongs to a `segment`, it has mainly 2 attached parameters :

+ `ss_name` : subsegment slab name
+ `ss_z` : [(zmin1,zmax1),(zmin2,zmax2),...,(zminK,zmaxK))] list of minimum and maximum height of associated subsegments (meters)



When appearing in a 3D ray a subsegment should have a unique index different from the segment index.

### The different layout format

The layout format has regularly evolved over time and is going to evolve again.
Currently, the different recognized file extensions are the following :

+ `.str2`: a ASCII file (Node list + edge list)
+ `.str`  : a binary file which includes visibility relations between point and segments
+ `.ini`  : an ini file which gather node list and edge list as well as the state of the current `display` dictionnary
+ `.osm`  : an xml file which can be edited with [JOSM](http://josm.openstreetmap.de/)

```python
>>> from pylayers.gis.layout import *
>>> from pylayers.util.project import *
>>> %matplotlib inline
```

### Reading an exiting Layout

To read an existing layout it is sufficient to create a Layout object with, as an argument, a file name with
one of the recognized extension. All files are stored in the `pstruc['DIRSTRUC']` directory of the project. The project root directory
is defined in the `$BASENAME` environment variable.

```python
>>> print pstruc['DIRSTRUC']
struc/str
```

`pstruc` is a dictionnary which gathers all directories which are used in `PyLayers`

```python
>>> pstruc
```

The structure of the `.osm` file is shown below

```python
>>> %%bash
    cd $BASENAME/struc
    ls *.osm

```

```python
>>> %%bash
     cd $BASENAME/struc
     head DLR.osm
     echo '---'
     tail -17 DLR.osm
```

To read a new layout in osm format :

```python
>>> L=Layout('DLR.ini')
```

```python
>>> fig,ax=L.showGs()
```

```python
>>> L.info()
```

The different graphs associated with the layout are then built

```python
>>> L.build()
```

The topological graph $\mathcal{G}_t$ or graph of non overlapping cycles.

```python
>>> f,a=L.showG('t')
>>> b=plt.axis('off')
```

The graph of room $\mathcal{G}_r$. Two rooms which share at least a wall are connected.
Two rooms which share only a corner (punctual connection) are not connected

```python
>>> f,a=L.showG('r')
>>> b=plt.axis('off')
```

The graph of waypath $\mathcal{G}_w$. This graph is used for agent mobility. This allows to determine the shortest path between 2 rooms. This information could be included in the osm file. This is not the case yet

```python
>>> f,a=L.showG('w')
>>> b=plt.axis('off')
```

The graph of visibility $\mathcal{G_v}$

```python
>>> f,a=L.showG('v')
>>> b=plt.axis('off')
```

The graph of interactions $\mathcal{G}_i$ used to determine the ray signatures.

```python
>>> f=plt.figure(figsize=(15,15))
>>> a = f.gca()
>>> f,a=L.showG('i',fig=f,ax=a)
>>> b= plt.axis('off')
```

### The display options dictionnary

```python
>>> L.info()
```

The layout can be displayed using matplotlib plotting primitive. Several display options are specified in the display dictionary. Those options are exploited in `showGs()` visualization method.

```python
>>> L.display
```

#### Layers

 + 'layer' : list , []
 + 'layerset',list, list of available layers
 + 'layers', list , []
 + 'activelayer', str , 'WINDOW_GLASS'
 + 'alpha', float , 0.5 , overlay transparency
 + 'box', tuple , (-20,20,-10,10), (xmin xmax,ymin,ymax)

#### Strings

 + 'title' : str , 'Init'
 + 'fileoverlay' : str , 'TA-Office.png'

#### Sizes

 + 'fontsize', float , 10
 + 'ndsize', float , 10
 + 'ndlblsize' : float  20
 + 'edlblsize' : float , 20

#### Booleans

 + 'edlabel', boolean, False
 + 'ticksoff',boolean, True
 + 'scaled' :  boolean , True
 + 'subseg' : boolean , True
 + 'nodes', boolean , True
 + 'visu', boolean , False
 + 'edges', boolean , True
 + 'clear', boolean, False
 + 'overlay', boolean , False
 + 'thin', boolean , False , If True trace all segments with thickness 1
 + 'ndlabel',boolean, If True display node labels
 + 'ednodes', boolean, True

### Interactive Editor

The command L.editor() launches an interactive editor. The state machine is implemented in module `pylayers.gis.selectl.py`.

To have an idea of all available options, look in the 

[`pylayers.gis.SelectL`](http://pylayers.github.io/pylayers/_modules/pylayers/gis/selectl.html#SelectL.new_state) module

PyLayers comes along with a low level structure editor based on `matplotlib` which can be invoked using the `editor()` method.
This editor is more suited for modifying constitutive properties of walls. In the future a dedicated plugin in `JOSM`
could be a much better solution.


There are two different modes of edition

+ A create points mode CP

    + left clic   : free point
    + right clic  : same x point
    + center clic : same y point

+ A create segments mode
    + left clic   : select point 1
    + left clic   : select point 2
    + left clic   : create a segment between point 1 and point 2

**m**  : to switch from one mode to an other

**i** : to return to init state

#### Image overlay

It is useful while editing a layout to have an overlay of an image in order to help placing points. The image overlay can either be an url
or a filename. In that case the file is stored in

```python
>>> L=Layout()
>>> L.display['fileoverlay']='http://images.wikia.com/theoffice/images/9/9e/Layout.jpg'
```

```python
>>> L.display['overlay']=True
>>> L.display['alpha']=1
>>> L.display['scaled']=False
>>> L.display['ticksoff']=False
>>> L.display['inverse']=True
```

```python
>>> plt.figure(figsize=(10,10))
>>> L.showGs()
```

#### Scaling the figure overlay

Before going further it is necessary :

+ to place the global origin
+ to precise the vertical and horizontal scale of the image

This is done by the following commands :

+ 'i' : back to init state
+ 'm' : goes to CP state
+ 'o' : define the origin
+  'left click' on the point of the figure chasen as the origin
+  'left click' on a point at a known distance from the origin along x axis. Fill the dialog box with the actual distance (expressed in meters) between the two points.
+  'left click' on a point at a known distance from the origin along y axis. Fill the dialog box with the actual distance (expressed in meters) between the two points.

In that sequence of operation it is useful to rescale the figure with 'r'.

At that stage, it is possible to start creating points

        'b'  : selct a segment
        'l'  : select activelayer
        'i'  : back to init state
        'e'  : edit segment
        't'  : translate  structure
        'h'  : add subsegment
        'd'  : delete subsegment
        'r'  : refresh
        'o'  : toggle overlay
        'm'  : toggle mode (point or segment)
        'z'  : change display parameters
        'q'  : quit interactive mode
        'x'  : save .str2 file
        'w'  : display all layers

#### Vizualisation of the layout

```python
>>> L = Layout('TA-Office.ini')
>>> L.dumpr()
>>> fig = plt.figure(figsize=(25,25))
>>> ax = fig.gca()
>>> fig,ax = L.showG(fig=fig,ax=ax,graph='s',labels=True,font_size=9,node_size=220,node_color='c')
>>> a = plt.axis('off')
```

Each node of $\mathcal{G}_s$ with a negative index is a point.

Each node of $\mathcal{G}_s$ with a positive index corresponds to a segment (wall,door,window,...).

The segment name is the key of the **slab** dictionnary.

[Multi Subsegments](./Multisubsegments.html)
