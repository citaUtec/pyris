#!/usr/bin/env python

# .:==============:.
# .:    PyRIS     :.
# .: -------------:.
# .: Setup Script :.
# .:==============:.

# Python - RIvers by Satellites

from distutils.core import setup

description = 'PyRIS :: Python - RIvers by Satellites'
long_description = '\n'.join((
    description,
    '''

    See Publication:
    
    --------------------------------------------------------------------------------------------------
    Monegaglia et al. 2017
    "Automating extraction of meandering river morphodynamics from multitemporal remotely sensed data"
    (Remote Sensing of Environment)
    --------------------------------------------------------------------------------------------------

    Requires: NumPy, SciPy, MatPlotLib, GDAL
    
    '''
))

setup(
    name = 'pyris',
    version = '1.0',
    author = 'Federico Monegaglia',
    author_email = 'f.monegaglia@gmail.com',
    maintainer = 'Federico Monegaglia',
    maintainer_email = 'f.monegaglia@gmail.com',
    description = description,
    long_description = long_description,
    url = 'https://bitbucket.org/fmonegaglia/pyris',
    install_requires = [ 'numpy', 'matplotlib', 'scikit-image', 'gdal' ],
    packages = [ 'pyris', 'pyris.config', 'pyris.misc', 'pyris.raster', 'pyris.vector' ],
    py_modules = [ 'misc', 'raster', 'vector' ],
    scripts = ['pyris/bin/pyris'],
    
)
    