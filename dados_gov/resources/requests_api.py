from datetime import datetime

from dados_gov import ApiClient, HttpResponse


class RequestsApi(object):

    def __init__(self, api_client: ApiClient = ApiClient()):
        self._api_client = api_client

    def response_to_requests(self, request_id: int, response_message: str, **kwargs) -> HttpResponse:
        return self._api_client.request(method='POST',
                                        endpoint='/dados/api/solicitacoes/resposta',
                                        params={
                                            "idSolicitacao": request_id,
                                            "resposta": response_message
                                        }, **kwargs)

    def list(self,
             opening_date: datetime = None,
             request_type: str = None,
             request_state: str = None, **kwargs) -> HttpResponse:
        opening_date_formatted = None
        if opening_date is not None:
            opening_date_formatted = opening_date.strftime('%Y-%m-%d')

        return self._api_client.request(method='GET',
                                        endpoint='/dados/api/solicitacoes',
                                        params={
                                            'dataAbertura': opening_date_formatted,
                                            'tipoSolicitacao': request_type,
                                            'statusSolicitacao': request_state
                                        }, **kwargs)
