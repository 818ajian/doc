```python
!date
```

#Network Simulation Configuration

```python
import ConfigParser
from IPython.display import FileLink
import pylayers.util.pyutil as pyu
```

PyLayers is designed to provide indoor radio channel simulation for mobile agents.

The goal is to address mobility in indoor environment heterogeneous network, with human being carriers of a mobile User Equipement (UE) which possibly embeds several Radio Acess Technology (RAT).

Several humans can be created and their motion in the environement should be as realistic as possible, because for many applications it turns out that many parameters of interest
are stongly dependent of the dynamic topology of the mobile network.

In the following the configuration files for proceeding with those high level `PyLayers` simulation are described.

The configuration file is `simulnet.ini`

## Simulnet.ini

This file is assumed to be located in `$BASENAME/ini`. As the format of this file is not stable yet. Refer to the comment in the file below for obtaining the inforamtion about the format.

```python
!cat $BASENAME/ini/simulnet.ini
```

```python
Cp = ConfigParser.ConfigParser()
Cp.read(pyu.getlong('simulnet.ini','ini'))
```

Current version of `Simulnet.ini` contains the following sections

```python
Cp.sections()
```

### Save section

The save section handles the output files of the simulation.

```python
dict(Cp.items('Save'))
```

The `savep` boolean enable/disable saving of the simulation.

```python
dict(Cp.items('Save'))['savep']
```

The log file which contains all traces from the simulated dynamics are in `$BASENAME/netsave`

```python
!ls $BASENAME/netsave/*
```

### Layout section

This section specifies the layout parameter and spatial dimension of the simulation

```python
dict(Cp.items('Layout'))
```

Choose the used Layout for simulation

```python
dict(Cp.items('Layout'))['filename']
```

Setup an offset for defining the coordinate system origin

```python
print dict(Cp.items('Layout'))['x_offset']
print dict(Cp.items('Layout'))['y_offset']
```

### Network section

```python
dict(Cp.items('Network'))
```

Setup communication mode between node:

+ `"autonomous"` : the data exchange between nodes is driven by the localization layer. If more information is required to estimate the position then a communication request is sent to the communication state
+ `"synchro"` : the data exchange between nodes is periodic. LDPs are periodically refreshed at the `network_update_time`

```python
dict(Cp.items('Network'))['communication_mode']
```

Time step for the refresh network information

```python
dict(Cp.items('Network'))['network_update_time']
```

Vizualization of the simulation using matplotlib

```python
dict(Cp.items('Network'))['show']
```

Vizualization of a table summing up the data exchange of the nodes

```python
dict(Cp.items('Network'))['show_table']
```

Vizualization of the simulation inside ipython notebook

```python
dict(Cp.items('Network'))['ipython_nb_show']
```

## Mechanics

This section specifies agents dynamic during simulation

```python
dict(Cp.items('Mechanics'))
```

Setup how agent choose their target:

+ `"random"`: the agnet move into the layout randomly
+ `"file"` : the agent follow the sequence specified in `<project_dir>/nodes_destination.ini`

```python
dict(Cp.items('Mechanics'))['choose_destination']
```

Time step for refreshing the mechanical layer (ground truth position)

```python
dict(Cp.items('Mechanics'))['mecanic_update_time']
```

### Localization section
Setup Localization algorithms

```python
dict(Cp.items('Localization'))
```

enable/disable localization of the agents

```python
dict(Cp.items('Localization'))['localization']
```

Select localization methods :

+ Algebraic : heterogeneous localization algorithm
+ Geometric : RGPA

```python
dict(Cp.items('Localization'))['method']
```

Time step for localization update

```python
dict(Cp.items('Localization'))['localization_update_time']
```

### Simulation section

```python
dict(Cp.items('Simulation'))
```

Setup simulation duration in second

```python
dict(Cp.items('Simulation'))['duration']
```

Setup random seed for simulation

```python
dict(Cp.items('Simulation'))['seed']
```

Display messages during simulation

```python
dict(Cp.items('Simulation'))['verbose']
```

See Also Mobility_

.. _Mobility: ../4-MOB/Mobility.html
