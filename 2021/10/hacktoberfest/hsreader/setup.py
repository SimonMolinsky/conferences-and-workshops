import re
from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

# Project description
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

# obtain version string from __init__.py
with open(path.join(here, 'hsreader/__init__.py'), 'r') as f:
    init_py = f.read()
version = re.search("__version__ = '(.*)'", init_py).groups()[0]

setup(
    name='hsreader',
    version=version,
    description='Read and download HackerSpace Trójmiasto webpage',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/szymon-datalions/hsreader',
    download_url='https://github.com/szymon-datalions/hsreader/archive/v0.1.0.tar.gz',
    author='Szymon Moliński',
    author_email='simon@ml-gis-service.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3'
    ],
    keywords=['Tutorials', 'Hacktoberfest 2021'],
    packages=find_packages(exclude=['docs']),
    install_requires=[
        'requests'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/szymon-datalions/hsreader/issues',
        'HackerSpace Trójmiasto Webpage': 'https://hs3.pl/',
        'HackerSpace Trójmiasto Discord': 'https://discord.gg/GSTgYzU',
    },
    entry_points={
        "console_scripts": [
            "hsreader=hsreader.__main__:main",
        ]
    },
)
