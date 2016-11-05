.. raw:: html

    <style>
        @font-face {
            font-family: "Computer Modern";
            src: url('http://mirrors.ctan.org/fonts/cm-unicode/fonts/otf/cmunss.otf');
        }
        div.cell{
            width:800px;
            margin-left:16% !important;
            margin-right:auto;
        }
        h1 {
            font-family: Helvetica, serif;
        }
        h4{
            margin-top:12px;
            margin-bottom: 3px;
           }
        div.text_cell_render{
            font-family: Computer Modern, "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;
            line-height: 145%;
            font-size: 130%;
            width:800px;
            margin-left:auto;
            margin-right:auto;
        }
        .CodeMirror{
                font-family: "Source Code Pro", source-code-pro,Consolas, monospace;
        }
        .prompt{
            display: None;
        }
        .text_cell_render h5 {
            font-weight: 300;
            font-size: 22pt;
            color: #4057A1;
            font-style: italic;
            margin-bottom: .5em;
            margin-top: 0.5em;
            display: block;
        }
        
        .warning{
            color: rgb( 240, 20, 20 )
            }  
    </style>
    <script>
        MathJax.Hub.Config({
                            TeX: {
                               extensions: ["AMSmath.js"]
                               },
                    tex2jax: {
                        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                        displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
                    },
                    displayAlign: 'center', // Change this to 'center' to center equations.
                    "HTML-CSS": {
                        styles: {'.MathJax_Display': {"margin": 4}}
                    }
            });
    </script>

 
.. raw:: html

   <div class="no-display">


.. sectnum:: 
   :depth: 6

.. contents::
   :depth: 4

.. toctree::
   maxdepth: 4

Overview
########

Pylayers is a site-specific radio channel simulator.
It is organized in different python modules. 

The source code is distributed in the following directories

+ gis
    Handle geographical information system
+ antprop
    Antenna and Propagation related modules
+ measures
    Measurement related tools 
+ simul 
    High level simulation tools
+ mobility 
    Human and vehicular mobility modules 
+ signal
    Signal and PHY tools
+ location 
    Location and positioning tools
+ util 
    Utility functions


The basic usage is first to build a description of the radio propagation 
scene. This means : 

1. Describing a propagation environment 
2. Setting a transmitter and a receiver and a given standard. 
3. Producing different kind of outputs for further upper layer analysis.   



Radio Propagation Simulation 
############################

Environment Description 
************************ 

Indoor and Outdoor Layout
=========================

.. toctree::
  :maxdepth: 2

  1-GIS/Layout.rst 

  1-GIS/Multisubsegments.rst

GIS and DEM
===========

.. toctree::
  :maxdepth: 2

  1-GIS/Ezone.rst
  1-GIS/Coverage.rst

Handling Material Properties of Layout
======================================

.. toctree::
  :maxdepth: 2
  
  2-AP/SlabsMaterials.rst

Description of Antennas
***********************

.. toctree::
  :maxdepth: 2

  2-AP/Antenna.rst
  2-AP/AntennaSSH.rst
  2-AP/AntennaVSH.rst

Multiwall Motley-Keenan Simulation
**********************************

.. toctree::
  :maxdepth: 2

  2-AP/Coverage.rst
  2-AP/Coverage2.rst
  2-AP/MultiWall.rst
  2-AP/CoverageMetis.rst

Ray Tracing Tool
****************

.. toctree::
  :maxdepth: 2

  2-AP/Signatures.rst
  2-AP/Channel.rst
  2-AP/CIR.rst
  5-SIM/LinkSimulation.rst
  
  

Handling Agent Mobility 
#######################

.. toctree::
  :maxdepth: 2

  5-SIM/SimulNetConfig.rst
  4-MOB/Mobility.rst
  4-MOB/Body.rst

Wireless Body Area Network Related Classes
########################################## 
  
.. toctree::
  :maxdepth: 2

  5-SIM/Corser.rst

Some Simulation Examples
########################

.. toctree::
  :maxdepth: 2

  2-AP/MetisRayTracing60GHzforTC1.rst
  5-SIM/DLR-WHERE2.rst
  5-SIM/PTIN.rst
  5-SIM/WHERE1-M1.rst
  5-SIM/Where1M1.rst
  5-SIM/AggregatedCIR.rst
  5-SIM/

Algorithms for Localization 
###########################

.. toctree::
  :maxdepth: 2

  7-APP/LOC-algebraic.rst
  7-APP/LOC-rgpa.rst
  7-APP/LOC-localisation.rst


Measurements Tools 
############################

.. toctree::
  :maxdepth: 2

  A-MES/VNA.rst
  A-MES/scanner.rst

PyLayers Tools 
############################

.. toctree::
  :maxdepth: 2

  3-PHY/Bsignal.rst
  3-PHY/Noise.rst
  8-MISC/Cone.rst
  8-MISC/Geomutil.rst


.. raw:: html

  <\div>

