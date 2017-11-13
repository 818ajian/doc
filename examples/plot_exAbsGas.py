# -*- coding: utf-8 -*-
r"""
=================================================
Attenuation due to atmospheric gases
=================================================

This is an implementation of the recommandation [ITU-R P676-10](https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.676-10-201309-S!!PDF-E.pdf)

The function is implemented in pylayers/antprop/loss.py module

"""
from pylayers.antprop.loss import *

# set the temperature to 15deg Celsius
T = 15
# set the atmospheric pressure
PhPa = 1013
# set the wave vapor density ( g/m^3)
wvden = 7.5
# set distance in meters 
d = 1000
fGHz = np.linspace(1,1000,500)
# calculate specific attenuation (wet)
Lw= gaspl(d,fGHz,T,PhPa,wvden)
# calculate specific attenuation (dry)
Ls= gaspl(d,fGHz,T,PhPa,0)
fs = 18
plt.semilogy(fGHz,Lw,linewidth=2)
plt.semilogy(fGHz,Ls,'r',linewidth=2)
plt.grid(True,which="both",ls='--')
plt.xlabel('Frequency (GHz)',fontsize=fs)
plt.ylabel('Specific Attenuation (dB)',fontsize=fs)
plt.show()
