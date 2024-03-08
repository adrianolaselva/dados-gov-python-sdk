import datetime
import json
import urllib.parse

from parameterized import parameterized

from dados_gov.commons import EnhancedJSONEncoder
from dados_gov.models import DatasetModel
from dados_gov.models.dataset_model import TagModel, ResourceModel, ThemeModel
from dados_gov.resources.resource_api import ResourceApi
from tests.fixtures import ApiResourcesTestCaseFixture, HandleFileFixture


class TestResourceApi(ApiResourcesTestCaseFixture):

    def setUp(self):
        super().setUp()
        self.resource_api = ResourceApi(self.api_client)

    @parameterized.expand([
        "resources/test_resource_api/should_create_resource_successfully_2xx_001.json",
    ])
    def test_should_create_resource_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.resource_api.create(ResourceModel(id=content_text['request_content']['id'],
                                                          dataset_id=content_text['request_content']['idConjuntoDados'],
                                                          title=content_text['request_content']['titulo'],
                                                          description=content_text['request_content']['descricao'],
                                                          link=content_text['request_content']['titulo'],
                                                          type=content_text['request_content']['tipo'],
                                                          format=content_text['request_content']['formato']))

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(content_text['request_content']['id'], response.content['id'])
        self.assertEqual(payload_response, response.text)

    @parameterized.expand([
        "resources/test_resource_api/should_delete_resource_successfully_2xx_001.json",
    ])
    def test_should_delete_resource_successfully(self, content_path: str):
        content_text = HandleFileFixture.load_json_contents(content_path)
        payload_response = json.dumps(content_text['response_content'])

        self.adapter.register_uri(method=content_text['method'],
                                  url=urllib.parse.urljoin(self.settings.host, content_text['endpoint']),
                                  status_code=content_text['response_status_code'],
                                  headers=content_text['response_headers'],
                                  text=payload_response)

        response = self.resource_api.delete(content_text['params']['id'])

        self.assertEqual(content_text['response_status_code'], response.status_code)
        self.assertDictEqual(content_text['response_headers'], response.headers)
        self.assertEqual(content_text['params']['id'], response.content['id'])
        self.assertEqual(payload_response, response.text)
