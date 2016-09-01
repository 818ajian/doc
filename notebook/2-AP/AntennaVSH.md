# Vector Spherical Harmonics Representation of Antennas

```python

from pylayers.antprop.antenna import *

from pylayers.antprop.antvsh import *

%matplotlib inline
```

Loading an Antenna from a Matlab file

```python

A = Antenna('S2R2.mat',directory='ant/UWBAN/Matfile')
```

The shape of the $F_{\phi}$ functions indicates :

- $N_{\theta} = 91$
- $N_{\phi} = 180 $
- $N_f= 104$

```python
np.shape(A.Fp)
```

The frequency array is expressed in $GHz$ and delays are expressed in $ns$

```python
fGHz = A.fGHz
```

```python
fGHz.shape
```

Then an electrical delay of $4.185ns$ is applied on the $F_{\theta}$

```python
I = A.Ft[:,:,:]
```

```python
I.shape
```

```python

plt.figure(figsize=(10,8))

plt.imshow(np.unwrap(np.angle(I[:,45,:])))

plt.title(r'Unwrapped phase of $F_{\theta}$ w.r.t frequency and phi for $\theta=\frac{pi}{2}$')

plt.ylabel('f index')

plt.colorbar()

plt.figure()

plt.plot(fGHz,np.unwrap(np.angle(I[45,85,:])))

plt.xlabel('f index')

```

```python

tau=4.185

I = A.Ft[:,:,:]*np.exp(-2*1j*np.pi*fGHz[None,None,:]*tau)
```

```python

plt.imshow(np.unwrap(np.angle(I[:,45,:])))

plt.title(r'Unwrapped phase of $F_{\theta}$ w.r.t frequency and phi for $\theta=\frac{pi}{2}$')

plt.ylabel('f index')

plt.colorbar()

plt.figure()

plt.plot(fGHz,np.unwrap(np.angle(I[45,85,:])))

```

##### Display of the radiation pattern for all frequencies

```python

plt.figure(figsize=(10,10))

for nf in range(104):
    plt.polar(A.phi,abs(A.Ft[45,:,nf]))
```

```python

A.info()
```

# Evaluation of Vector Spherical Harmonics Coefficients

At that stage we compute the Vector Spherical Harmonics coefficients

```python

A=vsh(A)
```

```python

A.info()
```

```python

A.C.s1tos2(30)
```

```python

A.C
```

```python

fig = plt.figure(figsize=(8,8))

A.C.show('s2',k=300)
```

```python

A.C.s2tos3()
```

```python

A.C
```

```python

fig = plt.figure(figsize=(8,8))

A.C.show('s3')

plt.tight_layout()
```
