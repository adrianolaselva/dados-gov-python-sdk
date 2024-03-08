# REST API of the Brazilian Federal Government Open Data Portal

[![Python package](https://github.com/adrianolaselva/dados-gov-python-sdk/actions/workflows/python-package.yml/badge.svg?branch=master)](https://github.com/adrianolaselva/dados-gov-python-sdk/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/github/adrianolaselva/dados-gov-python-sdk/graph/badge.svg?token=1JFRLT3ZLM)](https://codecov.io/github/adrianolaselva/dados-gov-python-sdk)
[![PyPI Latest Release](https://img.shields.io/pypi/v/dados-gov-sdk.svg)](https://pypi.org/project/dados-gov-sdk/) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/dados-gov-sdk)


dados.gov.br now manages the technological solution to improve the governance of federal investments in infrastructure, 
through monitoring and monitoring the execution of investments in Federal Government infrastructure projects. 
Optionally, other powers of the Union, States, Federal District and Municipalities may register investments in 
infrastructure with their own resources through a formal manifestation of their adhesion.

dados.gov.br, in addition to complying with various rulings from the Federal Court of Auditors, aims to meet society's 
demand for clear, updated and centralized information. Thus, it positively impacts the effectiveness of the execution 
of public policies and decision-making by managers, in addition to enabling social control through transparency.

The platform gathers information about the geolocation of investments and allows it to be integrated with other 
monitoring, control and inspection systems, thus optimizing citizens' access to information and strengthening 
transparency regarding the rational use of public resources.

For more information, visit: [https://www.gov.br/transferegov/pt-br/obrasgov/sobre](https://www.gov.br/transferegov/pt-br/obrasgov/sobre)

## Additional information

Python library created with the aim of contributing to the community, providing an alternative to facilitate the use of 
the Federal Government's APIs, thus making the column available for contributions aimed at maintaining and evolving this 
simple code base.

And last but not least, **please** use the information wisely and without political bias.

## How to install

To install the library use Python's `pip` package manager.

Below are some examples of how to install.

```shell
pip install dados-gov-sdk
```
> Example of installation from the latest available version

```shell
pip install dados-gov-sdk@1.1.0
```
> Installation example stating a specific version

## How to Get Token

Access the Brazilian Federal Government Portal with your access credentials using your CPF (Individual Person Registry). 
Access through the link [https://dados.gov.br/](https://dados.gov.br/).

Once logged in, generate an access token and that's it, you will already have the information at hand to access the 
APIs, have fun 🥳

## How To Use

To use, first have the access key on hand, once that is done, there are some ways to configure it for use, either 
directly through the `ApiClient(...)` instance or through environment variables.

Configuring through environment variables, simply set them according to the names of the [environment variable](#environment-variables) session, 
once this is done, simply instance the resources and use them.

Below are some examples.

```python
from dados_gov import Settings, ApiClient

settings = Settings(api_key='<YOUR_API_KEY>')
api_client = ApiClient(settings)
```
> This example shows a way to initialize an instance of ApiClient, note that in the Settings entity it is possible to 
  pass personalized settings, if this is not passed the default information will be accepted, and if they have been 
  defined through environment variables, they will replace the default settings

```python
import datetime

from dados_gov import Settings, ApiClient
from dados_gov.models import DatasetModel
from dados_gov.models.dataset_model import TagModel, ResourceModel, ThemeModel
from dados_gov.resources.dataset_api import DatasetApi

dataset = DatasetModel(id="e668f214-e24a-4eda-b0b6-3c73765615f6",
                       tittle="Dateset Tittle One",
                       description="Dateset Description One",
                       organization="Dateset Organization One",
                       licence="Dateset Licence One",
                       responsible="Dateset Responsible One",
                       email_responsible="Dateset Email Responsible One",
                       frequency="INVALIDO",
                       date_start_temporal_coverage=datetime.datetime.now(),
                       date_end_temporal_coverage=datetime.datetime.now(),
                       space_coverage="INVALIDO",
                       version="1.0.0",
                       space_coverage_value="10",
                       spatial_granularity="INVALIDO",
                       version_update=True,
                       visibility="INVALIDO",
                       approval_status="INVALIDO",
                       discontinued=True,
                       date_discontinuation=datetime.date.today(),
                       reuse=True,
                       themes=[
                           ThemeModel(name="Theme One", tittle="Description Theme One"),
                           ThemeModel(name="Theme Two", tittle="Description Theme Two"),
                       ],
                       tags=[
                           TagModel(id="teste_tag", name="tag_1"),
                           TagModel(id="teste_tag", name="tag_2"),
                           TagModel(id="teste_tag", name="tag_3"),
                       ],
                       resources=[
                           ResourceModel(id="e668f214-e24a-4eda-b0b6-3c73765615d3",
                                         tittle="Resource One",
                                         description="Description resource One",
                                         link="https://...",
                                         type="INVALIDO"),
                           ResourceModel(id="1b9ed187-70d0-4f92-be56-48be6b3d781c",
                                         tittle="Resource Two",
                                         description="Description resource Two",
                                         link="https://...",
                                         type="INVALIDO")
                       ])

api_client = ApiClient(Settings(api_key='<YOUR_API_KEY>'))
dataset_api = DatasetApi(api_client)

response = dataset_api.create(dataset)
```
> In this example we initialize an object of type Dataset and insert a new record

```python
from dados_gov import Settings, ApiClient
from dados_gov.resources.dataset_api import DatasetApi

api_client = ApiClient(Settings(api_key='<YOUR_API_KEY>'))
dataset_api = DatasetApi(api_client)

response = dataset_api.list(page=1)
```
> In this example we list all the datasets for page number one

**Obs: In this first version, the data returned is generic, in the future it will be deserialized into domain objects**

## Environment variables.

Environment variables are one of the ways to configure the library for use, so none of the parameters are mandatory, 
assuming that if not informed, it is expected that the `ApiClient(...)` class.

Below is a table containing the accepted environment variables.

| Name                 | Description  | Default              | Optional |
|----------------------|--------------|----------------------|----------|
| DATA_GOV_HOST        | API base URL | https://dados.gov.br | true     |
| DATA_GOV_API_KEY     | Access key   | null                 | true     |
| DATA_GOV_TIMEOUT     | Timeout      | 5000                 | true     |
| DATA_GOV_PROXY_HTTP  | Proxy HTTP   | null                 | true     |
| DATA_GOV_PROXY_HTTPS | Proxy HTTPS  | null                 | true     |

## References

- [https://dados.gov.br/](https://dados.gov.br/)
- [https://www.gov.br/transferegov/pt-br/obrasgov/sobre](https://www.gov.br/transferegov/pt-br/obrasgov/sobre)
- [Swagger](https://dados.gov.br/swagger-ui/index.html).



