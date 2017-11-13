# -*- coding: utf-8 -*-
r"""
=======================================================
Antenna Pattern for an H plane sectoral antenna @ 32GHz
=======================================================

"""
from pylayers.antprop.antenna import *
A = Antenna('hplanesectoralhorn',fGHz=32)
f,a = A.plotG(plan='theta',angdeg=0,color='b')
f,a = A.plotG(plan='theta',angdeg=90,fig=f,ax=a)
plt.show()
