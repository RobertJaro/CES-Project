from setuptools import find_packages, setup

setup(
    name='ces',
    version='0.1',
    description='Computergestuetzte Experimente und Signalauswertung VU',
    author='Robert Jarolim; Michael Mueller; Raphael Wagner',
    packages=find_packages(),
    provides=find_packages(),
    python_requires='>=3',
    entry_points={
        'gui_scripts': ['signalauswertung=ces.main:main'],
    }
)