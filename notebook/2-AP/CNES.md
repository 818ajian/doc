# Example of Utilisation of Coverage

```python
>>> %matplotlib inline
```

```python
>>> from pylayers.antprop.coverage import *
```

```python
>>> C = Coverage('cnes.ini')
```

```python
>>> C
```

```python
>>> fig=figure(figsize=(10,10))
>>> f,a=C.L.showGs(fig=fig)
```

```python
>>> C.L.sl.mat
```

```python
>>> C.L.sl
```

```python
>>> C.L.sla
```

```python
>>> C.cover()
```

```python
>>> fig=plt.figure(figsize=(14,8))
>>> a1 = fig.add_subplot(121)
>>> a2 = fig.add_subplot(122)
>>> f,a = C.show(typ='pr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
>>> f,a = C.show(typ='pr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)
```

```python
>>> fig=plt.figure(figsize=(14,8))
>>> a1 = fig.add_subplot(121)
>>> a2 = fig.add_subplot(122)
>>> f,a = C.show(typ='loss',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
>>> f,a = C.show(typ='loss',best=False,polar='p',vmin=-90,fig=fig,ax=a2)
```

```python
>>> fig=plt.figure(figsize=(14,8))
>>> a1 = fig.add_subplot(121)
>>> a2 = fig.add_subplot(122)
>>> f,a = C.show(typ='snr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
>>> f,a = C.show(typ='snr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)
```

```python
>>> fig=plt.figure(figsize=(14,8))
>>> a1 = fig.add_subplot(121)
>>> a2 = fig.add_subplot(122)
>>> f,a = C.show(typ='sinr',best=False,polar='o',vmin=-90,fig=fig,ax=a1)
>>> f,a = C.show(typ='sinr',best=False,polar='p',vmin=-90,fig=fig,ax=a2)
```

```python
>>> fig=plt.figure(figsize=(14,8))
>>> a1 = fig.add_subplot(121)
>>> a2 = fig.add_subplot(122)
>>> f,a = C.show(typ='capacity',best=False,polar='o',vmin=0,fig=fig,ax=a1)
>>> f,a = C.show(typ='capacity',best=False,polar='p',vmin=0,fig=fig,ax=a2)
```
