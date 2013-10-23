from __future__ import division, absolute_import, print_function

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('gufunc_sampler', parent_package, top_path)
    config.add_extension('_gs_kernels', ['_gs_kernels.c.src'])

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)