###########
AequilibraE
###########


.. image:: https://github.com/AequilibraE/aequilibrae/workflows/Documentation/badge.svg
    :target: https://github.com/AequilibraE/aequilibrae/workflows/Documentation/badge.svg
    :alt: Documentation Status


.. image:: https://github.com/AequilibraE/aequilibrae/workflows/Linting/badge.svg
    :target: https://github.com/AequilibraE/aequilibrae/workflows/Linting/badge.svg
    :alt: Linting

.. image:: https://github.com/AequilibraE/aequilibrae/workflows/Tests%20on%20Windows/badge.svg
    :target: https://github.com/AequilibraE/aequilibrae/workflows/Tests%20on%20Windows/badge.svg
    :alt: Windows Unit tests

.. image:: https://codecov.io/gh/AequilibraE/aequilibrae/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/AequilibraE/aequilibrae

.. image:: https://github.com/AequilibraE/aequilibrae/workflows/Upload%20MacOS%20Python%20Package/badge.svg
    :target: https://github.com/AequilibraE/aequilibrae/workflows/Upload%20MacOS%20Python%20Package/badge.svg
    :alt: PyPi - Mac OS

.. image:: https://github.com/AequilibraE/aequilibrae/workflows/Upload%20Windows%20Python%20Package/badge.svg
    :target: https://github.com/AequilibraE/aequilibrae/workflows/Upload%20Windows%20Python%20Package/badge.svg
    :alt: PyPi - Windows

.. image:: https://github.com/AequilibraE/aequilibrae/workflows/Upload%20Linux%20Python%20Package/badge.svg
    :target: https://github.com/AequilibraE/aequilibrae/workflows/Upload%20Linux%20Python%20Package/badge.svg
    :alt: PyPi - Linux

AequilibraE is the first comprehensive Python package for transportation modeling, and it aims to provide all the
resources not available from other open-source packages in the Python (NumPy, really) ecosystem.

Comprehensive documentation
###########################

`AequilibraE documentation built with Sphinx <http://www.aequilibrae.com>`_

What is available
#################

* Importing networks from OSM
* Synthetic gravity/IPF
* Traffic assignment (All-or Nothing, MSA, Frank-Wolfe, Conjugate Frank-Wolfe & Biconjugate-FrankWolfe)
* Network Skimming & node-to-node path computation
* Fast Matrix format based on NumPy
* GTFS Import

What is available only in QGIS
******************************

Some common resources for transportation modelling are inherently visual, and therefore they make more sense if
available within a GIS platform. For that reason, many resources are available only from AequilibraE's `QGIS plugin
<http://plugins.qgis.org/plugins/AequilibraE/>`_,
which uses AequilibraE as its computational workhorse and also provides GUIs for most of AequilibraE's tools. Said tool
is developed independently, although in parallel, and more details can be found in its `GitHub repository
<https://github.com/AequilibraE/AequilibraE-GUI>`_.


Development roadmap
********************

Available in the documentation


What is not planned to be available any time soon
*************************************************

As AequilibraE's focus is to provide resources that are not yet available in the open source world, particularly the
Python ecosystem, some important tools for transportation model won't be part of AequilibraE any time soon. Examples
of this are:

    * Discrete choice models - `BIOEGEME <http://biogeme.epfl.ch>`_ , `LARCH <http://larch.newman.me>`_

    * Activity-Based models - `ActivitySim <http://www.activitysim.org/>`_

History
#######

Before there was AequilibraE, there was a need for something like AequilibraE out there.

The very early days
*******************
It all started when I was a student at `UCI-ITS <www.its.uci.edu>`_ and needed low level access to outputs of standard
algorithms used in transportation modelling (e.g. path files from traffic assignment) and had that denied by the maker
of the commercial software he normally used. There, the `first scratch of a traffic assignment procedure
<www.xl-optim.com/python-traffic-assignment>`_ was born.
After that, there were a couple of scripts developed to implement synthetic gravity models (calibration and application)
that were develop for a government think-tank in Brazil `IPEA <www.ipea.gov.br>`_.
Around the same time, another student needed a piece of code that transformed a GIS link layer into a proper graph,
where each link would become the connection between two nodes.
So there were three fundamental pieces that would come to be part of AequilibraE.

The first take on a release software
************************************
Having all those algorithms at hand, it made sense combining them into something more people could use, and by them it
seemed that QGIS was the way to go, so I developed the `very first version of AequilibraE
<http://www.xl-optim.com/introducing_aequilibrae>`_.

It was buggy as hell and there was very little, if any, software engineering built into it, but it put Aequilibrae on
the map.

The first reasonable version
****************************
The first important thing I noticed after releasing AequilibraE was that the code was written in procedural style, even
though it would make a lot more sense doing it in a Object-Oriented fashion, which let me down the path of creating the
objects (graph, assignment results, matrix) that the software still relies on and were the foundation blocks of the
proper API that is in the making. That `version was release over 4 years ago
<http://www.xl-optim.com/new-version-of-aequilibrae/>`_.

Evolving into proper software
*****************************

A few distinct improvements deserve to be highlighted.

* The separation of the GUI and the Python library in `two repositories <http://www.xl-optim.com/separating-the-women-from-the-girls/>`_
* Introduction of Unit Tests and automatic testing using `Travis <https://travis-ci.org/AequilibraE/aequilibrae>`_
* Welcome of new collaborators: Jamie Cook, Andrew O'Brien, Yu-Chu Huang & Jan Zill
* Introduction of style-checking with Flake8 and Black
* Development of proper documentation and a recommended development virtual environment

QGIS Plugin
###########

The QGIS plugin is developed on a separate repository: `QGIS GUI <https://github.com/AequilibraE/AequilibraE-GUI>`_ 
That is where everything started.
