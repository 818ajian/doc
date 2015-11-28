
.. code:: python

    #!/usr/bin/python
    import time
    import matplotlib as ml
    import matplotlib.pyplot as plt
    import numpy as np
    from types import *
    from numpy import array
    %matplotlib inline
    import pylayers.measures.vna.E5072A
.. code:: python

    vna = E5072A.SCPI("129.20.33.201",verbose=False)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-e4e949882bf3> in <module>()
    ----> 1 vna = E5072A.SCPI("129.20.33.201",verbose=False)
    

    NameError: name 'E5072A' is not defined


.. code:: python

    # open remote measurement device (replace "hostname" by its actual name)
    data = vna.getIdent()
    print "Instrument ID : ",data

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-979c045b8d63> in <module>()
          1 # open remote measurement device (replace "hostname" by its actual name)
    ----> 2 data = vna.getIdent()
          3 print "Instrument ID : ",data


    NameError: name 'vna' is not defined


.. code:: python

    vna.s.send('')

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-f42acd5bcc38> in <module>()
    ----> 1 vna.s.send('')
    

    NameError: name 'vna' is not defined


.. code:: python

    vna.select(param='S21',chan=1)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-d72ae2afb63f> in <module>()
    ----> 1 vna.select(param='S21',chan=1)
    

    NameError: name 'vna' is not defined


.. code:: python

    com =":SWE:POIN 1201"
    vna.write(com)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-d5dd3b30e9b2> in <module>()
          1 com =":SWE:POIN 1201"
    ----> 2 vna.write(com)
    

    NameError: name 'vna' is not defined


.. code:: python

    com = ":SENS1:FREQ:DATA?\n"
    tab = vna.read(com)
    f = np.frombuffer(tab,'>f8')
    freq = f[1:]
    plt.plot(freq)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-f8cd45896ac0> in <module>()
          1 com = ":SENS1:FREQ:DATA?\n"
    ----> 2 tab = vna.read(com)
          3 f = np.frombuffer(tab,'>f8')
          4 freq = f[1:]
          5 plt.plot(freq)


    NameError: name 'vna' is not defined


.. code:: python

    try:
        del res
    except:
        pass
    com1 = "FORM:DATA REAL"
    com2 = "TRIG:SING"
    vna.write(com1)
    vna.write(com2)
    u = np.arange(0,201)*2
    v = np.arange(0,201)*2+1
    com = ":CALC1:DATA:SDAT?\n"
    N = 50
    for k in range(N):
        B = vna.read(com)
        S =np.frombuffer(B[0:201*16],dtype='>f8')
        S21= S[u]+1j*S[v]
        try:
            res = np.vstack((res,S21.T))
        except:
            res = S21.T

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-8-1258876c0fc8> in <module>()
          5 com1 = "FORM:DATA REAL"
          6 com2 = "TRIG:SING"
    ----> 7 vna.write(com1)
          8 vna.write(com2)
          9 u = np.arange(0,201)*2


    NameError: name 'vna' is not defined


.. code:: python

    from scipy.fftpack import fft,ifft,fftshift
.. code:: python

    fres=ifft(res,axis=1)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-bc7143b45761> in <module>()
    ----> 1 fres=ifft(res,axis=1)
    

    NameError: name 'res' is not defined


.. code:: python

    np.shape(res)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-e54f05e71f87> in <module>()
    ----> 1 np.shape(res)
    

    NameError: name 'res' is not defined


.. code:: python

    R=np.mean(res,axis=0)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-d44db15df4a8> in <module>()
    ----> 1 R=np.mean(res,axis=0)
    

    NameError: name 'res' is not defined


.. code:: python

    plt.plot(abs(R))

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-3473193bd0a3> in <module>()
    ----> 1 plt.plot(abs(R))
    

    NameError: name 'R' is not defined


.. code:: python

    r = ifft(R)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-7a1e13df69b5> in <module>()
    ----> 1 r = ifft(R)
    

    NameError: name 'R' is not defined


.. code:: python

    t = np.linspace(0,201/(2.2-1.8),201)
.. code:: python

    plt.plot(t*0.3,fftshift(abs(r)))

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-9f20ce80c354> in <module>()
    ----> 1 plt.plot(t*0.3,fftshift(abs(r)))
    

    NameError: name 'r' is not defined


.. code:: python

    plt.figure(figsize=(20,10))
    plt.imshow(abs(res),extent=(1.8,2.2,0,.1),origin='lower')

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-39adaae0b459> in <module>()
          1 plt.figure(figsize=(20,10))
    ----> 2 plt.imshow(abs(res),extent=(1.8,2.2,0,.1),origin='lower')
    

    NameError: name 'res' is not defined



