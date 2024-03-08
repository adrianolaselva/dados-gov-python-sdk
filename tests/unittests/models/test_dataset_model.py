import json

from datetime import datetime, date

from dados_gov.commons import EnhancedJSONEncoder
from dados_gov.models import DatasetModel
from dados_gov.models.dataset_model import TagModel, ResourceModel, ThemeModel
from tests.fixtures import ApiResourcesTestCaseFixture


class TestDatasetModel(ApiResourcesTestCaseFixture):

    def test_should_serialize_dataset_in_json_treating_all_attributes(self):
        dataset = DatasetModel(id="e668f214-e24a-4eda-b0b6-3c73765615f6",
                               tittle="Dateset Tittle One",
                               description="Dateset Description One",
                               organization="Dateset Organization One",
                               licence="Dateset Licence One",
                               responsible="Dateset Responsible One",
                               email_responsible="Dateset Email Responsible One",
                               frequency="INVALIDO",
                               date_start_temporal_coverage=datetime.now(),
                               date_end_temporal_coverage=datetime.now(),
                               space_coverage="INVALIDO",
                               version="1.0.0",
                               space_coverage_value="10",
                               spatial_granularity="INVALIDO",
                               version_update=True,
                               visibility="INVALIDO",
                               approval_status="INVALIDO",
                               discontinued=True,
                               date_discontinuation=date.today(),
                               reuse=True,
                               themes=[
                                   ThemeModel(name="Theme One", tittle="Description Theme One"),
                                   ThemeModel(name="Theme Two", tittle="Description Theme Two"),
                               ],
                               tags=[
                                   TagModel(id="teste_tag", name="tag_1"),
                                   TagModel(id="teste_tag", name="tag_2"),
                                   TagModel(id="teste_tag", name="tag_3"),
                               ],
                               resources=[
                                   ResourceModel(id="e668f214-e24a-4eda-b0b6-3c73765615d3",
                                                 title="Resource One",
                                                 description="Description resource One",
                                                 link="https://...",
                                                 type="INVALIDO"),
                                   ResourceModel(id="1b9ed187-70d0-4f92-be56-48be6b3d781c",
                                                 title="Resource Two",
                                                 description="Description resource Two",
                                                 link="https://...",
                                                 type="INVALIDO")
                               ])

        serialized_raw_dataset = json.dumps(dataset, cls=EnhancedJSONEncoder)
        deserialized_dataset = json.loads(serialized_raw_dataset)

        self.assertEqual(deserialized_dataset['id'], dataset.id)
        self.assertEqual(deserialized_dataset['titulo'], dataset.tittle)
        self.assertEqual(deserialized_dataset['descricao'], dataset.description)
        self.assertEqual(deserialized_dataset['organizacao'], dataset.organization)
        self.assertEqual(deserialized_dataset['licenca'], dataset.licence)
        self.assertEqual(deserialized_dataset['responsavel'], dataset.responsible)
        self.assertEqual(deserialized_dataset['emailResponsavel'], dataset.email_responsible)
        self.assertEqual(deserialized_dataset['periodicidade'], dataset.frequency)
        self.assertEqual(deserialized_dataset['coberturaTemporalInicio'],
                         dataset.date_start_temporal_coverage.strftime('%Y-%m-%d'))
        self.assertEqual(deserialized_dataset['coberturaTemporalFim'],
                         dataset.date_end_temporal_coverage.strftime('%Y-%m-%d'))
        self.assertEqual(deserialized_dataset['coberturaEspacial'], dataset.space_coverage)
        self.assertEqual(deserialized_dataset['versao'], dataset.version)
        self.assertEqual(deserialized_dataset['valorCoberturaEspacial'], dataset.space_coverage_value)
        self.assertEqual(deserialized_dataset['granularidadeEspacial'], dataset.spatial_granularity)
        self.assertEqual(deserialized_dataset['atualizacaoVersao'], dataset.version_update)
        self.assertEqual(deserialized_dataset['visibilidade'], dataset.visibility)
        self.assertEqual(deserialized_dataset['statusHomologacao'], dataset.approval_status)
        self.assertEqual(deserialized_dataset['descontinuado'], dataset.discontinued)
        self.assertEqual(deserialized_dataset['dataDescontinuacao'],
                         dataset.date_discontinuation.strftime('%Y-%m-%d'))
        self.assertEqual(deserialized_dataset['reuso'], dataset.reuse)
