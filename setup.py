# coding: utf-8

"""
    REST API of the Brazilian Federal Government Open Data Portal

    Api ...

    Contact: adrianolaselva@gmail.com
    Repository: https://github.com/adrianolaselva/dados-gov-python-sdk.git
"""
import os

from setuptools import setup, find_packages  # noqa: H301

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NAME = "dados-gov-sdk"
VERSION = "1.0.1"

with open(f'{ROOT_DIR}/README.md') as description:
    long_description = description.read()

setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    description="REST API of the Brazilian Federal Government Open Data Portal",
    author='Adriano M. La Selva',
    author_email="adrianolaselva@gmail.com",
    url="https://github.com/adrianolaselva/dados-gov-python-sdk.git",
    keywords=','.join([
        "python", "dados", "data", "api", "apis", "recursos", "resources", "swagger", "client", "sdk", "pygov",
        "swagger", "portal", "gov", "governo", "government", "federal", "brasil", "brazil",
        "api", "swagger", "abertos", "open", "open-data", "transparencia", "transparency",
        "utilitario", "utility", "colaborativo", "collaborative", "modulo", "module", "pacote", "package"
    ]),
    install_requires=[
        'certifi>=14.05.14',
        'six>=1.10',
        'setuptools>=21.0.0',
        'urllib3>=1.15.1',
        'requests>=2.31.0',
    ],
    packages=find_packages('.'),
    package_dir={'': '.'},
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License"
    ],
)
