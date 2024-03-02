from __future__ import absolute_import

import datetime
from dataclasses import dataclass
from typing import Any


@dataclass
class HttpResponse(object):
    status_code: int
    headers: dict
    content: dict
    text: str
    elapsed: datetime.timedelta

