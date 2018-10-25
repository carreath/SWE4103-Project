from distutils.core import setup
from setuptools import find_packages

setup(
    # Application name:
    name="api",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Caleb Reath",
    author_email="carreath@icloud.com",

    # Packages
    packages=find_packages(exclude=['.idea', 'contrib', 'docs', 'tests']),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://142.93.244.110:5000/api",

    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)