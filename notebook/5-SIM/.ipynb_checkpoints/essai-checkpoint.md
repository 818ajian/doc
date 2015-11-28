# This is a test

```python
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> from IPython.display import Image,HTML,YouTubeVideo,SVG
```

```python
>>> x = np.linspace(-5,5,100)
```

```python
>>> y = np.sin(2*x)*np.cos(20*x)
```

```python
>>> plt.plot(x,y)
>>> plt.savefig('fig1.png',dpi=70)
```

$$E=m c^{2}$$

![Ma figure](fig1.png)

```python
>>> Image('fig1.png')
<IPython.core.display.Image object>
```

```python

```
