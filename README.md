# REST API of the Brazilian Federal Government Open Data Portal

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
pip install dados-gov-sdk@1.0.0
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

```
> Api Client initialization example

```python

```
> Resource Query Example

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



