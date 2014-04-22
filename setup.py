#!/usr/bin/env python
from setuptools import setup, find_packages

version = __import__('background_tasker').get_version()

setup(
    name='django-background-tasker',
    version=version,
    url='https://github.com/leonsmith/django-background-tasker/',
    download_url='https://github.com/leonsmith/django-background-tasker/archive/%s.tar.gz' % version,
    author='Leon Smith',
    author_email='_@leonmarksmith.com',
    description='A simple django extension for running background tasks using zeromq',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'pyzmq',
    ]
)
