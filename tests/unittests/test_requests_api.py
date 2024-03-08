import json
import unittest
import urllib.parse
from datetime import datetime

from parameterized import parameterized

from dados_gov.resources.requests_api import RequestsApi
from tests.fixtures import ApiResourcesTestCaseFixture, HandleFileFixture


class TestRequestsApi(ApiResourcesTestCaseFixture):

    def setUp(self):
        super().setUp()
        self.requests_api = RequestsApi(self.api_client)

    @parameterized.expand([
        f"resources/{__name__}/should_response_to_requests_successfully_2xx_001.json",
    ])
    def test_should_response_to_requests_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.requests_api.response_to_requests(request_id=content_text['request_content']['idSolicitacao'],
                                                          response_message=content_text['request_content']['resposta'])

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(payload_response, response.text)

    @parameterized.expand([
        f"resources/{__name__}/should_list_requests_successfully_2xx_001.json",
    ])
    def test_should_list_requests_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        opening_date = datetime.strptime(content_text['request_content']['dataAbertura'], "%Y-%m-%d")

        response = self.requests_api.list(opening_date=opening_date,
                                          request_type=content_text['request_content']['tipoSolicitacao'],
                                          request_state=content_text['request_content']['statusSolicitacao'])

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(payload_response, response.text)


if __name__ == '__main__':
    unittest.main()
