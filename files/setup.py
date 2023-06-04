#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='M-Phisher2.O',
    version=version,
    description='A python phishing script for login phishing, image phishing video phishing an many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='SHAKTI BIPLAB',
    author_email='shaktibiplab25@gmail.com',
    license="MIT",
    url='https://github.com/LUCIFERGREYHAT1/m-phisher2.O/',
    scripts=['m-phisher2.O'],
    install_requires=["requests", "bs4", "rich"]
)
