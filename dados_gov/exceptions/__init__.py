# coding: utf-8

# flake8: noqa

"""
    REST API of the Brazilian Federal Government Open Data Portal

    Api Exceptions

    Contact: adrianolaselva@gmail.com
    Repository: https://github.com/adrianolaselva/dados-gov-python-sdk.git
"""

from __future__ import absolute_import

from .create_resource_exception import CreateResourcesException
from .edit_resource_exception import EditResourcesException
from .list_resources_exception import ListResourcesException
from .load_resource_exception import LoadResourcesException
from .update_resource_exception import UpdateResourcesException
from .http_request_exception import HttpRequestException
