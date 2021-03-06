#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages
from mt.skimage.version import VERSION

setup(
    name='skimagemt',
    version=VERSION,
    description="Minh-Tri Pham's extra modules for scikit-image",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=['mt.*']),
    #package_data={
    #    'skimagemt': ['*.pyx'],
    #},
    #include_package_data=True,
    #zip_safe=False,
    install_requires=[
        'scikit-image>=0.15.0',
        'geomt>=0.2.0',
    ],
)
