#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@ Author: Innary
@ Date: 2022-11-11 12:02:08
@ LastEditors: Innary
@ LastEditTime: 2022-11-11 12:35:51
'''
from setuptools import setup, find_packages
requirements = [
    'pywin32',
    'pyperclip'
    
]


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

setup(
    name='PdfCopy',
    version='0.0.1',
    author = 'Innary', 
    author_email = 'wyc1015128645@gmail.com',
    description='a example for dpf copy-paste',
    long_description=readme(), 
    long_description_content_type='text/markdown',
    url='https://github.com/Innary/pdfcopy',
    install_requires=requirements,
    packages=find_packages(),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'pcp = pdfcopy.main:main',
        ],
    },
    
)