# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import find_packages, setup

install_requires = [
    'Flask==0.10.1',
    'Flask-Mail==0.9.0',
    'Flask-WTF==0.9.4',
    'Jinja2==2.7.2',
    'MarkupSafe==0.18',
    'WTForms==1.0.5',
    'Werkzeug==0.9.4',
    'blinker==1.3',
    'gunicorn==18.0',
    'itsdangerous==0.23',
    'wsgiref==0.1.2',
]

setup(
    name="d5s",
    version="0.0.1",
    install_requires=install_requires
)
