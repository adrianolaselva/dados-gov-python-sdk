from dataclasses import dataclass
from datetime import datetime, date
from typing import List

from dados_gov.models.base_model import BaseModel


@dataclass
class ThemeModel(BaseModel):
    name: str = None
    tittle: str = None

    def attribute_mapping(self):
        return {
            'name': 'name',
            'tittle': 'tittle',
        }


@dataclass
class TagModel(BaseModel):
    id: str = None
    name: str = None
    display_name: str = None

    def attribute_mapping(self):
        return {
            'id': 'id',
            'name': 'name',
            'display_name': 'display_name',
        }


@dataclass
class ResourceModel(BaseModel):
    id: str = None
    dataset_id: str = None
    title: str = None
    link: str = None
    description: str = None
    type: str = None
    format: str = None

    def attribute_mapping(self):
        return {
            'id': 'id',
            'dataset_id': 'idConjuntoDados',
            'title': 'titulo',
            'link': 'link',
            'description': 'descricao',
            'type': 'tipo',
            'format': 'formato',
        }


@dataclass
class DatasetModel(BaseModel):
    id: str = None
    tittle: str = None
    organization: str = None
    inventory: str = None
    description: str = None
    licence: str = None
    responsible: str = None
    email_responsible: str = None
    frequency: str = None
    date_start_temporal_coverage: datetime = None
    date_end_temporal_coverage: datetime = None
    space_coverage: str = None
    space_coverage_value: str = None
    spatial_granularity: str = None
    version: str = None
    version_update: bool = None
    visibility: str = None
    approval_status: str = None
    discontinued: bool = None
    date_discontinuation: date = None
    reuse: bool = None
    associated_dataset: str = None
    source_dataset: str = None
    themes: List[ThemeModel] = None
    tags: List[TagModel] = None
    resources: List[ResourceModel] = None

    def attribute_mapping(self):
        return {
            'id': 'id',
            'tittle': 'titulo',
            'organization': 'organizacao',
            'inventory': 'inventario',
            'description': 'descricao',
            'licence': 'licenca',
            'responsible': 'responsavel',
            'themes': 'temas',
            'email_responsible': 'emailResponsavel',
            'frequency': 'periodicidade',
            'date_start_temporal_coverage': 'coberturaTemporalInicio',
            'date_end_temporal_coverage': 'coberturaTemporalFim',
            'space_coverage': 'coberturaEspacial',
            'space_coverage_value': 'valorCoberturaEspacial',
            'spatial_granularity': 'granularidadeEspacial',
            'version': 'versao',
            'version_update': 'atualizacaoVersao',
            'visibility': 'visibilidade',
            'approval_status': 'statusHomologacao',
            'discontinued': 'descontinuado',
            'date_discontinuation': 'dataDescontinuacao',
            'reuse': 'reuso',
            'associated_dataset': 'conjuntoDadosAssociados',
            'source_dataset': 'conjuntoDadosOrigem',
        }
