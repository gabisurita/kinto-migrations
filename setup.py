#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

with codecs.open(os.path.join(here, 'CHANGELOG.rst'), encoding='utf-8') as f:
    history = f.read()

requirements = [
    'kinto_http',
    'pyaml',
]

test_requirements = [
    'flake8',
    'kinto',
    'pytest',
    'pytest-cache',
    'pytest-cover',
    'pytest-sugar',
    'pytest-xdist',
]

entry_points = {
    'console_scripts': [
        'kinto-migrate = kinto_migrations.__main__:main'
    ],
}

setup(
    name='kinto-migrations',
    version='0.1.0',
    description="Run Kinto HTTP migrations.",
    long_description=readme + '\n\n' + history,
    author="Gabriela Suria",
    author_email='gabsurita@gmail.com',
    url='https://github.com/gabisurita/kinto-migrations',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="Apache License (2.0)",
    zip_safe=False,
    keywords='kinto',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points=entry_points,
)
