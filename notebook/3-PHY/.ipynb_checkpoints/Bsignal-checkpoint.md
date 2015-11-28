# Handling time and frequency domain signals : `Bsignal` Class

This section presents some features of the classes implemented in the [`pylayers.signal.bsignal.py`](http://pylayers.github.io/pylayers/modules/pylayers.signal.bsignal.html) module.

```python
>>> %matplotlib inline
```

The `Bsignal` class is a container for a signal with a base which can be either in time domain or frequency domain.

```python
>>> from pylayers.signal.bsignal import *
>>> from matplotlib.pyplot import *
```

As a first example, let construct an impulse signal normalized in energy. To do so there exist a specialized function : [`EnImpulse`](http://pylayers.github.io/pylayers/modules/generated/pylayers.signal.bsignal.EnImpulse.demo.html#pylayers.signal.bsignal.EnImpulse.demo)

```python
>>> E=EnImpulse(fe=40)
```

```python
>>> >>> from pylayers.signal.bsignal import *
>>> >>> ip    = EnImpulse(fc=4,band=3,thresh=10,fe=100)
>>> >>> Eip1  = ip.energy()
>>> >>> ESDu  = ip.esd(mode='unilateral')
>>> >>> ESDb  = ip.esd(mode='bilateral')
>>> >>> df    = ESDu.dx()
>>> >>> Eipu  = sum(ESDu.y)*df
>>> >>> Eipb  = sum(ESDb.y)*df
>>> >>> erru  = Eip1-Eipu
>>> >>> errb  = Eip1-Eipb
```

```python
>>> Eipu
1.0000000388319035
```

```python
>>> print Eip1
100.000007743
```

```python
>>> E.plot(typ='v')
(<matplotlib.figure.Figure at 0x7f209264ead0>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f209265e350>]], dtype=object))
```

```python
>>> E.energy()
40.000003097054716
```

The Fourier transform of this signal has the hermitian Symmetry.

```python
>>> F = E.fft()
>>> F.plot(typ='m')
(<matplotlib.figure.Figure at 0x7f20925fb610>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f2092418990>]], dtype=object))
```

```python
>>> F.y[0]
(0.00029728997658457938+0j)
```

We then extract the non redundant part of the signal with the `ft` method

```python
>>> G=E.ft()
```

```python
>>> GH=G.symHz(100,scale='extract')
```

```python
>>> print GH.y[1]
>>> print GH.y[-1]
(-0.0014441784194-4.88037298122e-05j)
(-0.0014441784194+4.88037298122e-05j)
```

```python
>>> ip=F.ifft()
>>> ip2=GH.ifft()
```

```python
>>> f,a=E.plot(typ='v',labels=['original'])
>>> f,a=ip.plot(typ='v',fig=f,ax=a[0][0],labels=['no zero padding'])
>>> f,a=ip2.plot(typ='v',fig=f,ax=a[0][0],labels=['zero padding'])
>>> title('extract mode')
```

```python
>>> ip.energy()
40.000003097054773
```

```python
>>> ip2.energy()
401.35111446263471
```

```python
>>> Y=E.esd()
```

FHsignal for in CIR mode
------------------------

We create a Fusignal which corresponds to the signal

$$X_u(f) = \alpha e^{-2j\pi f \tau}$$

$$f\in [f_{min},f_{max}]$$

```python
>>> f = np.arange(2,10,0.01)
>>> y = 2*np.ones(len(f))*np.exp(-2*1j*np.pi*f*3)
>>> N = len(f)
>>> Hu = FUsignal(f,y)
>>> print N
800
```

```python
>>> Hu.plot(typ='m')
(<matplotlib.figure.Figure at 0x7f20924d1c10>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f209256d2d0>]], dtype=object))
```

```python
>>> hu = Hu.ifft()
```

The inverse Fourier transform allows to recover perfectly the amplitude $\alpha$ and the delay $\tau$
of the channel

```python
>>> hu.plot(typ='m')
(<matplotlib.figure.Figure at 0x7f20921f8b50>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f20921dc510>]], dtype=object))
```

```python
>>> real=np.imag(hu.y)
>>> u = np.where(hu.y==max(hu.y))[0]
>>> tau = hu.x[u]
>>> alpha = abs(hu.y[u])
>>> print alpha,tau
[ 2.] [ 3.00375469]
```

```python
>>> H = Hu.symHz(100,scale='cir')
```

```python
>>> H.plot(typ='m')
(<matplotlib.figure.Figure at 0x7f20921a3e50>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f2092418dd0>]], dtype=object))
```

```python
>>> h = H.ifft()
```

```python
>>> h.plot(typ='v')
(<matplotlib.figure.Figure at 0x7f2092055cd0>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f209204c5d0>]], dtype=object))
```

```python
>>> real=np.imag(h.y)
>>> u = np.where(h.y==max(h.y))[0]
>>> tau = h.x[u]
>>> alpha = abs(h.y[u])
>>> print alpha,tau
[ 1.97995425] [-46.97864607]
```

```python
>>> fft.ifft(H.y)
array([ -1.93565190e-15 -1.70240923e-19j,
         2.62295322e-04 -3.27871407e-19j,
         8.73458329e-04 -4.09839258e-20j, ...,
        -1.06670199e-04 +2.90350482e-19j,
        -8.69428086e-04 -1.58117458e-18j,  -5.31550980e-05 -2.71727936e-20j])
```

```python
>>> print H.y[203]
>>> print H.y[-203]
>>> len(H.y)
(0.116169256529-0.0459946624208j)
(0.116169256529+0.0459946624208j)
2201
```

```python
>>> Y=h.fft()
```

```python
>>> Y.plot(typ='m')
(<matplotlib.figure.Figure at 0x7f2092000bd0>,
 array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7f2091feb950>]], dtype=object))
```
