```python
from pylayers.gis.ezone import *
import matplotlib.tri as tri
%matplotlib inline
```


```python
z = Ezone('N48W002')
z.loadh5()
z.rebase()
```


```python
# x,y,r,R,dem,LOS,h_earth,diff,fac,nu,numax,LFS,Ltot= z.cov(pc=(11000,45000),Ht=2,Hr=2,Rmax=10000)
```


```python
pc=(11000,45000)
Rmax = 10000
fGHz=0.3
Ht = 2
Hr =2
K = 4/3.
Nphi = 45
Nr = 50
```

Then the coverage zone is defined

```python
lmbda = 0.3/fGHz
phi  = np.linspace(0,2*np.pi,Nphi)[:,None]
r  = np.linspace(0,Rmax,Nr)[None,:]
```


```python
 # cartesian
x  = pc[0] + r*np.cos(phi)
y  = pc[1] + r*np.sin(phi)
extent_c = np.array([x.min(),x.max(),y.min(),y.max()])
lon,lat = z.m(x,y,inverse=True)
# Triangulation
triang = tri.Triangulation(x.flatten(),y.flatten())
# back in lon,lat coordinates
triang.x = x
triang.y = y
rx = np.round((lon - z.extent[0]) / z.lonstep).astype(int)
ry = np.round((z.extent[3]-lat) / z.latstep).astype(int)

```


```python
x.max()
```


```python
x.min()
```


```python
 # dem
dem = z.hgts[ry,rx]
```


```python
dem.shape
```


```python
X=expand(x)
Y=expand(y)
```


```python
X0=expand(pc[0]*np.ones((Nphi,Nr)))
Y0=expand(pc[1]*np.ones((Nphi,Nr)))
```


```python
R=np.sqrt((X0-X)**2+(Y0-Y)**2)
```


```python
R.shape
```


```python
plt.plot(R[0,8,:],'or')
```


```python
r
```


```python
B=r.T[None,1:]-R
```


```python
plt.imshow(B[0,:,:],cmap=plt.cm.jet,vmax=10000)
plt.colorbar()
```


```python
h_earth=(R*B)/(2*K*6375e3)
```


```python
plt.imshow(h_earth[0,:,:],cmap=plt.cm.jet)
plt.colorbar()
```


```python
# ground height + antenna height
Ha = expand((Ht + z.hgts[ry[0,0],rx[0,0]])*np.ones((Nphi,Nr)))
Hb = expand(Hr + dem)
```


```python
# LOS line
LOS  = Ha+(Hb-Ha)*R/r.T[None,1:]
```


```python
LOS.shape
```


```python
plt.imshow(LOS[0,:,:],cmap=plt.cm.jet)
plt.colorbar()
```


```python
diff = expand(dem)+h_earth-LOS
```


```python
plt.imshow(diff[0,:,:],cmap=plt.cm.jet)
plt.colorbar()
```


```python
fac  = np.sqrt(2*r.T[None,1:]/(lmbda*R*B))
nu   = diff*fac
#num,ind  = maxloc(nu)
numax = np.nanmax(nu,axis=2)
u = np.where(numax>-0.7)
w = numax -0.1
L = np.zeros(w.shape)
L[u] = 6.9 + 20*np.log10(np.sqrt(w[u]**2+1)-w[u])
LFS = 32.4 + 20*np.log10(r[0,1:])+20*np.log10(fGHz)
Ltot = LFS+L
```


```python
numax
```


```python
Ltot.shape
```


```python
LOS.shape
```


```python
plt.figure(figsize=(15,8))
plt.imshow(dem,cmap=plt.cm.jet)
```


```python
plt.figure(figsize=(15,8))
plt.imshow(Ltot,cmap=plt.cm.jet)
plt.colorbar()
plt.axis('auto')
```


```python
u=np.argmax(nu,axis=2)
```


```python
plt.imshow(nu[0,:,:],vmin=-0.3,vmax=0.3,cmap=plt.cm.BrBG)
plt.colorbar()
```


```python
#plt.plot(h_earth[0,30,:])
#plt.plot(LOS[0,30,:])
#plt.plot(diff[0,30,:])
#plt.plot(dem[0,:])

```


```python
#plt.plot(nu[0,30,:])
#plt.ylim(0,1)
#plt.plot(8,nu[0,30,8],'or')
```


```python
nu.shape
```


```python
numax2=np.nanmax(nu,axis=2)
```


```python
numax2.shape
```


```python
plt.imshow(numax2,cmap=plt.cm.jet,vmin=-1.4)
plt.colorbar()
```

imax indique le point d'engagement maximum


```python
imax=np.nanargmax(nu,axis=2)
```


```python
imax
```


```python
plt.imshow(imax,cmap=plt.cm.jet)
plt.colorbar()
```

Recherche des coordonnées du point diffractant pour toutes les directions et pour tous les ranges. 


```python
imax.shape
```


```python
iphi = np.arange(Nphi)[:,None]
it = np.arange(0,Nr-1)[None,:]
```


```python
plt.imshow(imax,cmap=plt.cm.jet)
plt.colorbar()
```


```python
for k in range(2,Nphi-1):
    for l in range(1,Nr-1):
        if imax[k,l]!=0:
            t1 = np.arange(0,1,imax[k,l])
            t2 = np.arange(1,0,Nr-imax[k,l])
            t = np.hstack((t1,t2))
```


```python
XM = x[iphi,imax[iphi,it]]
YM = y[iphi,imax[iphi,it]]
```


```python
XM.shape
```


```python
plt.imshow(XM,cmap=plt.cm.jet)
plt.colorbar()
```


```python
plt.imshow(YM,cmap=plt.cm.jet)
plt.colorbar()
```


