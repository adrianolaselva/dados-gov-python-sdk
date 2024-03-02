from __future__ import absolute_import

import json
import urllib.parse
from abc import abstractmethod

from requests import Session, Response

from dados_gov.commons import EnhancedJSONEncoder
from dados_gov.exceptions import HttpRequestException
from dados_gov.http_response import HttpResponse
from dados_gov.settings import Settings


class ApiClient(object):
    session: Session = Session()

    def __init__(self,
                 settings: Settings = Settings()):
        self._settings = settings

    @abstractmethod
    def request(self,
                method: str,
                endpoint: str,
                params: dict = None,
                content: object = None, **kwargs) -> HttpResponse:
        data = content is None and json.dumps(content, cls=EnhancedJSONEncoder) or None

        response = self.session.request(url=urllib.parse.urljoin(self._settings.get_host(), endpoint),
                                        method=method,
                                        params=params,
                                        timeout=self._settings.timeout,
                                        proxies=self._settings.get_proxies(),
                                        headers=self._settings.get_headers(),
                                        data=data, **kwargs)

        return self.response_handler(response)

    @abstractmethod
    def response_handler(self, response: Response) -> HttpResponse:
        if not response.ok and self._settings.is_throwable():
            raise HttpRequestException(f"http-request-failure: ["
                                       f"status_code: {response.status_code}, "
                                       f"headers: {response.headers.__str__()}"
                                       f"content: {response.text}, "
                                       f"elapsed: {response.elapsed}]")

        return HttpResponse(status_code=response.status_code,
                            content=response.json(),
                            text=response.text,
                            headers=dict(response.headers),
                            elapsed=response.elapsed)
