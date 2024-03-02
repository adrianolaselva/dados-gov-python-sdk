from dataclasses import dataclass

from typing import List, Optional

from dados_gov.models import *

@dataclass
class DatasetModel(object):
    id: str = Optional[str]
    title: str = Optional[str]
    notes: str = Optional[str]
    data_hora_atualizacao: str = Optional[str]
    # tags: List[TagDto]
    # resources: List[ResourceDto]
    # organization: OrganizationDto
    # avaliacao: DatasetEvaluationDto
    # groups: List[GroupDto]
    # name: str
    # quantidade_seguidores: int
    # maintainer: str
    # extras: List[ExtraDto]
    # version: str
    # state: str
    # author: str
    # quantidade_reusos: int
    # quantidade_downloads: int
    # conjunto_dados_associados: List[dict]
    # conjunto_dados_associados_nao_acessiveis: List[dict]
    # avaliacao_dto: AssessmentDto
    # conjunto_dados_esta_atualizado: dict
    # conjunto_dados_validado: dict
    # periodiciade: dict
    # lista_formatos: dict
    # conjunto_dados_edicao: dict
    # periodiciade_formatado: dict
    # usuario_logado_seguindo: dict
    # tags_formatado: dict
    # groups_formatado: dict
    # data_ultima_atualizacao_formatado_mes_abreviado: dict
    # resources_count: dict
    # conjunto_dados_form: dict
    # inacessivel: dict
    # visibilidade: dict
    # cobertura_espacial: dict
    # descontinuado: dict
    # metadata_modified_date_time: dict
    # owner_org: dict
    # license_id: dict
    # license_title: dict
    # metadata_created: dict
    # metadata_modified: dict
    # maintainer_email: dict
    # private: dict
    # num_resources: dict
    # markdown_notes: dict
    
    # def __iter__(self):
    #     yield from {
    #         "id": self.id,
    #         "title": self.title,
    #         "notes": self.notes,
    #         "data_hora_atualizacao": self.data_hora_atualizacao,
    #         "tags": self.tags,
    #         "resources": self.resources,
    #         "organization": self.organization,
    #         "avaliacao": self.avaliacao,
    #         "groups": self.groups,
    #         "name": self.name,
    #         "quantidade_seguidores": self.quantidade_seguidores,
    #         "maintainer": self.maintainer,
    #         "extras": self.extras,
    #         "version": self.version,
    #         "state": self.state,
    #         "author": self.author,
    #         "quantidade_reusos": self.quantidade_reusos,
    #         "quantidade_downloads": self.quantidade_downloads,
    #         "conjunto_dados_associados": self.conjunto_dados_associados,
    #         "conjunto_dados_associados_nao_acessiveis": self.conjunto_dados_associados_nao_acessiveis,
    #         "avaliacao_dto": self.avaliacao_dto,
    #         "conjunto_dados_esta_atualizado": self.conjunto_dados_esta_atualizado,
    #         "conjunto_dados_validado": self.conjunto_dados_validado,
    #         "periodiciade": self.periodiciade,
    #         "lista_formatos": self.lista_formatos,
    #         "conjunto_dados_edicao": self.conjunto_dados_edicao,
    #         "periodiciade_formatado": self.periodiciade_formatado,
    #         "usuario_logado_seguindo": self.usuario_logado_seguindo,
    #         "tags_formatado": self.tags_formatado,
    #         "groups_formatado": self.groups_formatado,
    #         "data_ultima_atualizacao_formatado_mes_abreviado": self.data_ultima_atualizacao_formatado_mes_abreviado,
    #         "resources_count": self.resources_count,
    #         "conjunto_dados_form": self.conjunto_dados_form,
    #         "inacessivel": self.inacessivel,
    #         "visibilidade": self.visibilidade,
    #         "cobertura_espacial": self.cobertura_espacial,
    #         "descontinuado": self.descontinuado,
    #         "metadata_modified_date_time": self.metadata_modified_date_time,
    #         "owner_org": self.owner_org,
    #         "license_id": self.license_id,
    #         "license_title": self.license_title,
    #         "metadata_created": self.metadata_created,
    #         "metadata_modified": self.metadata_modified,
    #         "maintainer_email": self.maintainer_email,
    #         "private": self.private,
    #         "num_resources": self.num_resources,
    #         "markdown_notes": self.markdown_notes
    #     }
