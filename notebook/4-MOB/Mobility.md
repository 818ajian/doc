```python
!date
```

# Trajectory and Network simulation

```python
from IPython.display import Image, HTML, Latex, YouTubeVideo
import numpy as np
import pylayers.mobility.trajectory as traj
from pylayers.mobility.ban.body import *
from pylayers.gis.layout import *
%matplotlib inline
```

```python
YouTubeVideo('1Qa6xLpU5-M')
```

Trajectories can be generated using simulnet.

```python
from pylayers.simul.simulnet import *
S=Simul()
```

```python
# set simulation duration
S.sim_opt['duration']='100'
S.meca_opt['mecanic_update_time']=0.1
# turn on network simulation
S.net_opt['network']=True
```

```python
# run mechanical simulation
S.runsimul()
```

## Trajectory
trajectories can be imported from a simulnet simulation with the `importh5` method

```python
from pylayers.mobility.trajectory import *
```


```python
str1 = eval(S.sim_opt['filename'])
str2 = S.L._filename.split('.')[0]
save_filename = str1 + '_' + str2 +'.h5'
 
list_traj = S.traj
```

```python
list_traj
```

The 2 following trajectories have been calculated with `pylayers.simul.simulnet`

```python
 t=S.traj.resample(10)
```


```python
f=plt.figure(figsize=(20,20))
f,a = S.L.showG('s',fig=f)
for k,nodes in enumerate(t):
    f,a = nodes.plot(fig=f,ax=a)
```

```python
S
```

