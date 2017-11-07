```python
!date
```

## Example of a trajectory synthesis in the DLR WHERE2 environment

The document is describing the measurement performed in the DLR environment in the WHERE2 project  
[WHERE2 Deliverable D4.4 Test and Evaluation of the Integrated System under Laboratory Conditions](http://www.kn-s.dlr.de/where2/documents/Deliverables/Deliverable-D4.4.pdf)

```python
from pylayers.simul.simulem import *
from pylayers.antprop.rays import *
from pylayers.antprop.channel import *
from pylayers.antprop.signature import *
import pylayers.util.pyutil as pyu
from pylayers.gis.layout import *
from pylayers.util.project import *
import pylayers.signal.bsignal as bs
from datetime import datetime
import time
import pdb
import pickle
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

## Loading the Layout, and setting the link

```python
L  = Layout('DLR2.lay')
DL = DLink(L=L)
DL.showG()
```

```python
S.show3()
```

We have a list of static Anchor Nodes. Those values correspond to the actual anchor nodes coordinates
of the WHERE2 project DLR measurement campaign.

```python
AnchorNodes = {390:{'name':'MT_ACO_05','coord':[6,0.81,1.64]},
               386:{'name':'MT_ACO_08','coord':[30.574,2.8,1.291]},
                391:{'name':'MT_ACO_07','coord':[11.78,-5.553,1.5]},
                385:{'name': 'MT_ACO_01','coord':[19.52,-0.69,1.446]},
                387:{'name':'MT_ACO_03','coord':[28.606,-0.74,1.467]},
                400:{'name':'MT_ACO_02','coord':[30.574,2.8,1.291]},
                1:{'name':'MT_DLR_RTDSlave','coord':[0.85,0,1.18]}
               }
```

Vizualization of the simulated scenario

```python
fig,ax=S.L.showG('s',nodes=False)
plt.axis('off')
k = AnchorNodes.keys()[c]
pta = array([AnchorNodes[k]['coord'][0],AnchorNodes[k]['coord'][1],AnchorNodes[k]['coord'][2]]).reshape(3,1)
#
... # To add a point
... #
... S.tx.point(pta,mode="add")
da[c]=k
plt.plot(pta[0,:],pta[1,:],'or')
[<matplotlib.lines.Line2D at 0x7fb841bd3810>]
```

In the following a trajectory for the receiver is defined.

`linevect` function allows to define a linear trajectory from `ptt` along direction `vec`.

```python
S.rx.linevect(npt=290, step=0.1, ptt=[0, 0, 1.275], vec=[1, 0, 0], mode='subst')
ps = S.rx.position[:,-1]
S.rx.linevect(npt=60, step=0.1, ptt=ps,vec=[0,1,0],mode='append')
```

Looking what is does

```python
S.L.display['ednodes']=False
S.L.display['edges']=True
S.L.display['nodes']=False
S.L.display['title']='Trajectory to be simulated'
S.show(s=20)
Warning : no furniture file loaded
(<matplotlib.figure.Figure at 0x7fb841bd3390>,
 <matplotlib.axes._subplots.AxesSubplot at 0x7fb841abcd10>)
```

Choosing a UWB waveform for the simulation

```python
wav = wvf.Waveform(type='W1compensate')
wav.show()
```

running the simulation

```python
tcir = evalcir(S,wav,cutoff=4)
```

Saving the data in pickle format

```python
#file = open("tcir5.pickle","w")
... #pickle.dump(tcir,file)
... #file.close()
```

Reading the data from the above file

```python
#del tcir
... file=open("tcir5.pickle","r")
tcir=pickle.load(file)
file.close()
#del ttcir
... #
... for i in tcir[1].keys():
...     cir = tcir[1][i]
...     cir.zlr(0,150)
...     try:
...         ttcir=np.vstack((ttcir,cir.y))
...     except:
...         ttcir=cir.y
```

```python
tcir[1][1].x
tcir[1][102].x
array([  1.01214575e-02,   3.03643725e-02,   5.06072874e-02, ...,
         1.49949393e+02,   1.49969636e+02,   1.49989879e+02])
```

#### Aggregated CIR along a synthetic trajectory (line in the corridor)

```python
plt.figure(figsize=(20,20))
dmax=150
plt.imshow(20*np.log10(ttcir+1e-20),vmax=-40,vmin=-120,origin='lower',extent=[0,dmax,1,69],interpolation='nearest')
plt.xlabel(r'delay $\times$ c (meters)',fontsize=20)
#plt.ylabel(r'distance along trajectory (meters)',fontsize=20)
... plt.ylabel(r'trajectory index number',fontsize=20)
clb=plt.colorbar()
clb.set_label('level (dB)',fontsize=20)
...
plt.axis('tight')
(0.0, 150.0, 1.0, 69.0)
```

```python
tcir[1][10].plot(typ=['v'])
(<matplotlib.figure.Figure at 0x7fb846e06f50>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fb8417fc6d0>]], dtype=object))
```

```python
plt.figure(figsize=(10,5))
tcir[1][1].plot(typ=['v'])
xlabel('Delay (ns)')
ylabel('Level (V)')
title('Received Waveform')
```

```python
tcir[1][11].plot(typ=['v'])
xlabel('Delay (ns)')
ylabel('Level (V)')
title('Received Waveform')
```
