# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import find_packages, setup

install_requires = [
    'Flask==0.10.1',
    'Jinja2==2.7.2',
    'gunicorn==18.0',
]

setup(
    name="d5s",
    version="0.0.1",
    install_requires=install_requires
)
