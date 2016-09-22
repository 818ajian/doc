# Modelisation of the Thermal Noise

```python
from pylayers.signal.bsignal import *
%matplotlib inline
```

The bsignal module has a dedicated class for handling noise signal. To create a white noise just type :

```python
w = Noise()
```

The representation of the noise object provides information about default values. In digital representation of noise the sampling frequency is important. The noise signal is generated from a time $t_i$ to a time $t_f = t_i+T$. The default power spectral density is $-174dBm/Hz$ and can be modified with the argument `PSDdBmpHz`.

```python
w
```

```python
f,a=w.plot(typ='v')
```

```python
w.psd()
```

```python
w2 = w.fgating(fcGHz=4,WGHz=3)
```

```python
W2=w2.psd()
W2.plotdB(mask=True)
```

```python
w.plot(typ='v')
```

```python
ip=TUsignal()
ip.EnImpulse(fcGHz=4.4928,WGHz=0.4992,feGHz=100)
```

```python
#fig = plt.figure(figsize=(10,10))
#for k,snr in enumerate(range(30,-30,-10)):
#    a = fig.add_subplot(3,2,k+1)
#    ipn,n=ip.awgn(snr=snr,typ='snr')
#    ipn.plot(typ='v',fig=fig,ax=a)
#    a.set_title('SNR :'+str(snr)+' dB')
#plt.tight_layout()
```

