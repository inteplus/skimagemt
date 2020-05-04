#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages
from mt.skimage.version import version

setup(
    name='skimagemt',
    version=version,
    description="Minh-Tri Pham's extra modules for scikit-image",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=['ml.*']),
    #package_data={
    #    'skimagemt': ['*.pyx'],
    #},
    #include_package_data=True,
    #zip_safe=False,
    install_requires=[
        'scikit-image>=0.14.0',
        'geomt>=0.1.1',
    ],
)
