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

`PyLayers` is a site-specific radio propagation channel simulator, 
curently developed at IETR laboratory in Rennes. 
It aims at providing a very flexible tool to investigate 
radio propagation channel for education and research in the field of
communications and localization. The current work is mostly focused 
on investigating 5G cellular concepts. 

If you find some interest in this tool and decide to start to use it. 
You are welcome to contribute your feedback, suggestions and even 
improvements back to the project. 
The best place to do it first it in the issues
page of the project (https://github.com/pylayers/pylayers/issues)


Basic Usage
###########

The basic usage is first to build a description of the radio propagation 
scene. This means : 

1. Describing a propagation environment 
2. Setting a Link in specifying a transmitter and a receiver position with
   ther antennas type and orientation
3. Producing channel outputs 


Environment Description 
#######################

.. toctree::
  :maxdepth: 2

  1-GIS/Layout.rst 
  1-GIS/Multisubsegments.rst
  1-GIS/Ezone.rst
  1-GIS/Coverage.rst

Materials and Slabs
###################

.. toctree::
  :maxdepth: 2
  
  2-AP/SlabsMaterials.rst

Description of Antennas
#######################

.. toctree::
  :maxdepth: 2

  2-AP/Antenna.rst
  2-AP/AntennaSSH.rst
  2-AP/AntennaVSH.rst

Coverage Simulation
###################

.. toctree::
  :maxdepth: 2

  2-AP/Coverage.rst
  2-AP/Coverage2.rst
  2-AP/MultiWall.rst
  2-AP/CoverageMetis.rst

Ray Tracing Simulation 
######################

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
  5-SIM/Corser.rst

Other Simulation Examples
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

Localization Algorithms
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
