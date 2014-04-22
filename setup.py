#!/usr/bin/env python
from setuptools import setup, find_packages

version = __import__('background_tasker').get_version()

setup(
    name='django-background-tasker',
    version=version,
    url='https://github.com/leonsmith/django-background-tasker/',
    author='Leon Smith',
    author_email='_@leonmarksmith.com',
    description='A simple django extension for running background tasks using zeromq',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'pyzmq',
    ]
)