```python
plt.figure(figsize=(20,20))
ik = 3
#plt.tripcolor(triang,dem.flatten())
f,a,d=z.show(coord='cartesian',extent=extent_c)
a.plot(XM[:,ik],YM[:,ik],'.r')
a.plot(x[:,ik],y[:,ik],'.b')
#plt.axis('equal')
```


```python
RF=np.sqrt((XM[...,None]-x[:,None,:])**2+(YM[...,None]-y[:,None,:])**2)
```


```python
plt.imshow(RF[0,:,:],cmap=plt.cm.jet)
```


```python
plt.plot(x[0,:],y[0,:])
plt.plot(XM[0,:],YM[0,:],'or')
```


```python
RF.shape
```


```python
P=RF[:,0:-1,:]-RF[:,1:,:]
```


```python
import numpy as np
import time
import pdb
from numba import jit
@jit
def splitMDA(imax):
    Nphi,Nl = imax.shape
    N = Nphi*Nl*(Nl+1)
    Ntot = imax.sum()
    u = np.empty((3,Ntot),dtype=int)
    #u1 = np.empty(Ntot)
    #u2 = np.empty(Ntot)
    v = np.empty((3,N-Ntot),dtype=int)
    #v1 = np.empty(N-Ntot)
    #v2 = np.empty(N-Ntot)
    indu = 0
    indv = 0
    for ip in range(Nphi):
        for il in range(Nl):
            for k in range(Nr):
                if k<imax[ip,il]:
                    u[0,indu] = ip
                    u[1,indu] = il
                    u[2,indu] = k
                    indu = indu+1
                else:
                    v[0,indv] = ip
                    v[1,indv] = il
                    v[2,indv] = k
                    indv = indv+1
    #return (u0,u1,u2),(v0,v1,v2)
    return u,v

tic = time.time()
u,v = splitMDA(imax)
toc=time.time()
print toc-tic

```


```python
plt.plot(RF[0,4,:])
```


```python
UL=np.zeros(RF.shape)
UR=np.zeros(RF.shape)
UL[(u[0,:],u[1,:],u[2,:])]=RF[(u[0,:],u[1,:],u[2,:])]
UR[(v[0,:],v[1,:],v[2,:])]=RF[(v[0,:],v[1,:],v[2,:])]
```


```python
k=U[(u[0,:],u[1,:],u[2,:])]=RF[(u[0,:],u[1,:],u[2,:])].max()
```


```python
plt.plot(UL[0,4,:])
plt.plot(UR[0,4,:],'r')
```


```python
import numpy as np
import time
import pdb
from numba import jit
@jit
def splitMDA(imax):
    Nphi,Nl = imax.shape
    N = Nphi*Nl*(Nl+1)
    Ntot = imax.sum()
    u = np.empty((3,Ntot),dtype=int)
    #u1 = np.empty(Ntot)
    #u2 = np.empty(Ntot)
    v = np.empty((3,N-Ntot),dtype=int)
    #v1 = np.empty(N-Ntot)
    #v2 = np.empty(N-Ntot)
    indu = 0
    indv = 0
    for ip in range(Nphi):
        for il in range(Nl):
            for k in range(Nr):
                if k<imax[ip,il]:
                    u[0,indu] = ip
                    u[1,indu] = il
                    u[2,indu] = k
                    indu = indu+1
                else:
                    v[0,indv] = ip
                    v[1,indv] = il
                    v[2,indv] = k
                    indv = indv+1
    #return (u0,u1,u2),(v0,v1,v2)
    return u,v

tic = time.time()
u,v = splitMDA(imax)
toc=time.time()
print toc-tic
```


```python
import numpy as np
import time
import pdb
from numba import jit
#@jit
def cover(dem,X,Y,Ha,Hb,fGHz):
    Nphi,Nl = dem.shape
    #pdb.set_trace()
    print Nphi,Nl
    L = np.zeros((Nphi,Nl,Nl+1))
    for ip in range(Nphi):
        for il in range(Nl):
            uk = range(1,il+2)
            z = np.empty(len(uk))
            for k in uk:
                x = X[ip,:k]
                y = Y[ip,:k]
                z[:k] = dem[ip,:k]
            d = np.sqrt((x-x[0])**2+(y-y[0])**2)
            u = np.arange(len(z))/(len(z)-1.0)
            z[0]  = z[0] + Ha
            z[-1] = z[-1] + Hb
            plt.plot(d,z)
            L[ip,il,k]=interv(z,d,fGHz,0,0)
    return(L)   

#@jit
def interv(z,d,fGHz,L,depth):
    lmbda = 0.3/fGHz
    depth = depth+1
    if depth <3:
        if len(z)>3:
            u = np.arange(len(z))/(len(z)-1.0)
            l = (z[0])*(1-u)+(z[-1])*u
            h = z[1:-1]-l[1:-1]
            nu = h*np.sqrt((2/lmbda)*(1/d[1:-1]+1/(d[-1]-d[1:-1])))
            imax = np.nanargmax(nu)
            numax = nu[imax]
        else:
            numax = -10
        if numax>-0.78:
            w  = numax -0.1
            L  = L + 6.9 + 20*np.log10(np.sqrt(w**2+1)+w)
            z1 = z[0:imax]
            d1 = d[0:imax]
            Ll = interv(z1,d1,fGHz,0,depth)       
            z2 = z[imax:]
            d2 = d[imax:]

            Lr = interv(z2,d2,fGHz,0,depth)
            
            L  = L+Lr+Ll
    return(L)

```


```python
tic = time.time()
L=cover(dem,x,y,1,1,2)
toc=time.time()
print toc-tic
```


```python
x
```


```python
plt.imshow(L[0,:,:],cmap=plt.cm.jet)
plt.colorbar()
```


```python

```
