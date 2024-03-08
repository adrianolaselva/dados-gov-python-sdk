from dataclasses import dataclass

from dados_gov.models.base_model import BaseModel


@dataclass
class ResourceModel(BaseModel):
    id: str = None
    dataset_id: str = None
    tittle: str = None
    link: str = None
    description: str = None
    type: str = None
    format: str = None

    def attribute_mapping(self):
        return {
            'id': 'id',
            'dataset_id': 'idConjuntoDados',
            'tittle': 'titulo',
            'link': 'link',
            'description': 'descricao',
            'type': 'tipo',
            'format': 'formato',
        }
