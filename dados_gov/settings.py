from __future__ import absolute_import

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Settings(object):
    host: str = "https://dados.gov.br"
    api_key: str = ""
    refresh_api_key_hook = None
    throwable = False
    timeout: int = 5000
    proxies: dict = None

    def get_host(self) -> str:
        return os.environ.get("DATA_GOV_HOST", default=self.host)

    def get_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "chave-api-dados-abertos": os.environ.get("DATA_GOV_API_KEY", default=self.api_key),
        }

    def get_proxies(self) -> dict:
        if self.proxies is not None:
            return self.proxies

        proxy_http = os.environ.get("DATA_GOV_PROXY_HTTP", default=None)
        proxy_https = os.environ.get("DATA_GOV_PROXY_HTTPS", default=None)
        
        self.proxies = dict()
        if proxy_http is not None:
            self.proxies['http'] = proxy_http

        if proxy_https is not None:
            self.proxies['https'] = proxy_https

        return self.proxies

    def is_throwable(self) -> bool:
        return os.environ.get("DATA_GOV_THROWABLE", default=self.throwable)

    def get_timeout(self) -> int:
        return os.environ.get("DATA_GOV_TIMEOUT", default=self.timeout)
