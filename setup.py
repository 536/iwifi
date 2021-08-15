# !/usr/bin/env python3
# coding: utf-8
from setuptools import setup

from iwifi import *

setup(
    name=NAME,
    version=VERSION,
    long_description=open('README.md', mode='r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    url=URL,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=[
        'click',
        'qrcode',
    ],
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points=ENTRY_POINTS,
)
