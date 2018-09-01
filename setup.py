import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    description = f.read()

setup(
    name='gitscan',
    version="1.0",
    author="Marius Kleiner",
    author_email="kleiner@gmail.com",
    url='https://github.com/infogrind/gitscan',
    description='Shell script to display elementary info about git repos',
    long_description=description,
    packages=find_packages(),
    install_requires = [
        "gitpython",
        ],
    entry_points={
        "console_scripts": ["gitscan = gitscan:main"]
        },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English'
        ]
    )
