import dataclasses
import json
from typing import Any

from dados_gov.models.dataset_model import BaseModel


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, data) -> dict[str, Any]:
        if isinstance(data, BaseModel):
            return data.to_dict()

        if dataclasses.is_dataclass(data):
            return dataclasses.asdict(data)

        return super().default(data)
