# coding: utf-8

"""
    REST API of the Brazilian Federal Government Open Data Portal

    Api ...

    Contact: adrianolaselva@gmail.com
    Repository: https://github.com/adrianolaselva/dados-gov-python-sdk.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "dados-gov-sdk"
VERSION = "1.0.0"

with open('README.md') as description:
    long_description = description.read()

with open('requirements.txt') as requirements:
    install_requires = requirements.read().splitlines()

setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    description="REST API of the Brazilian Federal Government Open Data Portal",
    author_email="adrianolaselva@gmail.com",
    url="https://github.com/adrianolaselva/dados-gov-python-sdk.git",
    keywords=[
        "python", "dados", "data", "api", "apis", "recursos", "resources", "swagger", "client", "sdk", "pygov",
        "swagger", "portal", "gov", "governo", "government", "federal", "brasil", "brazil",
        "api", "swagger", "abertos", "open", "open-data", "transparencia", "transparency",
        "utilitario", "utility", "colaborativo", "collaborative", "modulo", "module", "pacote", "package"
    ],
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
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
