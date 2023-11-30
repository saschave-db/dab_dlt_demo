"""
Setup script for dab_dlt_demo.

This script packages and distributes the associated wheel file(s).
Source code is in ./src/. Run 'python setup.py sdist bdist_wheel' to build.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import dab_dlt_demo

setup(
    name="dab_dlt_demo",
    version=dab_dlt_demo.__version__,
    url="https://databricks.com",
    author="sascha.vetter@databricks.com",
    description="my test wheel",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={"entry_points": "main=dab_dlt_demo.main:main"},
    install_requires=["setuptools"],
)
