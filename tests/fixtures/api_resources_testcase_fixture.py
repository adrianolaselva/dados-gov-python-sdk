import unittest

import requests_mock

from dados_gov import Settings, ApiClient
from tests import ROOT_DIR_TESTS


class ApiResourcesTestCaseFixture(unittest.TestCase):

    def setUp(self):
        self.settings = Settings(host='https://dados.gov.br')
        self.api_client = ApiClient(self.settings)
        self.adapter = requests_mock.Adapter()
        self.api_client.session.mount('https://', self.adapter)
