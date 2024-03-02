import dataclasses
import json
from typing import Any


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, data) -> dict[str, Any]:
        if dataclasses.is_dataclass(data):
            return dataclasses.asdict(data)

        return super().default(data)
