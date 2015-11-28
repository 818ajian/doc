# The class Cone

```python
>>> from pylayers.util.cone import *
>>> from pylayers.util.geomutil import *
>>> from pylayers.util.plotutil import *
>>> %matplotlib inline
```

The [`Cone`](http://pylayers.github.io/pylayers/modules/pylayers.util.cone.html) class implements several methods for handling planar cones.

A planar cone is defined as being composed of :
+ an apex $\vec{p}$
+ two vectors $\vec{v}_a$ and  $\vec{v}_b$ not necessarily normalized.

Let create a cone.

```python
>>> va = np.array([2,1])
>>> vb = np.array([1,3])
>>> C = Cone(va,vb,apex=np.array([2,-3]))
```

From those parameters the Cone `__init__` constructs  2 unitary vectors $\hat{u}$ and $\hat{v}$ such that :

+ $\hat{u} \times \hat{v} = c\hat{z} \;\; \textrm{with} \;\; c >0$

This can be interpreted as applying an anticlockwise rotation from $\hat{u}$ to $\hat{v}$.

```python
>>> print "Unitary vector u",C.u
>>> print "Unitary vector v",C.v
>>> print "dot(u,v)",C.dot
>>> print "cross(u,v)",C.cross
```

## Is a point belonging to a cone ? : belong_point()

```python
>>> p = 4*np.random.randn(2,6000)
>>> b = C.belong_point(p)
```

```python
>>> nb = np.array(map(lambda x: not x,b))
>>> pr = p[:,b]
>>> pb = p[:,nb]
```

```python
>>> fig,ax = C.show()
>>> ax.plot(pr[0,:],pr[1,:],'.r')
>>> ax.plot(pb[0,:],pb[1,:],'.b')
>>> plt.axis('equal')
>>> plt.title('belong_cone method')
>>> plt.xlabel('x')
>>> plt.ylabel('y')
>>> #plt.axis('off')
```

## Creating a Cone from 2 segments `from2segs()`

```python
>>> seg0 = np.array([[2,3],[0,0]])
>>> seg1 = np.array([[0,1],[4,4]])
```

```python
>>> Cs=Cone()
```

```python
>>> Cs.from2segs(seg0,seg1)
```

```python
>>> Cs.apex
```

```python
>>> Cs.seg1-seg1
```

```python
>>> Cs.show()
```

```python
>>> b=Cs.belong_point(p)
```

```python
>>> pta = 10*sp.randn(2,1000)
>>> phe = 10*sp.randn(2,1000)
```

```python
>>> nb = np.array(map(lambda x: not x,b))
>>> pr = p[:,b]
>>> pb = p[:,nb]
```

```python
>>> fig,ax = Cs.show()
>>> #displot(pta[:,bs],phe[:,bs],color='k')
... ax.plot(pr[0,:],pr[1,:],'.r')
>>> ax.plot(pb[0,:],pb[1,:],'.b')
>>> plt.axis('equal')
>>> #plt.axis('off')
```

```python
>>> Cs.seg1
```

```python
>>> bi=Cs.belong_point2(p)
```

```python
>>> %timeit b=Cs.belong_point(p)
```

```python
>>> #nb = np.array(map(lambda x: not x,bo))
... pr = p[:,bi]
>>> #pb = p[:,bo2]
... fig,ax = Cs.show()
>>> ax.plot(pr[0,:],pr[1,:],'.r')
>>> #ax.plot(pb[0,:],pb[1,:],'.b')
... plt.axis('equal')
>>> #plt.axis('off')
```

The adressed problem consists in determining whether a segment lies in the cone or not. The condition is satisfied
if not all segments termination are outside the cone on the same side of the cone. This is implemented in the
method `Cone.outside`

```python
>>> b1,b2=Cs.outside_point(p)
```

```python
>>> pr = p[:,b1]
>>> pb = p[:,b2]
>>> fig,ax = Cs.show()
>>> ax.plot(pr[0,:],pr[1,:],'.r')
>>> ax.plot(pb[0,:],pb[1,:],'.b')
>>> plt.axis('equal')
>>> #plt.axis('off')
```

Un cone est un objet qui va servir  construire les objets `Beams`.
Un `Beam` est un `Cone` qui englobe les segments d'une `Signature`.
Une signature et un point donne un `Beam`. A un `Beam` est associ un `Cone`
dont l'apex est une ancre virtuelle.

```python
>>> pta = 10*sp.randn(2,400)
>>> phe = 10*sp.randn(2,400)
```

```python
>>> displot(pta,phe)
```

```python
>>> Cs.seg0
```

```python
>>> typ, proba = Cs.belong_seg(pta,phe)
```

```python
>>> fig,ax = Cs.show()
>>> bs1 = np.where(typ==1)[0]
>>> bs2 = np.where(typ==2)[0]
>>> bs3 = np.where(typ==3)[0]
>>> bs4 = np.where(typ==4)[0]
>>> bs5 = np.where(typ==5)[0]
>>> bs6 = np.where(typ==6)[0]
>>> displot(pta[:,bs1],phe[:,bs1],color='g')
>>> displot(pta[:,bs2],phe[:,bs2],color='b')
>>> displot(pta[:,bs3],phe[:,bs3],color='b')
>>> displot(pta[:,bs4],phe[:,bs4],color='r')
>>> displot(pta[:,bs5],phe[:,bs5],color='r')
>>> #displot(pta[:,bs6],phe[:,bs6],color='m')
... #displot(pta[:,bs],phe[:,bs],color='blue')
```

There is different way to create a `Cone` either from 2 segments `from2segs` or from one point and one segment `fromptseg`. This second method is used when the field is going from a diffraction point to a segment.

## Conditional Graph

$\mathcal{G}_i$ is a `conditional graph` meaning that the edge indicates which is the list of authorized next edge  for the output.
A ray being a sequence ${\nu_k}$ of nodes of $\mathcal{G}_i$.
The cone angular sector represents the whole set and each intercepting segment, is a part or this whole set. This can be interpreted as a probability. This means that the research of rays could be done stochastically in a very efficient manner. This is not fully implemented yet.

```python
>>> Cb = Cone()
```

```python
>>> Cb.u
```

```python
>>> seg = np.array([[1,2],[2,2]])
>>> pt = np.array([0,0])
```

```python
>>> Cb.fromptseg(pt,seg)
```

```python
>>> typ,proba = Cb.belong_seg(pta,phe)
>>> bs = np.where(typ>0)[0]
```

```python
>>> Cb.seg1
```

```python
>>> Cb.show()
>>> displot(pta[:,bs],phe[:,bs],color='k')
```

### Benchmark normalizing a vector

```python
>>> a = np.array([5,6])
```

```python
>>> %timeit a/np.sqrt(np.dot(a,a))
```

```python
>>> %timeit a/sp.linalg.norm(a)
```

```python
>>> %timeit a/np.sqrt(np.sum(a*a,axis=0))
```

## Debug

This a case which where segments `seg0` and `seg1` are orthogonal

```python
>>> seg0 = array([[-25.768, -25.822],
...        [  4.28 ,   9.925]])
```

```python
>>> seg1 = array([[-26.848, -26.805],
...        [  5.415,   4.515]])
```

```python
>>> cn = Cone()
```

```python
>>> cn.from2segs(seg0,seg1)
```

```python
>>> pta =array([[-27.836, -27.833, -27.833, -27.817, -26.848, -27.774, -26.952,
...         -28.062],
...        [ 10.926,  10.686,  10.686,   8.956,   5.415,   4.506,  10.934,    8.954]])
```

```python
>>> phe = array([[-27.835, -27.835, -28.078, -27.774, -26.882, -26.805, -27.836,
...         -28.078],
...        [ 10.891,  10.891,  10.683,   4.506,   8.965,   4.515,  10.926,
...          10.683]])
```

```python
>>> typ,proba = cn.belong_seg(pta,phe)
>>> bn = np.where(typ==0)[0]
```

```python
>>> proba
```

```python
>>> cn.show()
>>> displot(pta[:,bn],phe[:,bn])
```

```python
>>> pta1=pta[:,5].reshape(2,1)
>>> phe1=phe[:,5].reshape(2,1)
```

```python
>>> cn.show()
>>> displot(pta1,phe1)
```

```python
>>> b = cn.belong_seg(pta1,phe1)
```

## geomutil.mirror

```python
>>> p = np.random.randn(2,10000)
>>> pa  = np.array([-1,1]).reshape(2,1)
>>> pb  = np.array([-1,3]).reshape(2,1)
>>> M = geu.mirror(p,pa,pb)
```

```python
>>> M
```

```python
>>> figsize(20,20)
>>> displot(pa,pb)
>>> plot(p[0,:],p[1,:],'or',alpha=0.2)
>>> plot(M[0,:],M[1,:],'ob',alpha=0.2)
```

```python
>>> pa=np.array([0,0]).reshape(2,1)
>>> pb=np.array([1,0]).reshape(2,1)
>>> pc=np.array([1,0]).reshape(2,1)
```

```python
>>> geu.isaligned(pa,pb,pc)
```

## Geometric probability

The idea is to add an information of the fraction of the angular sector which is subtended by the intercepted segment.

```python
>>> a = np.array([2,1])
>>> b = np.array([1,3])
>>> C = Cone(a,b,apex=np.array([2,-3]))
```

```python
>>> import scipy as sp
>>> pta = np.array([2,-1]).reshape(2,1)
>>> phe = np.array([5.99,-1]).reshape(2,1)
>>> pta = 10*sp.randn(2,1000)
>>> phe = 10*sp.randn(2,1000)
>>> typ,proba = C.belong_seg(pta,phe)
>>> u0 = np.where(typ==0)[0]
>>> u1 = np.where(typ==1)[0]
>>> u2 = np.where(typ==2)[0]
>>> u3 = np.where(typ==3)[0]
>>> u4 = np.where(typ==4)[0]
>>> u5 = np.where(typ==5)[0]
>>> u6 = np.where(typ==6)[0]
>>> us = np.where( ((proba<0.1) & (proba>0)) )  [0]
```

```python
>>> C.show()
>>> #col=['r','g','b','m']
... try:
...     displot(pta[:,us],phe[:,us],color='k')
>>> except:
...     pass
```

```python
>>> C.show()
>>> #col=['r','g','b','m']
... try:
...     displot(pta[:,u1],phe[:,u1],color='r')
>>> except:
...     pass
>>> print proba[u1]
```

```python
>>> C.show()
>>> 
>>> try:
...     displot(pta[:,u2],phe[:,u2],color='g')
>>> except:
...     pass
>>> print(proba[u2])
```

```python
>>> C.show()
>>> try:
...     displot(pta[:,u3],phe[:,u3],color='b')
>>> except:
...     pass
>>> print(proba[u3])
```

```python
>>> C.show()
>>> try:
...     displot(pta[:,u4],phe[:,u4],color='m')
>>> except:
...     pass
>>> print(proba[u4])
```

```python
>>> C.show()
>>> try:
...     displot(pta[:,u5],phe[:,u5],color='k')
>>> except:
...     pass
```

```python
>>> C.show()
>>> try:
...     displot(pta[:,u6],phe[:,u6],color='k')
>>> except:
...     pass
```
