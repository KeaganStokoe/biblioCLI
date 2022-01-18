from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='bibliocli',
    version=1.0,
    py_modules=['bibliocli'],
    install_requires=[
        'Click', 'requests', 'rich'
    ],
    entry_points={
        'console_scripts': 'bib=bibliocli:bibliocli'
    }
)