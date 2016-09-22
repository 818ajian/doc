# Scalar Spherical Harmonics

```python
from pylayers.antprop.antenna import *
from pylayers.antprop.antssh import *
%matplotlib inline
```

```python
A = Antenna('S1R1.mat',directory='ant/UWBAN/Matfile')
```

```python
A
```

```python
A.nf
```

To calculate scalar spherical harmonics use method `ssh(A,L)`

```python
L = 5
A = ssh(A,L=5)
```

```python
A
```

```python
plt.plot(abs(A.S.Cx.s2[0]))
```

```python
A.savesh2()
```

```python
A.loadsh2()
```

```python
plt.plot(abs(A.S.Cx.s2[0]))
```

```python
A.S.s2tos3()
```

```python
plt.plot(abs(A.S.Cx.s3[0]))
```

```python
A.S.Cx.ind2.shape
```

```python
A.savesh3()
```

```python
plt.plot(abs(A.S.Cx.s2[0]))
```

```python
A.loadsh3()
```

```python
plt.plot(abs(A.S.Cx.s3[100]))
```

```python
plt.plot(abs(A.S.Cx.s2[100]))
```

```python
A.__dict__.keys()
```

```python
A.S.Cx.__dict__.keys()
```

```python
A.S.Cx
```
