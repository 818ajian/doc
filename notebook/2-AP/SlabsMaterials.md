```python
!date
```

# Slabs and Materials

```python
%matplotlib inline
```

A slab is a set ol several layers of materials with specified thickness. 
Slabs are used to describe properties of the different constitutive elements of a
building such as wall, windows,...

In practice when describing a specific building, it is necessary to specify a set of different slabs with different characteristics.

A structure which gathers this set is `SlabDB`. If no file argument is given,
this structure is initialized with the default file:
[slabDB.ini](https://github.com/pylayers/pylayers/blob/master/data/ini/slabDB.ini)

This section demonstrates some features of the `pylayers.antprop.slab` module.

```python
from pylayers.antprop.slab import *
```

The Class `SlabDB` contains a dictionnary of all available Slabs. This
information is read in the file `slabDB.ini` of the current project pointed by
environment variable `$BASENAME`

```python
S = SlabDB('slabDB.ini')
```

A SlabDB is a dictionnary, the keys are for the current file are shown below

```python
S.keys()
```

## Defining a new Slab and a new Material

```python
S.add('slab2',['STONE'],[0.15])
```

```python
S.mat['STONE']
{'epr': (8.69999980927+0j),
 'index': 8,
 'mur': (1+0j),
 'name': 'STONE',
 'roughness': 0.0,
 'sigma': 3.0}
```

```python
S['slab2']['lmatname']
['STONE']
```

```python
S['slab2']['lthick']
[0.15]
```

```python
fGHz= np.arange(3,5,0.01)
theta = np.arange(0,np.pi/2,0.01)
S['slab2'].eval(fGHz,theta)
```

```python
fig = plt.figure(figsize=(10,10))
S['slab2'].pcolor()
```

```python
A=S['slab2']
```

As any PyLayers object there is an `help` function for getting a listing of which methods are implemented in the class.

```python
A.help()
```

## Information necessary to define a Slab

Each slab contains informations about its constitutive materials electromagnetic properties.

Below an example for a simple slab, constituted with a single material slab. The slab 'WOOD' is a layer of 4cm 'WOOD' material.

```python
S['WOOD']['lmatname']
```

thickness is expressed in meters

```python
S['WOOD']['lthick']
```

```python
S['WOOD']['color']
```

```python
S['WOOD']['linewidth']
```

Multi layers Slab, using different stacks of materials can be easily defined using the two lists **lmatname** and **lthick**.

> Notice the adopted convention naming lists starting with letter 'l' and dictionnaries  starting with letter 'd'

```python
S['3D_WINDOW_GLASS']['lmatname']
```

```python
S['3D_WINDOW_GLASS']['lthick']
```

For each constitutive material of a slab, their electromagnetic properties can be obtained as:

```python
S['3D_WINDOW_GLASS']['lmat']
```

## Evaluation of a Slab

Each Slab can be evaluated to obtain the Transmission and Reflexion coefficients for

+ a given frequency range
+ a given incidence angle range  ($0\le\theta<\frac{\pi}{2}$)

```python
fGHz = np.arange(3,5,0.01)
theta = np.arange(0,np.pi/2,0.01)

S['WOOD'].eval(fGHz,theta,compensate=True)
sR = np.shape(S['WOOD'].R)
print '\nHere, slab is evaluted for',sR[0],'frequency(ies)', 'and',sR[1], 'angle(s)\n'
```

## Transmission and Reflexion coefficients

Reflexion and transmission coefficient are computed for the given frequency range and theta range

```python
ifreq=1
ithet=10
print '\nReflection coefficient @',fGHz[ifreq],'GHz and theta=',theta[ithet],':\n\n R=',S['WOOD'].R[0,0]
print '\nTransmission coefficient @',fGHz[ifreq],'GHz and theta=',theta[ithet],':\n\n T=',S['WOOD'].T[0,0],'\n'
```

### Ploting Reflection and Transmission Coefficients

The method `plotwrt` can plot the different calculated coefficients with respect to angle or frequency.

```python
S['WOOD']['lthick']=[0.02]
S['WOOD'].eval()
S['WOOD'].eval()
f,a=S['WOOD'].plotwrt()
```

```python
fGHz = np.arange(1,10,0.01)
theta = np.arange(0,np.pi/2,0.01)

S['3D_WINDOW_GLASS']['lthick']=[0.006,0.01,0.006]
#S['3D_WINDOW_GLASS']['lmatname']=['GLASS','AIR','GLASS']
S['3D_WINDOW_GLASS'].eval(fGHz,theta)
```

plotwrt : plot with respect to frequency

```python
fig,ax = S['3D_WINDOW_GLASS'].plotwrt(var='f',coeff='T',polar='o')
```

plot with respect to angles

```python
fig = plt.figure(figsize=(20,20))
fGHz= np.array([2.4])
S['WOOD'].eval(fGHz,theta)
fig,ax = S['WOOD'].plotwrt(var='a',coeff='R',fig=fig)
plt.tight_layout()
```

wrt to angle and frequency, use pcolor

```python
plt.figure(figsize=(10,10))
fGHz= np.arange(0.7,5.2,0.1)
S['WOOD'].eval(fGHz,theta)
S['WOOD'].pcolor()
```

```python
theta = np.arange(0,np.pi/2,0.01)
fGHz = np.arange(0.1,10,0.2)
sl = SlabDB('matDB.ini','slabDB.ini')
mat   = sl.mat
lmat  = [mat['AIR'],mat['WOOD']]
II    = MatInterface(lmat,0,fGHz,theta)
II.RT()
fig,ax = II.plotwrt(var='a',kv=10,typ=['m'])
plt.tight_layout()
air = mat['AIR']
brick  = mat['BRICK']
II  = MatInterface([air,brick],0,fGHz,theta)
II.RT()
fig,ax = II.plotwrt(var='f',color='k',typ=['m'])
plt.tight_layout()
```

## Adding new slab and materials 

```python
theta = np.arange(0,np.pi/2,0.01)
fGHz = np.arange(0.1,10,0.2)
sl = SlabDB('matDB.ini','slabDB.ini')
sl.mat.add(name='AIR2',cval=1.00000001+0j,sigma=0.00,typ='epsr')

sl.add(name='AIR-5cm',lmatname=['AIR2','AIR2'],lthick=[0.05,0.05])
sl.add(name='AIR-10cm',lmatname=['AIR2','AIR2'],lthick=[0.10,0.10])
sl.add(name='AIR-50cm',lmatname=['AIR2','AIR2'],lthick=[0.15,0.15])
fGHz=4
theta = np.arange(0,np.pi/2,0.01)
#figure(figsize=(8,8))
# These Tessereau page 50
sl['AIR-5cm'].eval(fGHz,theta,compensate=True)
sl['AIR-10cm'].eval(fGHz,theta,compensate=True)
sl['AIR-50cm'].eval(fGHz,theta,compensate=True)

# by default var='a' and kv = 0
fig,ax = sl['AIR-5cm'].plotwrt(color='k',labels=['5cm'])
fig,ax = sl['AIR-10cm'].plotwrt(color='k',labels=['10cm'],linestyle='dashed',fig=fig,ax=ax)
fig,ax = sl['AIR-50cm'].plotwrt(color='k',labels=['15cm'],linestyle='dashdot',fig=fig,ax=ax)
plt.tight_layout()
```

## Evaluation without phase compensation

```python
fGHz = np.arange(2,16,0.1)
theta = 0

sl['AIR-5cm'].eval(fGHz,theta,compensate=False)
sl['AIR-10cm'].eval(fGHz,theta,compensate=False)
sl['AIR-50cm'].eval(fGHz,theta,compensate=False)

fig,ax = sl['AIR-5cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='r')
#print ax
fig,ax = sl['AIR-10cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='g',fig=fig,ax=ax)
fig,ax = sl['AIR-50cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='b',fig=fig,ax=ax)
sl['AIR-5cm'].eval(fGHz,theta,compensate=True)
sl['AIR-10cm'].eval(fGHz,theta,compensate=True)
sl['AIR-50cm'].eval(fGHz,theta,compensate=True)

# by default var='a' and kv = 0
fig,ax = sl['AIR-5cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='r',linestyle='dashdot',fig=fig,ax=ax)
fig,ax = sl['AIR-10cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='g',linestyle='dashed',fig=fig,ax=ax)
fig,ax = sl['AIR-50cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='b',linestyle='dashdot',fig=fig,ax=ax)
plt.tight_layout()
```

```python
from pylayers.signal.bsignal import *
```

```python
sl['AIR-5cm'].eval(fGHz,theta,compensate=False)

S = sl['AIR-5cm']
f=S.fGHz
y = S.T[:,0,0,0]
F=FUsignal(f[:,0],y)
```

```python
g=F.ift(ffts=1)
```

```python
g.plot(typ='v')
```

```python
sl['AIR-5cm'].eval(fGHz,theta,compensate=True)
sl['AIR-10cm'].eval(fGHz,theta,compensate=True)
sl['AIR-50cm'].eval(fGHz,theta,compensate=True)

fig,ax = sl['AIR-5cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='k')
#print ax
fig,ax = sl['AIR-10cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='k',linestyle='dashed',fig=fig,ax=ax)
fig,ax = sl['AIR-50cm'].plotwrt('f',coeff='T',typ=['ru'],labels=[''],color='k',linestyle='dashdot',fig=fig,ax=ax)
plt.tight_layout()
```

```python
sl.mat.add(name='ConcreteJc',cval=3.5,alpha_cmm1=1.9,fGHz=120,typ='THz')
sl.mat.add(name='GlassJc',cval=2.55,alpha_cmm1=2.4,fGHz=120,typ='THz')
sl.add('ConcreteJc',['ConcreteJc'],[0.049])

theta = np.linspace(20,60,100)*np.pi/180
sl['ConcreteJc'].eval(120,theta)
fig,ax = sl['ConcreteJc'].plotwrt('a')
```

```python
plt.figure(figsize=(20,10))
fGHz = np.linspace(110,135,50)
sl.add('DoubleGlass',['GlassJc','AIR','GlassJc'],[0.0029,0.0102,0.0029])
sl['DoubleGlass'].eval(fGHz,theta)
sl['DoubleGlass'].pcolor(dB=True)
```

```python
f = plt.figure(figsize=(4,4))
f = sl['DoubleGlass'].eval(120,theta)
fig,ax = sl['DoubleGlass'].plotwrt('a',figsize=(10,10))
plt.tight_layout()
```

```python
freq = np.linspace(110,135,50)
sl['DoubleGlass'].eval(freq,theta)
fig,ax = sl['DoubleGlass'].plotwrt('f',figsize=(10,10))  # @20
plt.tight_layout()
```

## References

[1]. [Jacob, M. ; Kurner, T. ; Geise, R. ; Piesiewicz, R.  "Reflection ant Transmission Properties of Building Materials in D-Band for Modeling Future mm-Wave Communication Systems" Antennas and Propagation (EuCAP), 2010 Proceedings of the Fourth European Conference on](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=5505315&queryText%3DReflection+ant+Transmission+Properties+of+Building+Materials+in+D-Band+for+Modeling+Future+mm-Wave+Communication+Systems.QT.+Antennas+and+Propagation)



[2]. [R.Piesiewicz 'Terahertz characterization of building materials'  Electronics .Letters Jan 2005 Vol 41 N18](https://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CCwQFjAA&url=http%3A%2F%2Fwww-ece.rice.edu%2F~daniel%2Fpapers%2FnormanElecLett.pdf&ei=Tr_eUe6EG-OM0AWA0IAw&usg=AFQjCNHzt9H3RkLAtws51E9EpEgyqh-6LA&sig2=QLZlhoTJtiuHAW5Zzg_xOw&bvm=bv.48705608,d.d2k)
