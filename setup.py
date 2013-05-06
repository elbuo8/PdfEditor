#!/usr/bin/env python

from setuptools import setup

setup(
    name='PdfEditor',
    version='0.0.3',
    description='Modify previously created PDF\'s',
    author='Yamil Asusta (elbuo8)',
    author_email='yamil.asusta@upr.edu',
    license='MIT',
    url='https://github.com/elbuo8/PdfEditor',
    install_requires=[
        'reportlab'
    ],
    dependency_links=[
        'http://github.com/knowah/PyPDF2/tarball/master'
    ],
)
