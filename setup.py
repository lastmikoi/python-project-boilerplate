# --------------------------------License Notice----------------------------------
# Python Project Boilerplate - A boilerplate project for python packages
#
# Written in 2018 by Mickaël 'lastmikoi' FALCK <lastmikoi@lastmikoi.net>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
# --------------------------------License Notice----------------------------------

"""Setuptools-backed setup module."""

import codecs
import os

import setuptools


if __name__ == '__main__':
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

    # Use README.rst as source for setuptools.setup's long_description param
    with codecs.open(os.path.join(ROOT_DIR, 'README.rst'),
                     encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()

    setuptools.setup(
        # Distutils parameters
        name='project_name',
        description='Placeholder description',
        long_description=LONG_DESCRIPTION,
        author="Mickaël 'lastmikoi' FALCK",
        author_email='lastmikoi@lastmikoi.net',
        url='https://github.com/lastmikoi/python-project-boilerplate/',
        packages=setuptools.find_packages(exclude=['tests']),
        classifiers=[
            'Programming Language :: Python :: 3',
        ],
        license='CC0 1.0 Universal',
        keywords='python project boilerplate skeleton template',
        # Setuptools parameters
        include_package_data=True,
        install_requires=[
        ],
        extras_require={
            'dev': [
                'ipython>=7.2.0,<8',
            ],
            'test': [
                'tox>=3.5.3,<4',
                'pytest>=4.0.1,<5',
                'pytest-mock>=1.10.0,<2',
            ],
        },
        python_requires='>=3.6,<4',
        setup_requires=['setuptools_scm'],
        # setuptools_scm parameters
        use_scm_version=True,
    )
