#!/usr/bin/env python

from setuptools import setup, find_packages

__AUTHOR__ = 'Martin Renou'

setup(
    name='json-lsp',
    version='0.1.0',
    description='JSON language server Python wrapper.',
    author=__AUTHOR__,
    maintainer=__AUTHOR__,
    url='https://github.com/martinRenou/json-lsp',
    license='BSD 3-Clause',
    keywords='python json language-server',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
    entry_points={
        'jupyter_lsp_spec_v1': [
            'json-language-server = json_lsp.main:load'
        ],
        'console_scripts': ['json-lsp = json_lsp.main:main'],
    },
    platforms=['any'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
