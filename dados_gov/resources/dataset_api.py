from dados_gov import ApiClient, HttpResponse
from dados_gov.models import DatasetModel


class DatasetApi(object):

    def __init__(self, api_client: ApiClient = ApiClient()):
        self._api_client = api_client

    def update(self, uuid: str, content: DatasetModel, **kwargs) -> HttpResponse:
        return self._api_client.request(method='PUT',
                                        endpoint=f'/dados/api/publico/conjuntos-dado/{uuid}',
                                        content=content, **kwargs)

    def edit(self, uuid: str, content: DatasetModel, **kwargs) -> HttpResponse:
        return self._api_client.request(method='PATCH',
                                        endpoint=f'/dados/api/publico/conjuntos-dado/{uuid}',
                                        content=content, **kwargs)

    def create(self, content: DatasetModel, **kwargs) -> HttpResponse:
        return self._api_client.request(method='POST',
                                        endpoint='/dados/api/publico/conjuntos-dado',
                                        content=content, **kwargs)

    def delete(self, uuid: str, **kwargs) -> HttpResponse:
        return self._api_client.request(method='DELETE',
                                        endpoint=f'/dados/api/publico/conjuntos-dado/{uuid}',
                                        **kwargs)

    def load(self, uuid: str, **kwargs) -> HttpResponse:
        return self._api_client.request(method='GET',
                                        endpoint=f'/dados/api/publico/conjuntos-dado/{uuid}',
                                        **kwargs)

    def list(self,
             dataset_name: str = None,
             is_private: bool = None,
             organization_id: int = None,
             page: int = 1, **kwargs) -> HttpResponse:
        return self._api_client.request(method='GET',
                                        endpoint='/dados/api/publico/conjuntos-dado',
                                        params={
                                            'nomeConjuntoDados': dataset_name,
                                            'isPrivado': is_private,
                                            'idOrganizacao': organization_id,
                                            'pagina': page,
                                        }, **kwargs)

    def list_formats(self, **kwargs) -> HttpResponse:
        return self._api_client.request(method='GET',
                                        endpoint='/dados/api/publico/conjuntos-dado',
                                        params={}, **kwargs)
