r"""
===========================================
8 Random Layout 
===========================================

This example display randomly N layout from 
the set of all available Layout file

The file extension is .lay

"""
from pylayers.gis.layout import Layout
import matplotlib.pyplot as plt 
import random
import warnings

warnings.filterwarnings("error")
L = Layout()
lL = L.ls()
N = 8
for tL in random.sample(lL,N):
    if 'Munich' not in tL:
        L = Layout(tL,bbuild=0,bgraphs=0)
        f,a = L.showG('s')
        plt.title(tL,fontsize=32)
        plt.show()
