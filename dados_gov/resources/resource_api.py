from datetime import datetime

from dados_gov import ApiClient, HttpResponse
from dados_gov.models.dataset_model import ResourceModel


class ResourceApi(object):

    def __init__(self, api_client: ApiClient = ApiClient()):
        self._api_client = api_client

    def create(self, content: ResourceModel, **kwargs) -> HttpResponse:
        return self._api_client.request(method='POST',
                                        endpoint='/dados/api/recurso/salvar',
                                        content=content, **kwargs)

    def delete(self, uuid: str, **kwargs) -> HttpResponse:
        return self._api_client.request(method='DELETE',
                                        endpoint=f'/dados/api/recurso/{uuid}',
                                        **kwargs)
