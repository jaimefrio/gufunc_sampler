"""Several examples of C coded Generalized Universal FUNCtions.
"""
from __future__ import division, absolute_import, print_function

DOCLINES = __doc__.split('\n')

import os
import sys

NAME = 'gufunc_sampler'
AUTHOR = 'Jaime Fernandez'
AUTHOR_EMAIL = 'jaime.frio@gmail.com'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])
PLATFORMS = ["Windows", "Linux", "Mac OS-X"]
MAJOR = 0
MINOR = 1
MICRO = 0
VERSION = '{0}.{1}.{2}'.format(MAJOR, MINOR, MICRO)

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    
    config = Configuration(None, parent_package, top_path)
    config.add_subpackage('gufunc_sampler', None)

    return config

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    from numpy.distutils.core import setup
    try:
        setup(name=NAME,
              maintainer=MAINTAINER,
              maintainer_email=MAINTAINER_EMAIL,
              description=DESCRIPTION,
              long_description=LONG_DESCRIPTION,
              author=AUTHOR,
              author_email=AUTHOR_EMAIL,
              platforms=PLATFORMS,
              version=VERSION,
              configuration=configuration)
    finally:
        del sys.path[0]
        os.chdir(old_path)

if __name__ == "__main__":
    setup_package()