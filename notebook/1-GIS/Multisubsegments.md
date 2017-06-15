```python
!date
```

# Effect of Modifying the Nature of Sub-Segments

This illustrates a simple ray tracing simulation. The environement 
is a building with 2 rooms. At the interface betweebn the two rooms there is 
a segment with 3 sub-segment whose material properties are changed in the simulation. The notebook illustrates in details the different steps of the simulation. First we need to import several specialized modules. 

```python
from pylayers.simul.link import *
from pylayers.antprop.rays import *
from pylayers.antprop.aarray import *
from pylayers.antprop.channel import *
from pylayers.gis.layout import *
from pylayers.antprop.signature import *
import pylayers.signal.bsignal as bs
import pylayers.signal.waveform as wvf
from pylayers.simul.simulem import *
import matplotlib.pyplot as plt
%matplotlib inline
```

Let's start by loading a simple layout with 2 single rooms. The multi subsegment
appears in the middle with the red vertical lines. Each subsegment is
materialized by a  segment.

```python
L=Layout('defstr.ini')
f,a=L.showG('s',subseg=True,figsize=(10,10))
```

The studied configuration is composed of a simple 2 rooms building separated by
a subsegment which has a multi subsegment attribute. The attribute of the
subsegment can be changed  with the method [`chgmss`](http://pylayers.github.io/
pylayers/modules/generated/pylayers.gis.layout.Layout.chgmss.html) (change
multisubsegment). In the example WOOD in the lower part then 10cm of AIR then
wood again until the ceiling.

```python
L.chgmss(1,ss_name=['WOOD','AIR','WOOD'],ss_z =[(0.0,2.7),(2.7,2.8),(2.8,3)],ss_offset=[0,0,0])
```


The $\mathcal{G}_s$ graph dictionary has the following structure

```python
L.Gs.node
```

We define now, the position of the transmitter and the receiver, the two points which are always the termination of a radio link.

```python
#tx=np.array([759,1114,1.5])
#rx=np.array([767,1114,1.5])
tx=np.array([759,1114,1.5])
rx=np.array([767,1114,1.5])
```


```python
fGHz=np.linspace(1,11,100)
#Aa = Antenna('S1R1.vsh3')
#Ab = Antenna('S1R1.vsh3')
Aa = Antenna('Gauss',fGHz=fGHz)
Ab = Antenna('Gauss',fGHz=fGHz)
Ab.eval()
Aa.eval()
#Aa = AntArray(N=[8,1,1],fGHz=fGHz)
#Ab = AntArray(N=[4,1,1],fGHz=fGHz)
Lk = DLink(L=L,a=tx,b=rx,Aa=Aa,Ab=Ab,fGHz=fGHz,cutoff=5)
ak,tauk=Lk.eval(force=True,verbose=False)
```

```python
ak.shape
```

```python
plt.stem(tauk,ak[:,0,0])
```

A link is the set of a layout and 2 termination points.

```python
Aa.eval()
Aa.plotG()
```

```python
Lk.C.Ctt
```

```python
ak,tauk=Lk.eval(force=True,a=tx,b=rx,applywav=True)
```

```python
Lk.C
```

```python
f = plt.figure(figsize=(10,10))
f,a=Lk.C.show(cmap='jet',fig=f,typ='l20',vmin=-120,vmax=-10)
```

```python
fGHz=np.arange(2,6,0.1)
wav = wvf.Waveform(fcGHz=4,bandGHz=1.5)
wav.show()
```

```python
Lk = DLink(L=L,a=tx,b=rx,fGHz=fGHz)
```

Position of the transmitter 

```python
Lk.a
```

Position of the receiver

```python
Lk.b
```

```python
cir = Lk.H.applywavB(wav.sf)
```

```python
layer = ['AIR','AIR','AIR']
Lk.L.chgmss(1,ss_name=layer)
Lk.L.Gs.node[1]['ss_name']=layer
#Aa = Antenna('Omni',fGHz=fGHz)
#Aa = Antenna('Omni',fGHz=fGHz)
ak,tauk=Lk.eval(force=True,verbose=0,fGHz=fGHz)
plt.stem(Lk.H.taud,Lk.H.ak[:,0,20])
plt.title(str(layer))
plt.figure()
layer = ['METAL','METAL','METAL']
Lk.L.chgmss(1,ss_name=layer)
Lk.L.Gs.node[1]['ss_name']=layer
ak,tauk=Lk.eval(force=True,verbose=0,fGHz=fGHz)
plt.stem(Lk.H.taud,Lk.H.ak[:,0,20])
plt.title(str(layer))
#plt.stem(Lk.H.taud,Lk.H.ak[:,0,50])
plt.figure()
layer = ['WOOD','AIR','WOOD']
Lk.L.chgmss(1,ss_name=layer)
Lk.L.Gs.node[1]['ss_name']=layer
ak,tauk=Lk.eval(force=True,verbose=0,fGHz=fGHz)
plt.title(str(layer))
plt.stem(Lk.H.taud,Lk.H.ak[:,0,20])
```


We have modified successively the nature of the 3 surfaces in the sub segment
placed in the separation partition. The first was AIR, the second WOOD and the
third METAL. As the subsegment is placed on the LOS path the blockage effect is
clearly visible.
The chosen antennas were omni directional `Antenna('Omni')`