.. parsed-literal::

    <matplotlib.figure.Figure at 0x2adc7925f090>


.. code:: python

    plt.plot(fftshift(abs(fres[0,:])))

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-18-193234907ed0> in <module>()
    ----> 1 plt.plot(fftshift(abs(fres[0,:])))
    

    NameError: name 'fres' is not defined


.. code:: python

    3238-3216



.. parsed-literal::

    22



.. code:: python

    len(S[22:])

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-6eddf478751c> in <module>()
    ----> 1 len(S[22:])
    

    NameError: name 'S' is not defined


.. code:: python

    S21=np.frombuffer(S[0:201*16],dtype='>f8')

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-21-9d3be1c9967f> in <module>()
    ----> 1 S21=np.frombuffer(S[0:201*16],dtype='>f8')
    

    NameError: name 'S' is not defined


.. code:: python

    len(S21)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-22-b6b7beee8080> in <module>()
    ----> 1 len(S21)
    

    NameError: name 'S21' is not defined


.. code:: python

    u = np.arange(0,201)*2
    v = np.arange(0,201)*2+1
.. code:: python

    cS21= S21[u]+1j*S21[v]

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-24-89dbbf0c84ef> in <module>()
    ----> 1 cS21= S21[u]+1j*S21[v]
    

    NameError: name 'S21' is not defined


.. code:: python

    plt.plot(freq,20*np.log10(abs(cS21)))

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-25-84db27f811f6> in <module>()
    ----> 1 plt.plot(freq,20*np.log10(abs(cS21)))
    

    NameError: name 'freq' is not defined


.. code:: python

    plt.plot(freq,20*np.angle(cS21))

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-9f5a7ede795d> in <module>()
    ----> 1 plt.plot(freq,20*np.angle(cS21))
    

    NameError: name 'freq' is not defined


.. code:: python

    import numpy as np
    f = np.frombuffer(tab,dtype='>i2')

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-27-fcd5bece7f74> in <module>()
          1 import numpy as np
    ----> 2 f = np.frombuffer(tab,dtype='>i2')
    

    NameError: name 'tab' is not defined


.. code:: python

    201*8



.. parsed-literal::

    1608



.. code:: python

    fr=vna.getfreq()

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-29-51e6140ab7c6> in <module>()
    ----> 1 fr=vna.getfreq()
    

    NameError: name 'vna' is not defined


.. code:: python

    S=vna.getnpoints()

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-30-3d7778067036> in <module>()
    ----> 1 S=vna.getnpoints()
    

    NameError: name 'vna' is not defined


.. code:: python

    vna.s.send(":SENS1:SWE:POIN?\n")

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-5353e08d0f49> in <module>()
    ----> 1 vna.s.send(":SENS1:SWE:POIN?\n")
    

    NameError: name 'vna' is not defined


.. code:: python

    vna.s.recv(56)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-32-8f2fe545b62d> in <module>()
    ----> 1 vna.s.recv(56)
    

    NameError: name 'vna' is not defined


.. code:: python

    S=vna.getdata()

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-33-6ef375d59131> in <module>()
    ----> 1 S=vna.getdata()
    

    NameError: name 'vna' is not defined


.. code:: python

    import pylayers.measures.switch.ni_usb_6501 as sw
    switch = sw.get_adapter()
    if not switch:
        raise Exception("No device found")
    switch.set_io_mode(0b11111111, 0b11111111, 0b00000000)

::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-34-4ab981a04027> in <module>()
          1 import pylayers.measures.switch.ni_usb_6501 as sw
    ----> 2 switch = sw.get_adapter()
          3 if not switch:
          4     raise Exception("No device found")
          5 switch.set_io_mode(0b11111111, 0b11111111, 0b00000000)


    /home/uguen/Documents/rch/devel/pylayers/pylayers/measures/switch/ni_usb_6501.py in get_adapter(**kwargs)
         39     device = usb.core.find(idVendor=ID_VENDOR, idProduct=ID_PRODUCT, **kwargs)
         40     if not device:
    ---> 41         raise ValueError('Device not found')
         42 
         43     return NiUsb6501(device)


    ValueError: Device not found


.. code:: python

    switch.write_port(0,0b00000101)

::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-35-a356476b0949> in <module>()
    ----> 1 switch.write_port(0,0b00000101)
    

    NameError: name 'switch' is not defined


.. code:: python

    eval('0b100')



.. parsed-literal::

    4



