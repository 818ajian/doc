```python
!date
```

# Modifying the segment nature 

This illustrates a simple ray tracing simulation. The environement 
is a building with 2 rooms. At the interface between the two rooms there is 
a segment with 3 sub-segment whose material properties are changed in the simulation. 
This section illustrates in details the different steps of the simulation. 
First we need to import several specialized modules. 

```python
from pylayers.simul.link import *
from pylayers.antprop.rays import *
from pylayers.antprop.aarray import *
from pylayers.antprop.channel import *
from pylayers.gis.layout import *
from pylayers.antprop.signature import *
import pylayers.signal.bsignal as bs
import pylayers.signal.waveform as wvf
import matplotlib.pyplot as plt
%matplotlib inline 
```

Let's start by loading a simple layout with 2 single rooms. The multi subsegment
appears in the middle with the red vertical lines. Each subsegment is
materialized by a  segment.

```python
L=Layout('defstr.lay')
f,a=L.showG('s',subseg=True,figsize=(10,10))
```

The attribute `lsss` lists all the segments which are superposed called `iso` segment. 
```
L.lsss
```

The studied configuration is composed of a simple 2 rooms
building separated by an iso segment.

```python 
print L.Gs.node[1]
print L.Gs.node[2]
print L.Gs.node[3]
```

The $\mathcal{G}_s$ graph dictionary has the following node. Negative nodes are points 
and positive index nodes are segments. 

```python
for k in [-1,1,2]:
    print(L.Gs.node[k])
```

We define now, the position of the transmitter and the receiver, the two termination of a radio link.

```python
#tx=np.array([759,1114,1.5])
#rx=np.array([767,1114,1.5])
tx=np.array([2,3,1.5])
rx=np.array([8,4,1.6])
```


```python
fGHz=np.linspace(1,11,100)
#Aa = Antenna('S1R1.vsh3')
#Ab = Antenna('S1R1.vsh3')
Aa = Antenna('Gauss',fGHz=fGHz)
Ab = Antenna('Gauss',fGHz=fGHz)
#Aa = AntArray(N=[8,1,1],fGHz=fGHz)
#Ab = AntArray(N=[4,1,1],fGHz=fGHz)
Lk = DLink(L=L,
	   a=tx,
           b=rx,
           Aa=Aa,
           Ab=Ab,
           fGHz=fGHz,
	   cutoff=5)
Lk.eval(force=True,verbose=False)
```


```python
Aa.eval()
Aa.plotG()
```

```python
Lk.C.Ctt
```

```python
Lk.eval(force=True,a=tx,b=rx,applywav=True)
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

L.Gs.node[1]['name']='AIR'
L.Gs.node[2]['name']='AIR'
L.Gs.node[3]['name']='AIR'
#Aa = Antenna('Omni',fGHz=fGHz)
#Ab = Antenna('Omni',fGHz=fGHz)
Lk.eval(force=True,verbose=0,fGHz=fGHz)
Lk.plt_cir()
plt.title('AIR/AIR/AIR')
plt.figure()
L.Gs.node[1]['name']='METAL'
L.Gs.node[2]['name']='METAL'
L.Gs.node[3]['name']='METAL'
Lk.eval(force=True,verbose=0,fGHz=fGHz)
Lk.plt_cir()
plt.title('METAL/METAL/METAL')
plt.figure()
L.Gs.node[1]['name']='WOOD'
L.Gs.node[2]['name']='AIR'
L.Gs.node[3]['name']='WOOD'
Lk.eval(force=True,verbose=0,fGHz=fGHz)
Lk.plt_cir()
plt.title('WOOD/AIR/WOOD')
```


We have modified successively the nature of the 3 surfaces in the sub segment
placed in the separation partition. The first was AIR, the second WOOD and the
third METAL. As the subsegment is placed on the LOS path the blockage effect is
clearly visible.
The chosen antennas were omni directional `Antenna('Omni')`
