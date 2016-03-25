
.. code:: python

    from pylayers.gis.ezone import *
    %matplotlib inline


.. parsed-literal::

    /home/uguen/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:872: UserWarning: axes.color_cycle is deprecated and replaced with axes.prop_cycle; please use the latter.
      warnings.warn(self.msg_depr % (key, alt_key))


An Ezone is an objet which gathers vector and raster information from a
1 degree by 1 degree tile of earth

.. code:: python

    prefix=enctile(-1.5,10.5)
    print prefix


.. parsed-literal::

    N10W002


.. code:: python

    prefix




.. parsed-literal::

    'N10W002'



.. code:: python

    dectile(prefix=prefix)




.. parsed-literal::

    (-2, -1, 10, 11)



.. code:: python

    int('08')




.. parsed-literal::

    8



.. code:: python

    E=Ezone(prefix)

.. code:: python

    E.prefix




.. parsed-literal::

    'N10W002'



An ``Ezone`` can be obtained from a point (longitude,Latitude)

.. code:: python

    r=E.getdem()


.. parsed-literal::

    Download srtm file
    SRTMDownloader - server= dds.cr.usgs.gov, directory=srtm/version2_1/SRTM3.
    N10W002.hgt.zip
    no aster file for this point


.. code:: python

    E.saveh5()

.. code:: python

    f,a = E.show(source='srtm',clim=[0,500])


::


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-10-38421fc8f6f7> in <module>()
    ----> 1 f,a = E.show(source='srtm',clim=[0,500])
    

    ValueError: too many values to unpack



.. image:: Downloading_files/Downloading_11_1.png


.. code:: python

    from IPython.core.display import HTML
