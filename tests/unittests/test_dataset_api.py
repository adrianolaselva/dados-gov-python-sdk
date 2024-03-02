import json
import unittest
import urllib.parse

from parameterized import parameterized

from dados_gov.models import DatasetModel
from dados_gov.resources.dataset_api import DatasetApi
from tests.fixtures import ApiResourcesTestCaseFixture, HandleFileFixture


class TestDatasetApi(ApiResourcesTestCaseFixture):

    def setUp(self):
        super().setUp()
        self.dataset_api = DatasetApi(self.api_client)

    @parameterized.expand([
        f"resources/{__name__}/should_update_dataset_successfully_2xx_001.json",
    ])
    def test_should_update_dataset_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.dataset_api.update(content_text['request_content']['id'], DatasetModel(
            id=content_text['request_content']['id'],
            title=content_text['request_content']['title']))

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(content_text['request_content']['id'], response.content['id'])
        self.assertEqual(payload_response, response.text)

    @parameterized.expand([
        f"resources/{__name__}/should_edit_dataset_successfully_2xx_001.json",
    ])
    def test_should_edit_dataset_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.dataset_api.edit(content_text['request_content']['id'], DatasetModel(
            id=content_text['request_content']['id'],
            title=content_text['request_content']['id'],
            notes=content_text['request_content']['notes'],
            data_hora_atualizacao=content_text['request_content']['dataAtualizacao']))

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(content_text['request_content']['id'], response.content['id'])
        self.assertEqual(payload_response, response.text)

    @parameterized.expand([
        f"resources/{__name__}/should_create_dataset_successfully_2xx_001.json",
    ])
    def test_should_create_dataset_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.dataset_api.create(DatasetModel(
            id=content_text['request_content']['id'],
            title=content_text['request_content']['id'],
            notes=content_text['request_content']['notes'],
            data_hora_atualizacao=content_text['request_content']['dataAtualizacao']))

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(content_text['request_content']['id'], response.content['id'])
        self.assertEqual(payload_response, response.text)

    @parameterized.expand([
        f"resources/{__name__}/should_delete_dataset_successfully_2xx_001.json",
    ])
    def test_should_delete_dataset_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.dataset_api.delete(content_text['params']['id'])

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(content_text['params']['id'], response.content['id'])
        self.assertEqual(payload_response, response.text)

    @parameterized.expand([
        f"resources/{__name__}/should_load_dataset_successfully_2xx_001.json",
        f"resources/{__name__}/should_load_dataset_successfully_2xx_002.json",
    ])
    def test_should_load_dataset_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.dataset_api.load(content_text['params']['id'])

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(content_text['params']['id'], response.content['id'])
        self.assertEqual(payload_response, response.text)

    @parameterized.expand([
        f"resources/{__name__}/should_list_datasets_successfully_2xx_001.json",
        f"resources/{__name__}/should_list_datasets_successfully_2xx_002.json",
        f"resources/{__name__}/should_list_datasets_successfully_2xx_003.json",
        f"resources/{__name__}/should_list_datasets_successfully_2xx_004.json",
        f"resources/{__name__}/should_list_datasets_successfully_2xx_005.json",
        f"resources/{__name__}/should_list_datasets_successfully_2xx_006.json",
    ])
    def test_should_list_datasets_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.dataset_api.list()

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(payload_response, response.text)


if __name__ == '__main__':
    unittest.main()
