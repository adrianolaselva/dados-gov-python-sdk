import json

from datetime import datetime, date

from dados_gov.commons import EnhancedJSONEncoder
from dados_gov.models import DatasetModel
from dados_gov.models.dataset_model import TagModel, ResourceModel, ThemeModel
from tests.fixtures import ApiResourcesTestCaseFixture


class TestResourceModel(ApiResourcesTestCaseFixture):

    def test_should_serialize_resource_in_json_treating_all_attributes(self):
        resource = ResourceModel(id="e668f214-e24a-4eda-b0b6-3c73765615f6",
                                 dataset_id="e668f214-e24a-4eda-b0b6-3c7376561588",
                                 title="Resource Title",
                                 description="Resource Description",
                                 link="https://...",
                                 format="UNDEFINED",
                                 type="INVALIDO")

        serialized_raw_resource = json.dumps(resource, cls=EnhancedJSONEncoder)
        deserialized_resource = json.loads(serialized_raw_resource)

        self.assertEqual(deserialized_resource['id'], resource.id)
        self.assertEqual(deserialized_resource['idConjuntoDados'], resource.dataset_id)
        self.assertEqual(deserialized_resource['descricao'], resource.description)
        self.assertEqual(deserialized_resource['link'], resource.link)
        self.assertEqual(deserialized_resource['formato'], resource.format)
        self.assertEqual(deserialized_resource['tipo'], resource.type)
